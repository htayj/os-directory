#!/usr/bin/env python3
"""Cache provisional attributes from linked multilingual Wikipedia infoboxes."""

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
INVENTORY = ROOT / "inventory" / "multilingual"
CACHE = INVENTORY / "wikipedia-infobox-snapshots.json"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF multilingual research bundle)"
BLOCK_START = "# BEGIN GENERATED MULTILINGUAL INFOBOX"
BLOCK_END = "# END GENERATED MULTILINGUAL INFOBOX"
SPACE_RE = re.compile(r"\s+")
REFERENCE_RE = re.compile(r"\[\s*\d+(?:\s*[A-Za-z])?\s*\]")

LABELS = {
    # English
    "Developer": "developer", "Developed by": "developer",
    "Written in": "programming_languages", "OS family": "os_family",
    "Working state": "development_status", "Source model": "source_model",
    "Initial release": "first_release", "Latest release": "latest_release",
    "Platforms": "platforms", "Supported platforms": "platforms",
    "Kernel type": "kernel_type", "Default user interface": "gui",
    "User interface": "gui", "License": "license",
    "Marketing target": "purpose", "Country of origin": "country_of_origin",
    # Italian
    "Sviluppatore": "developer", "Famiglia": "os_family",
    "Stato attuale": "development_status", "Modello di sviluppo": "source_model",
    "Prima pubblicazione": "first_release", "Ultima versione": "latest_release",
    "Piattaforme": "platforms", "Tipo di kernel": "kernel_type",
    "Interfaccia utente predefinita": "gui", "Licenza": "license",
    "Scritto in": "programming_languages",
    # Japanese
    "開発者": "developer", "系統": "os_family", "開発状況": "development_status",
    "ソースモデル": "source_model", "初版": "first_release", "最新版": "latest_release",
    "対応プラットフォーム": "platforms", "カーネル種別": "kernel_type",
    "既定のUI": "gui", "ライセンス": "license", "プログラミング言語": "programming_languages",
    # Korean
    "개발자": "developer", "계열": "os_family", "상태": "development_status",
    "소스 형태": "source_model", "최초 버전 출시일": "first_release",
    "최신 버전": "latest_release", "플랫폼": "platforms",
    "커널 형태": "kernel_type", "기본 사용자 인터페이스": "gui",
    "라이선스": "license", "프로그래밍 언어": "programming_languages",
}
FIELDS = (
    "developer", "country_of_origin", "purpose", "programming_languages",
    "first_release", "latest_release", "last_updated", "development_status",
    "source_model", "os_family", "gui", "platforms", "kernel_type", "license",
)


def clean(value: str) -> str:
    return SPACE_RE.sub(" ", REFERENCE_RE.sub("", value)).strip()


def fetch(url: str) -> dict:
    last_error = ""
    for attempt in range(4):
        try:
            response = requests.get(
                url, headers={"User-Agent": USER_AGENT}, timeout=45,
                allow_redirects=True,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                last_error = f"HTTP {response.status_code}"
                time.sleep(2**attempt)
                continue
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            fields: dict[str, str] = {}
            box = soup.select_one("table.infobox")
            if box:
                for row in box.select("tr"):
                    heading, value = row.find("th"), row.find("td")
                    if not heading or not value:
                        continue
                    key = LABELS.get(clean(heading.get_text(" ", strip=True)))
                    if key and key not in fields:
                        fields[key] = clean(value.get_text(" ", strip=True))
            fields["last_updated"] = fields.get("latest_release")
            return {
                "requested_url": url, "resolved_url": response.url,
                "fetch_status": "ok", "fields": fields,
            }
        except requests.RequestException as exc:
            last_error = str(exc)
            time.sleep(2**attempt)
    return {
        "requested_url": url, "resolved_url": None, "fetch_status": "error",
        "error": last_error, "fields": {},
    }


def mappings() -> dict[str, str]:
    candidates = {
        item["candidate_id"]: item
        for item in json.loads(
            (INVENTORY / "candidates-normalized.json").read_text(encoding="utf-8")
        )
    }
    result: dict[str, str] = {}
    for result_path in sorted((INVENTORY / "results").glob("batch-*.json")):
        for item in json.loads(result_path.read_text(encoding="utf-8"))["results"]:
            candidate = candidates[item["candidate_id"]]
            entries = candidate["entries"]
            url = next(
                (entry.get("english_sitelink") for entry in entries
                 if entry.get("english_sitelink")),
                None,
            ) or next(
                (entry.get("native_url") for entry in entries
                 if entry.get("native_url")
                 and "wikipedia.org/" in entry["native_url"]),
                None,
            )
            if url:
                result[item["path"].rstrip("/")] = url
    return result


def insert(record: Path, snapshot: dict, retrieved_at: str) -> None:
    text = record.read_text(encoding="utf-8")
    if BLOCK_START in text:
        start = text.index(BLOCK_START)
        end = text.index(BLOCK_END, start) + len(BLOCK_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")
    value = {
        "multilingual_infobox_snapshot": {
            "source": snapshot.get("resolved_url") or snapshot["requested_url"],
            "retrieved_at": retrieved_at,
            "assertion_status": "provisional",
            "note": (
                "Raw discovery metadata from the linked Wikipedia infobox; "
                "verify against stronger native or primary sources."
            ),
            "fields": {field: snapshot["fields"].get(field) for field in FIELDS},
        }
    }
    block = (
        f"{BLOCK_START}\n"
        f"{yaml.safe_dump(value, allow_unicode=True, sort_keys=False).rstrip()}\n"
        f"{BLOCK_END}"
    )
    closing = text.find("\n---", 4)
    if closing < 0:
        raise ValueError(f"{record}: missing frontmatter")
    record.write_text(
        re.sub(r"\n+\Z", "\n", text[:closing].rstrip() + "\n" + block + text[closing:]),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--retrieved-at", default="2026-07-26")
    args = parser.parse_args()
    mapping = mappings()
    cache: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(fetch, url): url for url in set(mapping.values())}
        for future in as_completed(futures):
            cache[futures[future]] = future.result()
    CACHE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for path, url in mapping.items():
        insert(ROOT / path / "system.md", cache[url], args.retrieved_at)
    populated = sum(bool(item["fields"]) for item in cache.values())
    errors = sum(item["fetch_status"] != "ok" for item in cache.values())
    print(
        f"Enriched {len(mapping)} multilingual records from {len(cache)} linked "
        f"Wikipedia pages; {populated} infoboxes populated, {errors} errors."
    )
    # A disappeared discovery page is preserved as a cache result, not treated as
    # a build failure; the catalog record and its other sources remain valid.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
