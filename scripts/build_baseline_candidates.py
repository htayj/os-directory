#!/usr/bin/env python3
"""Normalize the frozen English-list occurrences into catalog candidates."""

from __future__ import annotations

import json
import re
import time
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
ENWIKI_API = "https://en.wikipedia.org/w/api.php"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"
OS_ROOT_QID = "Q9135"
OS_RE = re.compile(
    r"\b(?:operating system|operating environment|linux distribution|"
    r"unix-like system|real-time operating system|rtos)\b",
    re.IGNORECASE,
)
UNNAMED_RE = re.compile(r"^(?:unnamed|operating system for)\b", re.IGNORECASE)
RELEASE_RE = re.compile(
    r"(?:\bversions?\b|\breleases?\b|\bv\d+(?:\.\d+)*\b|"
    r"\b\d+\.\d+(?:[-–]\d+(?:\.\d+)*)?\b)",
    re.IGNORECASE,
)
BREAK_RE = re.compile(r"\s+(?:–|—|-)\s+")
SPACE_RE = re.compile(r"\s+")


def api_get(url: str, params: dict) -> dict:
    last_error = ""
    for attempt in range(5):
        response = requests.post(
            url,
            data={"format": "json", "formatversion": "2", **params},
            headers={"User-Agent": USER_AGENT},
            timeout=90,
        )
        if response.status_code in {429, 500, 502, 503, 504}:
            last_error = f"HTTP {response.status_code}: {response.text[:300]}"
            retry_after = response.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else 2**attempt
            if response.status_code == 429:
                delay = max(delay, 30)
            time.sleep(delay)
            continue
        if not response.ok:
            last_error = f"HTTP {response.status_code}: {response.text[:300]}"
            response.raise_for_status()
        return response.json()
    raise RuntimeError(f"API request failed after retries: {url}: {last_error}")


def chunks(values: list[str], size: int = 50):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def article_title(url: str) -> str | None:
    path = unquote(urlsplit(url).path)
    if not path.startswith("/wiki/"):
        return None
    title = path.removeprefix("/wiki/").split("#", 1)[0].replace("_", " ")
    return title or None


def resolve_mapping(query: dict, requested: list[str]) -> dict[str, str]:
    mapping = {title: title for title in requested}
    for item in query.get("normalized", []):
        mapping[item["from"]] = item["to"]
    for item in query.get("redirects", []):
        source = item["from"]
        target = item["to"]
        for original, current in list(mapping.items()):
            if current == source:
                mapping[original] = target
        mapping[source] = target
    return mapping


def fetch_enwiki(titles: list[str]) -> tuple[dict[str, dict], dict[str, str]]:
    pages: dict[str, dict] = {}
    aliases: dict[str, str] = {}
    for batch in chunks(titles, 20):
        data = api_get(
            ENWIKI_API,
            {
                "action": "query",
                "titles": "|".join(batch),
                "redirects": 1,
                "prop": "pageprops|extracts|info",
                "exintro": 1,
                "explaintext": 1,
                "exsentences": 3,
                "inprop": "url",
            },
        )
        query = data["query"]
        aliases.update(resolve_mapping(query, batch))
        for page in query["pages"]:
            if page.get("missing"):
                continue
            pages[page["title"]] = {
                "title": page["title"],
                "pageid": page["pageid"],
                "url": page.get("fullurl"),
                "wikidata": page.get("pageprops", {}).get("wikibase_item"),
                "description": SPACE_RE.sub(" ", page.get("extract", "")).strip(),
            }
        time.sleep(0.5)
    return pages, aliases


def fetch_entities(qids: set[str], props: str = "claims|labels|aliases") -> dict[str, dict]:
    entities: dict[str, dict] = {}
    pending = sorted(qids)
    for batch in chunks(pending):
        data = api_get(
            WIKIDATA_API,
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": props,
                "languages": "en",
                "languagefallback": 1,
            },
        )
        entities.update(data.get("entities", {}))
        time.sleep(0.5)
    return entities


def claim_qids(entity: dict, prop: str) -> list[str]:
    values = []
    for claim in entity.get("claims", {}).get(prop, []):
        value = (
            claim.get("mainsnak", {})
            .get("datavalue", {})
            .get("value")
        )
        if isinstance(value, dict) and value.get("entity-type") == "item":
            values.append(value["id"])
    return values


