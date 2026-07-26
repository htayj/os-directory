#!/usr/bin/env python3
"""Normalize multilingual discovery files and build Terra catalog manifests."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
MULTILINGUAL = INVENTORY / "multilingual"
MANIFESTS = MULTILINGUAL / "manifests"
BATCH_SIZE = 8

DISPOSITIONS = {
    "included-system": "included-system",
    "supplemental-system": "included-system",
    "alias": "alias",
    "already-covered": "alias",
    "already-in-frozen-inventory": "alias",
    "included-release": "included-release",
    "release": "included-release",
    "grouping": "grouping",
    "non-OS": "not-an-operating-system",
    "non-os": "not-an-operating-system",
    "needs-review": "needs-review",
}

# Native-language evidence can resolve an ambiguity left by the frozen English
# list. These are reviewed identity corrections, not string-match exceptions.
OVERRIDES = {
    "bs1000-siemens": ("included-system", None),
    "rodos": ("included-system", None),
    "fuguita-fr-listing": ("included-system", None),
    "bs3000-siemens": ("included-release", "systems/msp"),
    "tron-project": ("grouping", None),
}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def article_key(url: str) -> str:
    parsed = urlsplit(url)
    return unquote(parsed.path).split("#", 1)[0].rstrip("/").casefold()


def existing_identity_maps() -> tuple[dict[str, str], dict[str, str]]:
    urls: dict[str, str] = {}
    names: dict[str, str] = {}
    for record in sorted((ROOT / "systems").glob("*/system.md")):
        path = str(record.parent.relative_to(ROOT))
        data = yaml.safe_load(record.read_text(encoding="utf-8").split("---", 2)[1])
        for value in [data.get("title")]:
            if value and (normalized := norm(str(value))):
                names.setdefault(normalized, path)
        for item in data.get("names", []) or []:
            if isinstance(item, dict) and item.get("value"):
                normalized = norm(str(item["value"]))
                if normalized:
                    names.setdefault(normalized, path)
        first_pass = data.get("first_pass_attributes", {})
        if first_pass.get("source"):
            urls.setdefault(article_key(first_pass["source"]), path)
        for item in data.get("same_as", []) or []:
            if isinstance(item, str) and item.startswith("http"):
                urls.setdefault(article_key(item), path)
        for item in data.get("sources", []) or []:
            if isinstance(item, dict):
                resource = item.get("resource")
                if isinstance(resource, str) and "wikipedia.org/wiki/" in resource:
                    urls.setdefault(article_key(resource), path)
    return urls, names


def identity_key(candidate: dict) -> str:
    qid = candidate.get("wikidata_qid")
    if qid:
        return f"qid:{qid}"
    english = candidate.get("english_sitelink")
    if english:
        return f"en:{article_key(english)}"
    return f"id:{candidate['candidate_id']}"


def candidate_url(candidate: dict) -> str | None:
    return candidate.get("native_url") or candidate.get("url")


def main() -> int:
    existing_urls, existing_names = existing_identity_maps()
    grouped: dict[str, list[dict]] = defaultdict(list)

    for path in sorted(MULTILINGUAL.glob("*-candidates.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        language = document["language"]
        sources = document.get("sources") or document.get("source_pages") or []
        for candidate in document["candidates"]:
            item = {
                **candidate,
                "language": language,
                "manifest": str(path.relative_to(ROOT)),
                "source_document": sources,
                "normalized_disposition": DISPOSITIONS[candidate["disposition"]],
            }
            grouped[identity_key(item)].append(item)

    normalized: list[dict] = []
    for key, language_entries in grouped.items():
        first = language_entries[0]
        dispositions = {
            item["normalized_disposition"] for item in language_entries
        }
        disposition = (
            "included-system"
            if "included-system" in dispositions
            else sorted(dispositions)[0]
        )

        existing_path = None
        for item in language_entries:
            english = item.get("english_sitelink")
            if english:
                existing_path = existing_urls.get(article_key(english))
            if not existing_path:
                candidate_id_path = ROOT / "systems" / item["candidate_id"]
                if candidate_id_path.exists():
                    existing_path = str(candidate_id_path.relative_to(ROOT))
            if not existing_path:
                values = [
                    item.get("native_label"),
                    *(item.get("native_aliases") or []),
                ]
                for value in values:
                    normalized_name = norm(value) if value else ""
                    if normalized_name and normalized_name in existing_names:
                        existing_path = existing_names[normalized_name]
                        break
            if existing_path:
                break

        if disposition == "included-system" and existing_path:
            disposition = "alias"
        if first["candidate_id"] in OVERRIDES:
            disposition, existing_path = OVERRIDES[first["candidate_id"]]

        normalized.append(
            {
                "identity_key": key,
                "candidate_id": first["candidate_id"],
                "title": first.get("native_label") or first["candidate_id"],
                "disposition": disposition,
                "existing_path": existing_path,
                "languages": sorted({item["language"] for item in language_entries}),
                "entries": language_entries,
            }
        )

    normalized.sort(
        key=lambda item: (
            item["disposition"] != "included-system",
            item["languages"],
            item["candidate_id"],
        )
    )
    (MULTILINGUAL / "candidates-normalized.json").write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    included = [item for item in normalized if item["disposition"] == "included-system"]
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    for old in MANIFESTS.glob("batch-*.json"):
        old.unlink()
    ledger = []
    for offset in range(0, len(included), BATCH_SIZE):
        number = offset // BATCH_SIZE + 1
        filename = f"batch-{number:03d}.json"
        batch = {
            "schema_version": "0.1",
            "batch": number,
            "candidate_count": len(included[offset : offset + BATCH_SIZE]),
            "candidates": included[offset : offset + BATCH_SIZE],
        }
        (MANIFESTS / filename).write_text(
            json.dumps(batch, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        ledger.append(
            {
                "batch": number,
                "manifest": f"inventory/multilingual/manifests/{filename}",
                "candidate_count": batch["candidate_count"],
                "status": "pending",
            }
        )
    (MULTILINGUAL / "batches.json").write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    counts: dict[str, int] = defaultdict(int)
    for item in normalized:
        counts[item["disposition"]] += 1
    print(
        f"Normalized {sum(len(v) for v in grouped.values())} language entries "
        f"into {len(normalized)} identities; {len(included)} new systems in "
        f"{len(ledger)} batches."
    )
    for disposition, count in sorted(counts.items()):
        print(f"{disposition}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
