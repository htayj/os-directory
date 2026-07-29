#!/usr/bin/env python3
"""Discover and attach provisional text-editor relationships for every system."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
OUTPUT = INVENTORY / "text-editor-associations.json"
PAGE_CACHE = INVENTORY / "text-editor-page-snapshots.json"
WIKIDATA_CACHE = INVENTORY / "text-editor-wikidata.json"
USER_AGENT = "HistoricalOSCatalog/0.1 (text-editor relationship pass)"
RUN_DATE = "2026-07-29"
BLOCK_START = "# BEGIN GENERATED TEXT EDITORS"
BLOCK_END = "# END GENERATED TEXT EDITORS"
DISPOSITION_START = "# BEGIN GENERATED TEXT EDITOR DISPOSITION"
DISPOSITION_END = "# END GENERATED TEXT EDITOR DISPOSITION"

# Ambiguous names such as "Edit", "E", and "ed" are handled separately and
# require explicit editor context.
EDITOR_PATTERNS = {
    "Acme": r"\bAcme\b",
    "AMIS": r"\bAMIS\b",
    "aXe": r"\baXe\b",
    "BBEdit": r"\bBBEdit\b",
    "BRIEF": r"\bBRIEF\b",
    "CygnusEd": r"\bCygnusEd\b",
    "DEC SED": r"\b(?:DEC )?SED\b",
    "Eddie": r"\bEddie\b",
    "EDLIN": r"\bEDLIN\b",
    "Emacs": r"\b(?:GNU |Micro|X)?Emacs\b",
    "Epsilon": r"\bEpsilon\b",
    "EVE": r"\bEVE\b",
    "ex": r"\bex editor\b|\bex text editor\b",
    "FINE": r"\bFINE\b",
    "GNU nano": r"\b(?:GNU )?nano\b(?!-)",
    "gedit": r"\bgedit\b",
    "Hemlock": r"\bHemlock\b",
    "ISPF editor": r"\bISPF (?:text )?editor\b",
    "JED": r"\bJED\b",
    "JOE": r"\bJOE\b|\bJoe'?s Own Editor\b",
    "jot": r"\bjot\b",
    "Kate": r"\bKate\b",
    "KEDIT": r"\bKEDIT\b",
    "KWrite": r"\bKWrite\b",
    "Leafpad": r"\bLeafpad\b",
    "LSE": r"\bLanguage-Sensitive Editor\b|\bLSE\b",
    "Mined": r"\bMined\b",
    "MS-DOS Editor": r"\bMS-DOS Editor\b|\bMS-DOS EDIT\b",
    "NEdit": r"\bNEdit\b",
    "Notepad": r"\b(?:Microsoft )?Notepad\b",
    "O26": r"\bO26\b",
    "Pico": r"\bPico\b",
    "Pluma": r"\bPluma\b",
    "QED": r"\bQED\b",
    "qedx": r"\bqedx\b",
    "Sam": r"\bsam text editor\b|\bsam editor\b",
    "SimpleText": r"\bSimpleText\b",
    "SOS": r"\bSOS editor\b|\bSon of Stopgap\b",
    "StyledEdit": r"\bStyledEdit\b",
    "TeachText": r"\bTeachText\b",
    "TECO": r"\bTECO\b",
    "TextEdit": r"\bTextEdit\b",
    "The Hessling Editor": r"\bThe Hessling Editor\b|\bTHE editor\b",
    "TPU": r"\bText Processing Utility\b|\bTPU\b",
    "vi": r"\bvi(?: text)? editor\b|\bvi\b(?=.{0,30}\beditor\b)",
    "Vim": r"\bVim\b",
    "vile": r"\bvile\b",
    "Visual Studio Code": r"\bVisual Studio Code\b|\bVS Code\b",
    "WordPad": r"\bWordPad\b",
    "XEDIT": r"\bXEDIT\b",
    "Xi": r"\bXi editor\b|\bXi text editor\b",
    "Zed": r"\bZed\b",
    "Zmacs": r"\bZmacs\b",
}
EXPLICIT_EDITOR_RE = re.compile(
    r"\b(?:text|line|screen|source-code|source code|program|structure) editor\b",
    re.I,
)
WIKIDATA_EXCLUDED_LABELS = {
    # These are directly typed as text editors in Wikidata, but their primary
    # function falls outside this catalog's plain-text/source-editor scope.
    "ChiWriter",
    "CintaNotes",
    "Dramatica",
    "Evernote",
    "Frescobaldi",
    "GNU TeXmacs",
    "Logseq",
    "SWI-Prolog",
    "TheDraw",
    "WPCleaner",
    "Zim Desktop Wiki",
}
PAGE_EXCLUSIONS = {
    # The 86-DOS article contrasts EDLIN with MS-DOS Editor, which appeared in
    # the much later MS-DOS 5.0; the latter is not an 86-DOS association.
    "systems/86-dos": {"ms-dos editor"},
}


def api_request(url: str, params: dict) -> dict:
    last_error = ""
    for attempt in range(5):
        response = requests.get(
            url,
            params=params,
            headers={"User-Agent": USER_AGENT},
            timeout=60,
        )
        if response.status_code in {429, 500, 502, 503, 504}:
            last_error = f"HTTP {response.status_code}"
            time.sleep(max(2**attempt, 15 if response.status_code == 429 else 0))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError(f"request failed: {last_error}")


def chunks(values: list, size: int):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def frontmatter(record: Path) -> dict:
    text = record.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def all_systems() -> dict[str, dict]:
    result = {}
    for record in sorted((ROOT / "systems").glob("*/system.md")):
        path = str(record.parent.relative_to(ROOT))
        data = frontmatter(record)
        result[path] = {
            "record": record,
            "title": data.get("title", record.parent.name),
            "deep_research": data.get("deep_research", {}),
        }
    return result


def linked_pages() -> dict[str, str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import enrich_from_enwiki_infoboxes  # noqa: PLC0415

    mapping = enrich_from_enwiki_infoboxes.system_urls()
    multilingual_candidates = {
        item["candidate_id"]: item
        for item in json.loads(
            (INVENTORY / "multilingual" / "candidates-normalized.json").read_text(
                encoding="utf-8"
            )
        )
    }
    for result_path in sorted(
        (INVENTORY / "multilingual" / "results").glob("batch-*.json")
    ):
        for item in json.loads(result_path.read_text(encoding="utf-8"))["results"]:
            candidate = multilingual_candidates[item["candidate_id"]]
            entries = candidate["entries"]
            url = next(
                (
                    entry.get("english_sitelink")
                    for entry in entries
                    if entry.get("english_sitelink")
                ),
                None,
            ) or next(
                (
                    entry.get("native_url")
                    for entry in entries
                    if entry.get("native_url")
                    and "wikipedia.org/" in entry["native_url"]
                ),
                None,
            )
            if url:
                mapping[item["path"].rstrip("/")] = url
    mapping["systems/explorer-system-software"] = (
        "https://en.wikipedia.org/wiki/Texas_Instruments_Explorer"
    )
    return mapping


def wiki_site_title(url: str) -> tuple[str, str, str] | None:
    parsed = urlsplit(url)
    if not parsed.hostname or not parsed.hostname.endswith(".wikipedia.org"):
        return None
    language = parsed.hostname.removesuffix(".wikipedia.org")
    path = unquote(parsed.path)
    if not path.startswith("/wiki/"):
        return None
    title = path.removeprefix("/wiki/").split("#", 1)[0].replace("_", " ")
    return language, f"https://{parsed.hostname}/w/api.php", title


def fetch_page_snapshots(mapping: dict[str, str]) -> dict[str, dict]:
    requests_by_wiki: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for path, url in mapping.items():
        parsed = wiki_site_title(url)
        if parsed:
            language, api_url, title = parsed
            requests_by_wiki[(language, api_url)][title].append(path)

    snapshots: dict[str, dict] = {}
    for (language, api_url), titles in sorted(requests_by_wiki.items()):
        for batch in chunks(sorted(titles), 20):
            data = api_request(
                api_url,
                {
                    "action": "query",
                    "format": "json",
                    "formatversion": 2,
                    "prop": "extracts|revisions",
                    "explaintext": 1,
                    "exsectionformat": "plain",
                    "rvprop": "ids|timestamp",
                    "redirects": 1,
                    "titles": "|".join(batch),
                },
            )
            resolved: dict[str, set[str]] = {title: {title} for title in batch}
            for item in data.get("query", {}).get("normalized", []):
                originals = resolved.pop(item["from"], {item["from"]})
                resolved.setdefault(item["to"], set()).update(originals)
            for item in data.get("query", {}).get("redirects", []):
                originals = resolved.pop(item["from"], {item["from"]})
                resolved.setdefault(item["to"], set()).update(originals)
            for page in data.get("query", {}).get("pages", []):
                requested_titles = resolved.get(page.get("title"), {page.get("title")})
                revision = (page.get("revisions") or [{}])[0]
                source = (
                    f"https://{language}.wikipedia.org/w/index.php?"
                    f"title={quote(page.get('title', '').replace(' ', '_'))}"
                    f"&oldid={revision.get('revid')}"
                    if revision.get("revid")
                    else None
                )
                snapshot = {
                    "language": language,
                    "title": page.get("title"),
                    "revision": revision.get("revid"),
                    "timestamp": revision.get("timestamp"),
                    "source": source,
                    "extract": page.get("extract", ""),
                }
                for original in requested_titles:
                    for path in titles.get(original, []):
                        snapshots[path] = snapshot
    return snapshots


def sentences(text: str) -> list[str]:
    for marker in (
        "\nSee also\n",
        "\nReferences\n",
        "\nFurther reading\n",
        "\nExternal links\n",
    ):
        text = text.split(marker, 1)[0]
    return [
        re.sub(r"\s+", " ", part).strip()
        for part in re.split(r"(?<=[.!?])\s+|\n+", text)
        if part.strip()
    ]


def relationship(sentence: str) -> str:
    lower = sentence.casefold()
    if "default" in lower and "editor" in lower:
        return "bundled-default"
    if any(word in lower for word in ("bundled", "included", "ships with", "comes with")):
        return "bundled-optional"
    if "integrated" in lower or "integral" in lower:
        return "integral"
    if "native" in lower:
        return "native"
    if "port" in lower or "ported" in lower:
        return "ported"
    return "historically-prominent"


def page_associations(snapshot: dict) -> list[dict]:
    associations: dict[str, dict] = {}
    for sentence in sentences(snapshot.get("extract", "")):
        if len(sentence) > 1000:
            continue
        for name, pattern in EDITOR_PATTERNS.items():
            flags = 0 if name in {
                "AMIS", "DEC SED", "EDLIN", "EVE", "FINE", "ISPF editor",
                "JOE", "LSE", "QED", "SOS", "TECO", "TPU", "XEDIT",
            } else re.I
            if not re.search(pattern, sentence, flags):
                continue
            # Short or generic names require the sentence to establish editor context.
            if name in {
                "AMIS", "EVE", "FINE", "GNU nano", "JOE", "Kate", "QED",
                "SOS", "TPU", "Zed",
            }:
                if not EXPLICIT_EDITOR_RE.search(sentence):
                    continue
            associations[name] = {
                "name": name,
                "relationship": relationship(sentence),
                "interface_style": None,
                "source": snapshot.get("source"),
                "source_kind": "wikipedia-system-page",
                "source_revision": snapshot.get("revision"),
                "assertion_status": "provisional",
            }
    return list(associations.values())


def system_qids(mapping: dict[str, str]) -> dict[str, str]:
    countries = json.loads(
        (INVENTORY / "wikidata-country-origins.json").read_text(encoding="utf-8")
    )
    result = {
        path: countries[url]["wikidata_entity"]
        for path, url in mapping.items()
        if url in countries and countries[url].get("wikidata_entity")
    }
    multilingual = json.loads(
        (
            INVENTORY
            / "multilingual"
            / "wikidata-attribute-snapshots.json"
        ).read_text(encoding="utf-8")
    )
    result.update(
        {
            path: item["wikidata_entity"]
            for path, item in multilingual.items()
            if item.get("wikidata_entity")
        }
    )
    return result


def wikidata_associations(path_qids: dict[str, str]) -> tuple[dict[str, list[dict]], dict]:
    query = """SELECT ?editor ?editorLabel ?os WHERE {
      ?editor wdt:P31 wd:Q131212; wdt:P306 ?os.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }"""
    data = api_request(
        "https://query.wikidata.org/sparql",
        {"query": query, "format": "json"},
    )
    by_qid: dict[str, list[dict]] = defaultdict(list)
    raw = []
    for binding in data["results"]["bindings"]:
        editor_qid = binding["editor"]["value"].rsplit("/", 1)[-1]
        os_qid = binding["os"]["value"].rsplit("/", 1)[-1]
        editor = binding["editorLabel"]["value"]
        if editor.startswith("Q") or editor in WIKIDATA_EXCLUDED_LABELS:
            continue
        raw.append(
            {"editor_qid": editor_qid, "editor": editor, "os_qid": os_qid}
        )
        by_qid[os_qid].append(
            {
                "name": editor,
                "relationship": "supported-platform",
                "interface_style": None,
                "source": f"https://www.wikidata.org/wiki/{editor_qid}",
                "source_kind": "wikidata-P306-operating-system",
                "assertion_status": "provisional",
            }
        )
    result: dict[str, list[dict]] = {}
    for path, qid in path_qids.items():
        if qid in by_qid:
            # Deduplicate identical labels caused by repeated statements.
            result[path] = list(
                {
                    (item["name"], item["source"]): item for item in by_qid[qid]
                }.values()
            )
    return result, {"query": query, "retrieved_at": RUN_DATE, "results": raw}


def curated(
    name: str,
    relationship: str,
    source: str,
    interface_style: str | None = None,
    assertion_status: str = "provisional",
    source_kind: str = "editor-history-secondary-reference",
    note: str | None = None,
) -> dict:
    item = {
        "name": name,
        "relationship": relationship,
        "interface_style": interface_style,
        "source": source,
        "source_kind": source_kind,
        "assertion_status": assertion_status,
    }
    if note:
        item["note"] = note
    return item


ED = "https://en.wikipedia.org/wiki/Ed_(software)"
VI = "https://en.wikipedia.org/wiki/Vi_(text_editor)"
TECO = "https://en.wikipedia.org/wiki/TECO_(text_editor)"
EMACS = "https://en.wikipedia.org/wiki/Emacs"
CPM_ED = "https://en.wikipedia.org/wiki/CP/M#Commands"
MSDOS_EDITORS = "https://en.wikipedia.org/wiki/MS-DOS_Editor"
EDLIN = "https://en.wikipedia.org/wiki/Edlin"
VMS_EDITORS = "https://en.wikipedia.org/wiki/EDT_(text_editor)"
EVE = "https://en.wikipedia.org/wiki/Extensible_VAX_Editor"
XEDIT = "https://en.wikipedia.org/wiki/XEDIT"
ISPF = "https://www.ibm.com/docs/en/zos/3.2.0?topic=edit-using-editor"
PLAN9_EDITORS = "https://9p.io/sys/doc/sam/sam.html"
ACME = "https://9p.io/sys/doc/acme/acme.html"

CURATED = {
    "systems/explorer-system-software": [
        curated(
            "Zmacs",
            "integral",
            "https://bitsavers.org/pdf/ti/explorer/2243134-0001A_Glossary_6-87.pdf",
            "graphical",
            "documented",
            "contemporary-system-manual",
        )
    ],
    "systems/unix": [curated("ed", "native", ED, "line")],
    "systems/research-unix": [curated("ed", "bundled-default", ED, "line")],
    "systems/pwb-unix": [
        curated("ed", "bundled-default", ED, "line"),
        curated("vi", "historically-prominent", VI, "full-screen-text"),
    ],
    "systems/unix-system-v": [
        curated("ed", "bundled-default", ED, "line"),
        curated("vi", "bundled-default", VI, "full-screen-text"),
    ],
    "systems/system-v-at-386": [
        curated("ed", "bundled-default", ED, "line"),
        curated("vi", "bundled-default", VI, "full-screen-text"),
    ],
    "systems/xenix": [
        curated("ed", "bundled-default", ED, "line"),
        curated("vi", "ported", VI, "full-screen-text"),
    ],
    "systems/sco-unix": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/sco-unix-2": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/interactive-unix": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/unixware": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/berkeley-software-distribution": [
        curated("ex", "native", VI, "full-screen-text"),
        curated("vi", "native", VI, "full-screen-text"),
    ],
    "systems/freebsd": [
        curated("vi", "bundled-default", VI, "full-screen-text"),
        curated("ee", "bundled-default", "https://man.freebsd.org/cgi/man.cgi?ee(1)", "full-screen-text", "documented", "official-system-manual"),
    ],
    "systems/netbsd": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/openbsd": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/dragonfly-bsd": [curated("vi", "bundled-default", VI, "full-screen-text")],
    "systems/cp-m": [curated("ED", "bundled-default", CPM_ED, "line")],
    "systems/cp-m-86": [curated("ED", "bundled-default", CPM_ED, "line")],
    "systems/concurrent-cp-m": [curated("ED", "bundled-optional", CPM_ED, "line")],
    "systems/concurrent-cp-m-86": [curated("ED", "bundled-optional", CPM_ED, "line")],
    "systems/86-dos": [curated("EDLIN", "bundled-default", EDLIN, "line")],
    "systems/ms-dos": [
        curated("EDLIN", "bundled-default", EDLIN, "line"),
        curated("MS-DOS Editor", "bundled-default", MSDOS_EDITORS, "full-screen-text", note="Bundled beginning with MS-DOS 5.0."),
    ],
    "systems/pc-dos": [curated("EDLIN", "bundled-default", EDLIN, "line")],
    "systems/freedos": [
        curated("FreeDOS Edit", "bundled-default", "https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/edit/", "full-screen-text", "documented", "project-distribution-archive")
    ],
    "systems/windows": [
        curated("Notepad", "bundled-default", "https://learn.microsoft.com/en-us/windows/apps/design/controls/rich-edit-box", "graphical", "documented", "vendor-documentation")
    ],
    "systems/windows-nt": [
        curated("Notepad", "bundled-default", "https://en.wikipedia.org/wiki/Windows_Notepad", "graphical"),
        curated("WordPad", "bundled-default", "https://en.wikipedia.org/wiki/WordPad", "graphical"),
    ],
    "systems/classic-mac-os": [
        curated("TeachText", "bundled-default", "https://en.wikipedia.org/wiki/TeachText", "graphical"),
        curated("SimpleText", "bundled-default", "https://en.wikipedia.org/wiki/SimpleText", "graphical"),
    ],
    "systems/macos": [
        curated("TextEdit", "bundled-default", "https://support.apple.com/guide/textedit/welcome/mac", "graphical", "documented", "vendor-documentation")
    ],
    "systems/nextstep": [
        curated("Edit", "bundled-default", "https://www.nextop.de/NeXTstep_3.3/nsa/05_UserInterface/05_UserInterface.htmld/index.html", "graphical", source_kind="contemporary-system-documentation")
    ],
    "systems/os-2": [
        curated("E", "bundled-default", "https://en.wikipedia.org/wiki/E_(PC_DOS)", "full-screen-text"),
        curated("EPM", "bundled-default", "https://en.wikipedia.org/wiki/EPM_(software)", "graphical"),
    ],
    "systems/osfree": [
        curated("E", "historically-prominent", "https://en.wikipedia.org/wiki/E_(PC_DOS)", "full-screen-text"),
        curated("EPM", "historically-prominent", "https://en.wikipedia.org/wiki/EPM_(software)", "graphical"),
    ],
    "systems/amigaos": [
        curated("Ed", "bundled-default", "https://wiki.amigaos.net/wiki/AmigaOS_Manual:_AmigaDOS_Command_Reference#Ed", "full-screen-text", "documented", "official-system-manual"),
        curated("MEmacs", "bundled-default", "https://wiki.amigaos.net/wiki/AmigaOS_Manual:_AmigaDOS_Command_Reference#MEmacs", "full-screen-text", "documented", "official-system-manual"),
    ],
    "systems/beos": [curated("StyledEdit", "bundled-default", "https://www.haiku-os.org/legacy-docs/bebook/TheStyledEditApplication.html", "graphical", source_kind="system-documentation")],
    "systems/haiku": [curated("StyledEdit", "bundled-default", "https://www.haiku-os.org/docs/userguide/en/applications/stylededit.html", "graphical", "documented", "official-system-manual")],
    "systems/risc-os": [curated("Edit", "bundled-default", "https://www.riscosopen.org/wiki/documentation/show/Edit", "graphical", "documented", "official-system-manual")],
    "systems/oberon-operating-system": [curated("Edit", "integral", "https://people.inf.ethz.ch/wirth/ProjectOberon/PO.System.pdf", "structural", "documented", "contemporary-system-manual")],
    "systems/plan-9-from-bell-labs": [
        curated("sam", "first-party", PLAN9_EDITORS, "graphical", "documented", "contemporary-system-paper"),
        curated("acme", "first-party", ACME, "graphical", "documented", "contemporary-system-paper"),
    ],
    "systems/inferno": [curated("acme", "ported", ACME, "graphical")],
    "systems/minix": [curated("Mined", "bundled-default", "https://man.minix3.org/cgi-bin/man.cgi?query=mined&sektion=1", "full-screen-text", "documented", "official-system-manual")],
    "systems/vms": [
        curated("EDT", "first-party", VMS_EDITORS, "full-screen-text"),
        curated("EVE", "first-party", EVE, "full-screen-text"),
    ],
    "systems/rt-11": [curated("EDIT", "bundled-default", "https://bitsavers.org/pdf/dec/pdp11/rt11/AA-PD6PA-TC_RT-11_System_Utilities_Manual_Aug91.pdf", "full-screen-text", "documented", "contemporary-system-manual")],
    "systems/rsx-11": [curated("EDT", "first-party", VMS_EDITORS, "full-screen-text")],
    "systems/rsts-e": [curated("EDT", "first-party", VMS_EDITORS, "full-screen-text")],
    "systems/os-8": [curated("EDIT", "bundled-default", "https://bitsavers.org/pdf/dec/pdp8/os8/DEC-S8-OSSMB-A-D_OS8_Handbook_Apr74.pdf", "line", "documented", "contemporary-system-manual")],
    "systems/tenex": [
        curated("TECO", "historically-prominent", TECO, "terminal"),
        curated("Emacs", "native", EMACS, "full-screen-text"),
    ],
    "systems/tops-10": [
        curated("TECO", "first-party", TECO, "terminal"),
        curated("SOS", "first-party", "https://en.wikipedia.org/wiki/SOS_(text_editor)", "line"),
    ],
    "systems/tops-20": [
        curated("TECO", "first-party", TECO, "terminal"),
        curated("Emacs", "native", EMACS, "full-screen-text"),
    ],
    "systems/incompatible-timesharing-system": [
        curated("TECO", "integral", TECO, "terminal"),
        curated("Emacs", "native", EMACS, "full-screen-text"),
    ],
    "systems/multics": [
        curated("qedx", "native", "https://www.multicians.org/mepap.html", "line", "documented", "historical-system-archive"),
        curated("Multics Emacs", "native", EMACS, "full-screen-text"),
    ],
    "systems/cp-cms": [curated("EDIT", "bundled-default", XEDIT, "line")],
    "systems/os-360": [curated("TSO EDIT", "first-party", ISPF, "line", note="Applies to OS/360 configurations with TSO.")],
    "systems/os-390": [curated("ISPF editor", "bundled-optional", ISPF, "full-screen-text", "documented", "vendor-documentation")],
    "systems/z-os": [
        curated("ISPF editor", "bundled-optional", ISPF, "full-screen-text", "documented", "vendor-documentation"),
        curated("oedit", "bundled-default", "https://www.ibm.com/docs/en/zos/3.2.0?topic=descriptions-oedit-edit-text", "full-screen-text", "documented", "vendor-documentation"),
    ],
    "systems/mit-lisp-machine-system-software": [
        curated("Zwei", "integral", "https://bitsavers.org/pdf/mit/cadr/chinual_3rdEd_Mar81.pdf", "graphical", "documented", "contemporary-system-manual"),
    ],
    "systems/lmi-lisp-machine-software": [
        curated("ZMACS", "integral", "https://bitsavers.org/pdf/lmi/LMI_LispSW_Overview_Jun82.pdf", "graphical", "documented", "vendor-software-overview"),
    ],
    "systems/genera": [
        curated("Zmacs", "integral", "https://bitsavers.org/pdf/symbolics/software/genera_8/Genera_Workbook.pdf", "graphical", "documented", "official-system-manual"),
    ],
    "systems/interlisp-d-medley": [
        curated("TEdit", "native", "https://xeroxparcarchive.computerhistory.org/Xerox_PARC_source_code.html", "graphical", "documented", "institutional-source-archive"),
    ],
    "systems/small-incompatible-timesharing-system": [
        curated("TINTE", "integral", "https://github.com/pdp11/sits", "full-screen-text", "documented", "preservation-project"),
    ],
    "systems/batch-11-dos-11": [
        curated("EDIT-11", "bundled-default", "https://gunkies.org/wiki/DOS/BATCH", "line-oriented", "documented", "historical-computing-wiki"),
    ],
    "systems/camexec": [
        curated("TECO", "native", "https://gunkies.org/wiki/Camexec", "command-oriented", "documented", "historical-computing-wiki"),
    ],
    "systems/magicsix": [
        curated("SINE", "native", "https://gunkies.org/wiki/MagicSix", "emacs-family", "documented", "historical-computing-wiki"),
    ],
    "systems/nord-tss": [
        curated("QED", "bundled-optional", "https://gunkies.org/wiki/NORD-TSS", "command-oriented", "documented", "historical-computing-wiki"),
    ],
    "systems/stanford-time-sharing-system": [
        curated("TVEDIT", "integral", "https://gunkies.org/wiki/Stanford_Time-Sharing_System", "full-screen-text", "documented", "historical-computing-wiki"),
    ],
}


def merge_associations(*groups: list[dict]) -> list[dict]:
    status_rank = {"documented": 2, "provisional": 1}
    relationship_rank = {
        "integral": 8,
        "bundled-default": 7,
        "first-party": 6,
        "native": 5,
        "bundled-optional": 4,
        "historically-prominent": 3,
        "ported": 2,
        "supported-platform": 1,
    }
    merged: dict[str, dict] = {}
    for group in groups:
        for item in group:
            key = item["name"].casefold()
            candidate_rank = (
                relationship_rank.get(item["relationship"], 0),
                status_rank.get(item["assertion_status"], 0),
            )
            existing_rank = (
                relationship_rank.get(merged.get(key, {}).get("relationship"), 0),
                status_rank.get(merged.get(key, {}).get("assertion_status"), 0),
            )
            if key not in merged or candidate_rank > existing_rank:
                merged[key] = item
    return sorted(merged.values(), key=lambda item: (item["name"].casefold(), item["relationship"]))


def deep_research_associations(system: dict) -> list[dict]:
    deep = system.get("deep_research", {})
    sources = {source["id"]: source for source in deep.get("sources", [])}
    result = []
    for editor in deep.get("editor_associations", []):
        source = next(
            (
                sources[source_id]
                for source_id in editor.get("source_ids", [])
                if source_id in sources
            ),
            {},
        )
        if not source.get("url"):
            continue
        item = {
            "name": editor["name"],
            "relationship": editor["relationship"],
            "interface_style": editor.get("interface_style"),
            "source": source["url"],
            "source_kind": source.get("source_kind", "deep-research-source"),
            "assertion_status": editor["assertion_status"],
        }
        if editor.get("scope"):
            item["scope"] = editor["scope"]
        if editor.get("evidence_note"):
            item["note"] = editor["evidence_note"]
        result.append(item)
    return result


def yaml_block(entry: dict) -> str:
    value = {
        "text_editor_research": {
            "inventory": "/inventory/text-editor-associations.json",
            "checked_at": RUN_DATE,
            "disposition": entry["disposition"],
            "note": entry["note"],
        },
        "text_editors": entry["associations"],
    }
    return yaml.safe_dump(
        value, allow_unicode=True, sort_keys=False, default_flow_style=False
    ).rstrip()


def insert(record: Path, entry: dict) -> None:
    text = record.read_text(encoding="utf-8")
    if BLOCK_START in text:
        start = text.index(BLOCK_START)
        end = text.index(BLOCK_END, start) + len(BLOCK_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")
    if DISPOSITION_START in text:
        start = text.index(DISPOSITION_START)
        end = text.index(DISPOSITION_END, start) + len(DISPOSITION_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")

    disposition = (
        "documented"
        if any(
            item["assertion_status"] == "documented"
            for item in entry["associations"]
        )
        else "provisional"
        if entry["associations"]
        else "no-evidence-found"
    )
    editor_disposition = {
        "field": "text_editors",
        "disposition": disposition,
        "checked_at": RUN_DATE,
    }
    marker = "field_dispositions:\n"
    inline = re.search(r"^field_dispositions:\s*\[.*\]$", text, re.MULTILINE)
    if inline:
        existing = [
            item
            for item in yaml.safe_load(inline.group(0))["field_dispositions"]
            if item.get("field") != "text_editors"
        ]
        flow = yaml.safe_dump(
            [editor_disposition, *existing],
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=True,
            width=100000,
        ).strip()
        text = text[: inline.start()] + f"field_dispositions: {flow}" + text[inline.end() :]
    else:
        if marker not in text:
            raise ValueError(f"{record}: no field_dispositions")
        sequence = re.search(
            r"^field_dispositions:\n(?P<body>(?:[ \t]*#.*\n)*)(?P<indent>[ \t]*)- ",
            text,
            re.MULTILINE,
        )
        indent = sequence.group("indent") if sequence else "  "
        disposition_lines = (
            f"{indent}{DISPOSITION_START}\n"
            f"{indent}- {{ field: text_editors, disposition: {disposition}, "
            f"checked_at: {RUN_DATE} }}\n"
            f"{indent}{DISPOSITION_END}"
        )
        text = text.replace(marker, marker + disposition_lines + "\n", 1)

    closing = text.find("\n---", 4)
    block = f"{BLOCK_START}\n{yaml_block(entry)}\n{BLOCK_END}"
    text = text[:closing].rstrip() + "\n" + block + text[closing:]
    record.write_text(re.sub(r"\n+\Z", "\n", text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-write-records", action="store_true")
    parser.add_argument(
        "--preserve-existing",
        action="store_true",
        help=(
            "Keep existing inventory entries and generated record blocks unchanged; "
            "add coverage only for newly created system records from curated or "
            "deep-research evidence, without querying public APIs."
        ),
    )
    args = parser.parse_args()
    systems = all_systems()
    if args.preserve_existing:
        existing_payload = json.loads(OUTPUT.read_text(encoding="utf-8"))
        existing = {item["path"]: item for item in existing_payload["systems"]}
        output = []
        for path, system in systems.items():
            if path in existing:
                entry = existing[path]
                associations = merge_associations(
                    entry.get("associations", []),
                    CURATED.get(path, []),
                    deep_research_associations(system),
                )
                changed = associations != entry.get("associations", [])
                if changed:
                    entry = entry | {
                        "disposition": (
                            "has-associations"
                            if associations
                            else "no-evidence-found"
                        ),
                        "searched": sorted(
                            set(entry.get("searched", []))
                            | {"curated-primary-sources"}
                        ),
                        "note": (
                            "One or more relationships are documented by curated "
                            "primary, institutional, or preservation sources."
                        ),
                        "associations": associations,
                    }
                output.append(entry)
                if not args.no_write_records and (
                    changed
                    or BLOCK_START
                    not in system["record"].read_text(encoding="utf-8")
                ):
                    insert(system["record"], entry)
                continue
            associations = merge_associations(
                CURATED.get(path, []),
                deep_research_associations(system),
            )
            entry = {
                "path": path,
                "title": system["title"],
                "disposition": (
                    "has-associations" if associations else "no-evidence-found"
                ),
                "searched": ["curated-primary-sources"] if associations else [],
                "note": (
                    "One or more relationships are documented by curated primary "
                    "or institutional sources."
                    if associations
                    else "No editor relationship was established during the "
                    "incremental source-backed record addition."
                ),
                "associations": associations,
            }
            output.append(entry)
            if not args.no_write_records:
                insert(system["record"], entry)
        OUTPUT.write_text(
            json.dumps(
                {
                    "schema_version": existing_payload["schema_version"],
                    "as_of": RUN_DATE,
                    "systems": output,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=False,
            )
            + "\n",
            encoding="utf-8",
        )
        found = sum(bool(entry["associations"]) for entry in output)
        associations = sum(len(entry["associations"]) for entry in output)
        print(
            f"Incremental text-editor coverage: {found}/{len(output)} systems "
            f"have {associations} associations."
        )
        return 0

    mapping = linked_pages()
    linked_paths = set(mapping)
    for path, system in systems.items():
        mapping.setdefault(
            path,
            f"https://en.wikipedia.org/wiki/{quote(system['title'].replace(' ', '_'))}",
        )
    pages = fetch_page_snapshots(mapping)
    page_cache = {
        path: {key: value for key, value in snapshot.items() if key != "extract"}
        | {"associations": page_associations(snapshot)}
        for path, snapshot in pages.items()
    }
    PAGE_CACHE.write_text(
        json.dumps(page_cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    path_qids = system_qids(mapping)
    wd_by_path, wd_raw = wikidata_associations(path_qids)
    WIKIDATA_CACHE.write_text(
        json.dumps(wd_raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    output = []
    for path, system in systems.items():
        page_items = [
            item
            for item in page_cache.get(path, {}).get("associations", [])
            if item["name"].casefold() not in PAGE_EXCLUSIONS.get(path, set())
        ]
        associations = merge_associations(
            CURATED.get(path, []),
            deep_research_associations(system),
            page_items,
            wd_by_path.get(path, []),
        )
        searched = []
        if path in pages:
            searched.append(
                "linked-wikipedia-system-page"
                if path in linked_paths
                else "english-wikipedia-exact-title-query"
            )
        if path in path_qids:
            searched.append("wikidata-text-editor-platform-statements")
        note = (
            "One or more discovery relationships were found; provisional "
            "relationships still require primary-source confirmation."
            if associations
            else "No editor relationship was found in the linked Wikipedia page "
            "or direct Wikidata text-editor platform statements; primary manuals "
            "and distribution manifests still require research."
        )
        entry = {
            "path": path,
            "title": system["title"],
            "disposition": "has-associations" if associations else "no-evidence-found",
            "searched": searched,
            "note": note,
            "associations": associations,
        }
        output.append(entry)
        if not args.no_write_records:
            insert(system["record"], entry)
    OUTPUT.write_text(
        json.dumps(
            {
                "schema_version": "0.1",
                "as_of": RUN_DATE,
                "systems": output,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=False,
        )
        + "\n",
        encoding="utf-8",
    )
    found = sum(bool(entry["associations"]) for entry in output)
    associations = sum(len(entry["associations"]) for entry in output)
    print(
        f"Text-editor discovery: {found}/{len(output)} systems have "
        f"{associations} provisional or documented associations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