def class_graph(entities: dict[str, dict]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    pending = {
        qid
        for entity in entities.values()
        for qid in claim_qids(entity, "P31")
    }
    class_entities: dict[str, dict] = {}
    while pending:
        batch_entities = fetch_entities(pending)
        class_entities.update(batch_entities)
        new_pending: set[str] = set()
        for qid, entity in batch_entities.items():
            parents = set(claim_qids(entity, "P279"))
            graph[qid] = parents
            new_pending.update(parents - class_entities.keys())
        pending = new_pending
    entities.update(class_entities)
    return graph


def has_ancestor(qid: str, target: str, graph: dict[str, set[str]]) -> bool:
    seen: set[str] = set()
    pending = [qid]
    while pending:
        current = pending.pop()
        if current == target:
            return True
        if current in seen:
            continue
        seen.add(current)
        pending.extend(graph.get(current, ()))
    return False


def is_os_page(page: dict, entities: dict[str, dict], graph: dict[str, set[str]]) -> bool:
    qid = page.get("wikidata")
    if qid and qid in entities:
        if any(has_ancestor(kind, OS_ROOT_QID, graph) for kind in claim_qids(entities[qid], "P31")):
            return True
    return bool(OS_RE.search(page.get("description", "")))


def subject_from_label(label: str) -> str:
    subject = BREAK_RE.split(label, maxsplit=1)[0].strip()
    subject = re.sub(r"\s+\[\d+\]\s*$", "", subject)
    return subject.rstrip(" .,:;")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    return slug or "unnamed-system"


def unique_slug(base: str, used: set[str]) -> str:
    if base not in used:
        used.add(base)
        return base
    counter = 2
    while f"{base}-{counter}" in used:
        counter += 1
    value = f"{base}-{counter}"
    used.add(value)
    return value


def main() -> int:
    occurrences = json.loads(
        (INVENTORY / "english-list-occurrences.json").read_text(encoding="utf-8")
    )
    titles = sorted(
        {
            title
            for occurrence in occurrences
            for link in occurrence["links"]
            if link["article"] and (title := article_title(link["target"]))
        }
    )
    pages, aliases = fetch_enwiki(titles)
    qids = {page["wikidata"] for page in pages.values() if page.get("wikidata")}
    entities = fetch_entities(qids)
    graph = class_graph(entities)

    page_is_os = {
        title: is_os_page(page, entities, graph)
        for title, page in pages.items()
    }
    child_positions = {
        occurrence["parent_position"]
        for occurrence in occurrences
        if occurrence["parent_position"] is not None
    }

    raw: list[dict] = []
    for occurrence in occurrences:
        article_links = []
        for link in occurrence["links"]:
            requested = article_title(link["target"]) if link["article"] else None
            if not requested:
                continue
            canonical = aliases.get(requested, requested)
            page = pages.get(canonical)
            if page:
                article_links.append((link, page))

        explicit_unnamed = bool(UNNAMED_RE.match(occurrence["label"]))
        os_links = [
            (link, page)
            for link, page in article_links
            if page_is_os.get(page["title"], False)
        ]
        chosen = None if explicit_unnamed else (os_links[0] if os_links else None)
        has_children = occurrence["position"] in child_positions

        if chosen:
            link, page = chosen
            title = link["label"] or page["title"]
            key = f"qid:{page['wikidata']}" if page.get("wikidata") else f"page:{page['title']}"
            disposition = "included-system"
            canonical_page = page["title"]
            wikidata = page.get("wikidata")
            description = page.get("description", "")
        elif not has_children or OS_RE.search(occurrence["label"]):
            title = subject_from_label(occurrence["label"])
            parent = occurrence.get("parent_position")
            is_release = bool(parent and RELEASE_RE.search(title))
            key = f"release:{title.casefold()}:{parent}" if is_release else f"label:{title.casefold()}"
            disposition = "included-release" if is_release else "included-system"
            canonical_page = None
            wikidata = None
            description = ""
        else:
            title = subject_from_label(occurrence["label"])
            key = f"group:{occurrence['position']}"
            disposition = "grouping"
            canonical_page = None
            wikidata = None
            description = ""

        raw.append(
            {
                "key": key,
                "title": title,
                "disposition": disposition,
                "canonical_page": canonical_page,
                "wikidata": wikidata,
                "description": description,
                "occurrence": {
                    "position": occurrence["position"],
                    "section": occurrence["section"],
                    "depth": occurrence["depth"],
                    "parent_position": occurrence["parent_position"],
                    "label": occurrence["label"],
                },
            }
        )

    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in raw:
        grouped[item["key"]].append(item)

    used_slugs: set[str] = set()
    candidates: list[dict] = []
    occurrence_map: list[dict] = []
    for key, items in grouped.items():
        first = items[0]
        slug = unique_slug(slugify(first["title"]), used_slugs)
        candidate = {
            "candidate_id": slug,
            "title": first["title"],
            "disposition": first["disposition"],
            "canonical_page": first["canonical_page"],
            "wikidata": first["wikidata"],
            "description": first["description"],
            "occurrences": [item["occurrence"] for item in items],
        }
        candidates.append(candidate)
        for item in items:
            occurrence_map.append(
                {
                    "position": item["occurrence"]["position"],
                    "candidate_id": slug,
                    "disposition": first["disposition"],
                }
            )

    candidates.sort(key=lambda item: item["occurrences"][0]["position"])
    occurrence_map.sort(key=lambda item: item["position"])
    metadata = {
        title: page
        for title, page in sorted(pages.items())
        if page_is_os.get(title, False)
    }
    (INVENTORY / "enwiki-os-page-metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (INVENTORY / "baseline-candidates.json").write_text(
        json.dumps(candidates, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (INVENTORY / "baseline-occurrence-map.json").write_text(
        json.dumps(occurrence_map, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    counts = defaultdict(int)
    for candidate in candidates:
        counts[candidate["disposition"]] += 1
    print(f"Resolved {len(occurrences)} occurrences into {len(candidates)} candidates.")
    for disposition, count in sorted(counts.items()):
        print(f"{disposition}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
