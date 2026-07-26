#!/usr/bin/env python3
"""Add provisional Wikidata attribute evidence to multilingual system records."""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory" / "multilingual"
CANDIDATES = INVENTORY / "candidates-normalized.json"
RESULTS = INVENTORY / "results"
CACHE = INVENTORY / "wikidata-attribute-snapshots.json"
API = "https://www.wikidata.org/w/api.php"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF multilingual research bundle)"
BLOCK_START = "# BEGIN GENERATED MULTILINGUAL WIKIDATA"
BLOCK_END = "# END GENERATED MULTILINGUAL WIKIDATA"

ITEM_PROPERTIES = {
    "developer": "P178",
    "country_of_origin": "P495",
    "purpose": "P366",
    "programming_languages": "P277",
    "platforms": "P400",
    "license": "P275",
}


def chunks(values: list[str], size: int = 50):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def api(params: dict) -> dict:
    last_error = ""
    for attempt in range(5):
        response = requests.post(
            API,
            data={"format": "json", "formatversion": "2", **params},
            headers={"User-Agent": USER_AGENT},
            timeout=60,
        )
        if response.status_code in {429, 500, 502, 503, 504}:
            last_error = f"HTTP {response.status_code}"
            time.sleep(max(2**attempt, 20 if response.status_code == 429 else 0))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError(f"Wikidata request failed: {last_error}")


def wiki_site_and_title(url: str) -> tuple[str, str] | None:
    parsed = urlsplit(url)
    if not parsed.hostname or not parsed.hostname.endswith(".wikipedia.org"):
        return None
    language = parsed.hostname.removesuffix(".wikipedia.org")
    path = unquote(parsed.path)
    if not path.startswith("/wiki/"):
        return None
    title = path.removeprefix("/wiki/").split("#", 1)[0].replace("_", " ")
    return f"{language}wiki", title


def item_ids(entity: dict, prop: str) -> list[str]:
    values: list[str] = []
    for claim in entity.get("claims", {}).get(prop, []):
        value = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if isinstance(value, dict) and value.get("entity-type") == "item":
            values.append(value["id"])
    return list(dict.fromkeys(values))


def time_values(entity: dict, prop: str) -> list[str]:
    values: list[str] = []
    for claim in entity.get("claims", {}).get(prop, []):
        value = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if not isinstance(value, dict) or not value.get("time"):
            continue
        raw = value["time"].lstrip("+")
        precision = int(value.get("precision", 11))
        if precision >= 11:
            values.append(raw[:10])
        elif precision == 10:
            values.append(raw[:7])
        else:
            values.append(raw[:4])
    return list(dict.fromkeys(values))


def string_values(entity: dict, prop: str) -> list[str]:
    values: list[str] = []
    for claim in entity.get("claims", {}).get(prop, []):
        value = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if isinstance(value, str):
            values.append(value)
    return list(dict.fromkeys(values))


def qualifier_time_values(entity: dict, prop: str, qualifier: str) -> list[str]:
    values: list[str] = []
    for claim in entity.get("claims", {}).get(prop, []):
        for snak in claim.get("qualifiers", {}).get(qualifier, []):
            value = snak.get("datavalue", {}).get("value")
            if not isinstance(value, dict) or not value.get("time"):
                continue
            raw = value["time"].lstrip("+")
            precision = int(value.get("precision", 11))
            values.append(
                raw[:10] if precision >= 11 else raw[:7] if precision == 10 else raw[:4]
            )
    return list(dict.fromkeys(values))


def label(entity: dict) -> str:
    labels = entity.get("labels", {})
    for language in ("en", "mul"):
        if labels.get(language, {}).get("value"):
            return labels[language]["value"]
    for value in labels.values():
        if value.get("value"):
            return value["value"]
    return entity.get("id", "unknown")


def candidate_map() -> dict[str, dict]:
    return {
        candidate["candidate_id"]: candidate
        for candidate in json.loads(CANDIDATES.read_text(encoding="utf-8"))
        if candidate.get("disposition") == "included-system"
    }


def record_map() -> dict[str, dict]:
    candidates = candidate_map()
    mapping: dict[str, dict] = {}
    for result_path in sorted(RESULTS.glob("batch-*.json")):
        result = json.loads(result_path.read_text(encoding="utf-8"))
        for item in result["results"]:
            candidate = candidates.get(item["candidate_id"])
            if item.get("disposition") == "included-system" and candidate:
                mapping[item["path"].rstrip("/")] = candidate
    return mapping


