#!/usr/bin/env python3
"""Add a reproducible, provisional Wikipedia-infobox snapshot to system records."""

from __future__ import annotations

import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
RESULTS = INVENTORY / "terra-results"
CACHE = INVENTORY / "enwiki-infobox-snapshots.json"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"
BLOCK_START = "# BEGIN GENERATED ENWIKI INFOBOX"
BLOCK_END = "# END GENERATED ENWIKI INFOBOX"
REFERENCE_RE = re.compile(r"\[\s*\d+(?:\s*[A-Za-z])?\s*\]")
SPACE_RE = re.compile(r"\s+")

LABELS = {
    "Developer": "developer",
    "Developed by": "developer",
    "Written in": "programming_languages",
    "OS family": "os_family",
    "Working state": "development_status",
    "Source model": "source_model",
    "Initial release": "first_release",
    "Latest release": "latest_release",
    "Latest preview": "latest_preview",
    "Marketing target": "purpose",
    "Type": "purpose",
    "Platforms": "platforms",
    "Supported platforms": "platforms",
    "Kernel type": "kernel_type",
    "Default user interface": "gui",
    "User interface": "gui",
    "License": "license",
    "Country of origin": "country_of_origin",
}


def clean(value: str) -> str:
    return SPACE_RE.sub(" ", REFERENCE_RE.sub("", value)).strip()


def fetch(url: str) -> dict:
    last_error = ""
    for attempt in range(4):
        try:
            response = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=45,
                allow_redirects=True,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                last_error = f"HTTP {response.status_code}"
                time.sleep(2**attempt)
                continue
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            box = soup.select_one("table.infobox")
            fields: dict[str, str] = {}
            if box:
                for row in box.select("tr"):
                    heading = row.find("th")
                    value = row.find("td")
                    if not heading or not value:
                        continue
                    label = clean(heading.get_text(" ", strip=True))
                    key = LABELS.get(label)
                    if not key or key in fields:
                        continue
                    fields[key] = clean(value.get_text(" ", strip=True))
            fields["last_updated"] = fields.get("latest_release")
            return {
                "requested_url": url,
                "resolved_url": response.url,
                "page_title": clean(soup.title.get_text(" ", strip=True))
                if soup.title
                else None,
                "fields": fields,
                "fetch_status": "ok",
            }
        except requests.RequestException as exc:
            last_error = str(exc)
            time.sleep(2**attempt)
    return {
        "requested_url": url,
        "resolved_url": None,
        "page_title": None,
        "fields": {},
        "fetch_status": "error",
        "error": last_error,
    }


def system_urls() -> dict[str, str]:
    candidates = {
        item["candidate_id"]: item
        for item in json.loads(
            (INVENTORY / "terra-candidates.json").read_text(encoding="utf-8")
        )
    }
    mapping: dict[str, str] = {}
    for result_path in sorted(RESULTS.glob("batch-*.json")):
        result = json.loads(result_path.read_text(encoding="utf-8"))
        for item in result["results"]:
            if item.get("disposition") != "included-system" or not item.get("path"):
                continue
            candidate = candidates[item["candidate_id"]]
            url = candidate.get("canonical_url")
            if url:
                mapping.setdefault(item["path"].rstrip("/"), url)
    return mapping


def yaml_block(snapshot: dict, retrieved_at: str) -> str:
    fields = {
        key: snapshot["fields"].get(key)
        for key in (
            "developer",
            "country_of_origin",
            "purpose",
            "programming_languages",
            "first_release",
            "latest_release",
            "last_updated",
            "development_status",
            "source_model",
            "os_family",
            "gui",
            "platforms",
            "kernel_type",
            "license",
        )
    }
    value = {
        "source": snapshot.get("resolved_url") or snapshot["requested_url"],
        "retrieved_at": retrieved_at,
        "assertion_status": "provisional",
        "note": (
            "Raw discovery metadata from the linked English Wikipedia infobox; "
            "normalize and verify against stronger sources before marking verified."
        ),
        "fields": fields,
    }
    if snapshot.get("country_evidence"):
        value["country_evidence"] = snapshot["country_evidence"]
    dumped = yaml.safe_dump(
        {"first_pass_attributes": value},
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()
    return f"{BLOCK_START}\n{dumped}\n{BLOCK_END}"


def insert_block(record: Path, block: str) -> None:
    text = record.read_text(encoding="utf-8")
    if BLOCK_START in text:
        start = text.index(BLOCK_START)
        end = text.index(BLOCK_END, start) + len(BLOCK_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")
    closing = text.find("\n---", 4)
    if not text.startswith("---\n") or closing < 0:
        raise ValueError(f"{record}: missing frontmatter delimiters")
    text = text[:closing].rstrip() + "\n" + block + text[closing:]
    record.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--retrieved-at", default="2026-07-26")
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    mapping = system_urls()
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    urls = sorted(set(mapping.values()))
    pending = (
        urls
        if args.refresh
        else [
            url
            for url in urls
            if url not in cache or cache[url].get("fetch_status") != "ok"
        ]
    )

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(fetch, url): url for url in pending}
        for number, future in enumerate(as_completed(futures), 1):
            url = futures[future]
            cache[url] = future.result()
            if number % 25 == 0 or number == len(pending):
                print(f"Fetched {number}/{len(pending)} pending pages.")

    CACHE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    enriched = 0
    errors = 0
    for system_path, url in mapping.items():
        snapshot = cache[url]
        if snapshot.get("fetch_status") != "ok":
            errors += 1
        insert_block(
            ROOT / system_path / "system.md",
            yaml_block(snapshot, args.retrieved_at),
        )
        enriched += 1
    print(
        f"Enriched {enriched} system records from {len(urls)} pages; "
        f"{errors} fetch errors."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
