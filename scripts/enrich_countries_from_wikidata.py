#!/usr/bin/env python3
"""Populate provisional country-of-origin values from Wikidata P495 claims."""

from __future__ import annotations

import json
import time
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
INFOBOX_CACHE = INVENTORY / "enwiki-infobox-snapshots.json"
COUNTRY_CACHE = INVENTORY / "wikidata-country-origins.json"
API = "https://www.wikidata.org/w/api.php"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"


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
            delay = 2**attempt
            if response.status_code == 429:
                delay = max(delay, 30)
            time.sleep(delay)
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError(f"Wikidata request failed: {last_error}")


def page_title(url: str) -> str | None:
    path = unquote(urlsplit(url).path)
    if not path.startswith("/wiki/"):
        return None
    return path.removeprefix("/wiki/").split("#", 1)[0].replace("_", " ")


def qids(entity: dict, prop: str) -> list[str]:
    values = []
    for claim in entity.get("claims", {}).get(prop, []):
        value = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if isinstance(value, dict) and value.get("entity-type") == "item":
            values.append(value["id"])
    return values


def main() -> int:
    snapshots = json.loads(INFOBOX_CACHE.read_text(encoding="utf-8"))
    titles = sorted(
        {title for url in snapshots if (title := page_title(url)) is not None}
    )
    title_entities: dict[str, dict] = {}
    for number, batch in enumerate(chunks(titles), 1):
        data = api(
            {
                "action": "wbgetentities",
                "sites": "enwiki",
                "titles": "|".join(batch),
                "props": "claims|labels|sitelinks",
                "languages": "en",
                "languagefallback": 1,
            }
        )
        for entity in data.get("entities", {}).values():
            title = (
                entity.get("sitelinks", {}).get("enwiki", {}).get("title")
            )
            if title:
                title_entities[title] = entity
        print(f"Resolved title batch {number}.")

    developer_qids = {
        qid
        for entity in title_entities.values()
        for qid in qids(entity, "P178")
    }
    developer_entities: dict[str, dict] = {}
    for batch in chunks(sorted(developer_qids)):
        data = api(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "claims|labels",
                "languages": "en",
                "languagefallback": 1,
            }
        )
        developer_entities.update(data.get("entities", {}))

    headquarters_qids = {
        qid
        for entity in developer_entities.values()
        for qid in qids(entity, "P159")
    }
    headquarters_entities: dict[str, dict] = {}
    for batch in chunks(sorted(headquarters_qids)):
        data = api(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "claims|labels",
                "languages": "en",
                "languagefallback": 1,
            }
        )
        headquarters_entities.update(data.get("entities", {}))

    country_qids = {
        qid
        for entity in title_entities.values()
        for qid in qids(entity, "P495")
    }
    country_qids.update(
        qid
        for entity in developer_entities.values()
        for qid in qids(entity, "P17")
    )
    country_qids.update(
        qid
        for entity in headquarters_entities.values()
        for qid in qids(entity, "P17")
    )
    country_entities: dict[str, dict] = {}
    for batch in chunks(sorted(country_qids), 50):
        data = api(
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels",
                "languages": "en",
                "languagefallback": 1,
            }
        )
        country_entities.update(data.get("entities", {}))

    results: dict[str, dict] = {}
    for url, snapshot in snapshots.items():
        requested = page_title(url)
        resolved = page_title(snapshot.get("resolved_url") or url)
        entity = title_entities.get(resolved or "") or title_entities.get(requested or "")
        values = qids(entity, "P495") if entity else []
        evidence_qid = entity.get("id") if entity else None
        method = "wikidata-country-of-origin"
        assertion_status = "provisional"
        if not values and entity:
            for developer_qid in qids(entity, "P178"):
                developer = developer_entities.get(developer_qid, {})
                developer_countries = qids(developer, "P17")
                if developer_countries:
                    values.extend(developer_countries)
                    evidence_qid = developer_qid
                    method = "inferred-from-developer-country"
                    assertion_status = "inferred"
                    continue
                for headquarters_qid in qids(developer, "P159"):
                    headquarters = headquarters_entities.get(headquarters_qid, {})
                    headquarters_countries = qids(headquarters, "P17")
                    if headquarters_countries:
                        values.extend(headquarters_countries)
                        evidence_qid = headquarters_qid
                        method = "inferred-from-developer-headquarters"
                        assertion_status = "inferred"
        values = list(dict.fromkeys(values))
        countries = [
            country_entities.get(qid, {}).get("labels", {}).get("en", {}).get("value")
            for qid in values
        ]
        countries = [country for country in countries if country]
        record = {
            "wikidata_entity": entity.get("id") if entity else None,
            "countries": countries,
            "property": "P495",
            "method": method if countries else "no-country-evidence",
            "assertion_status": assertion_status if countries else "unknown",
        }
        results[url] = record
        if countries:
            snapshot["fields"]["country_of_origin"] = "; ".join(countries)
            snapshot["country_evidence"] = {
                "source": f"https://www.wikidata.org/wiki/{evidence_qid}",
                "method": method,
                "assertion_status": assertion_status,
            }

    COUNTRY_CACHE.write_text(
        json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    INFOBOX_CACHE.write_text(
        json.dumps(snapshots, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    found = sum(bool(item["countries"]) for item in results.values())
    print(f"Wikidata P495 country values found for {found}/{len(results)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