def resolve_entities(records: dict[str, dict]) -> dict[str, dict]:
    resolved: dict[str, dict] = {}
    unresolved: dict[tuple[str, str], list[str]] = {}
    qids: dict[str, list[str]] = {}
    for path, candidate in records.items():
        qid = next(
            (
                entry.get("wikidata_qid")
                for entry in candidate["entries"]
                if entry.get("wikidata_qid")
            ),
            None,
        )
        if qid:
            qids.setdefault(qid, []).append(path)
            continue
        urls: list[str] = []
        for entry in candidate["entries"]:
            urls.extend(
                url
                for url in (entry.get("native_url"), entry.get("english_sitelink"))
                if url
            )
        wiki = next((wiki_site_and_title(url) for url in urls if wiki_site_and_title(url)), None)
        if wiki:
            unresolved.setdefault(wiki, []).append(path)

    for batch in chunks(sorted(qids)):
        data = api(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "claims|labels|sitelinks",
                "languages": "en|mul",
                "languagefallback": 1,
            }
        )
        for qid, entity in data.get("entities", {}).items():
            for path in qids.get(qid, []):
                resolved[path] = entity

    by_site: dict[str, dict[str, list[str]]] = {}
    for (site, title), paths in unresolved.items():
        by_site.setdefault(site, {})[title] = paths
    for site, titles in sorted(by_site.items()):
        for batch in chunks(sorted(titles)):
            data = api(
                {
                    "action": "wbgetentities",
                    "sites": site,
                    "titles": "|".join(batch),
                    "props": "claims|labels|sitelinks",
                    "languages": "en|mul",
                    "languagefallback": 1,
                }
            )
            for entity in data.get("entities", {}).values():
                sitelink = entity.get("sitelinks", {}).get(site, {}).get("title")
                if sitelink:
                    for path in titles.get(sitelink, []):
                        resolved[path] = entity
    return resolved


def build_snapshots(records: dict[str, dict], entities: dict[str, dict]) -> dict[str, dict]:
    related_ids = {
        qid
        for entity in entities.values()
        for prop in ITEM_PROPERTIES.values()
        for qid in item_ids(entity, prop)
    }
    related: dict[str, dict] = {}
    for batch in chunks(sorted(related_ids)):
        data = api(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels",
                "languages": "en|mul",
                "languagefallback": 1,
            }
        )
        related.update(data.get("entities", {}))

    snapshots: dict[str, dict] = {}
    for path, candidate in records.items():
        entity = entities.get(path)
        fields: dict[str, object] = {}
        if entity:
            for field, prop in ITEM_PROPERTIES.items():
                values = [
                    label(related[qid])
                    for qid in item_ids(entity, prop)
                    if qid in related
                ]
                fields[field] = values or None
            first_release = time_values(entity, "P571")
            versions = string_values(entity, "P348")
            version_dates = qualifier_time_values(entity, "P348", "P577")
            fields["first_release"] = first_release or None
            fields["latest_release"] = versions or None
            fields["last_updated"] = max(version_dates) if version_dates else None
        snapshots[path] = {
            "candidate_id": candidate["candidate_id"],
            "wikidata_entity": entity.get("id") if entity else None,
            "source": (
                f"https://www.wikidata.org/wiki/{entity['id']}" if entity else None
            ),
            "assertion_status": "provisional" if entity else "unknown",
            "note": (
                "Discovery metadata from Wikidata statements. It is not independently "
                "verified and does not replace native or primary-source research."
            ),
            "fields": fields,
        }
    return snapshots


def insert_block(record: Path, snapshot: dict, retrieved_at: str) -> None:
    text = record.read_text(encoding="utf-8")
    if BLOCK_START in text:
        start = text.index(BLOCK_START)
        end = text.index(BLOCK_END, start) + len(BLOCK_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")
    value = {
        "multilingual_wikidata_snapshot": {
            **snapshot,
            "retrieved_at": retrieved_at,
        }
    }
    dumped = yaml.safe_dump(
        value, allow_unicode=True, sort_keys=False, default_flow_style=False
    ).rstrip()
    block = f"{BLOCK_START}\n{dumped}\n{BLOCK_END}"
    closing = text.find("\n---", 4)
    if not text.startswith("---\n") or closing < 0:
        raise ValueError(f"{record}: missing frontmatter delimiters")
    text = text[:closing].rstrip() + "\n" + block + text[closing:]
    record.write_text(re.sub(r"\n+\Z", "\n", text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrieved-at", default="2026-07-26")
    args = parser.parse_args()
    records = record_map()
    entities = resolve_entities(records)
    snapshots = build_snapshots(records, entities)
    CACHE.write_text(
        json.dumps(snapshots, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for path, snapshot in snapshots.items():
        insert_block(ROOT / path / "system.md", snapshot, args.retrieved_at)
    populated = sum(bool(item["wikidata_entity"]) for item in snapshots.values())
    print(
        f"Added provisional Wikidata snapshots to {len(snapshots)} multilingual "
        f"records; {populated} entities resolved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
