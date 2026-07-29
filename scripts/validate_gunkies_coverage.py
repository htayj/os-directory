#!/usr/bin/env python3
"""Validate complete Gunkies category-page and system-record coverage."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "inventory" / "gunkies"
ALLOWED_DISPOSITIONS = {
    "cataloged-system",
    "covered-lineage-or-alias",
    "covered-release",
    "diagnostic-software",
    "grouping-page",
    "hardware-or-site",
    "kernel-not-operating-system",
    "non-system-concept",
    "operating-environment",
    "organization",
    "supporting-document",
    "supporting-software",
}


def main() -> int:
    source = json.loads((DIRECTORY / "category-source.json").read_text())
    pages = json.loads((DIRECTORY / "category-pages.json").read_text())
    coverage = json.loads((DIRECTORY / "coverage.json").read_text())
    seeds = json.loads((DIRECTORY / "system-seeds.json").read_text())
    errors: list[str] = []

    if source["category_count"] != 35:
        errors.append("category-source category_count must be 35")
    if source["page_count"] != len(pages) or len(pages) != 330:
        errors.append("category page count must consistently equal 330")
    if coverage["entry_count"] != len(coverage["entries"]):
        errors.append("coverage entry_count does not match entries")

    page_ids = [page["page_id"] for page in pages]
    page_titles = [page["title"] for page in pages]
    coverage_ids = [entry["page_id"] for entry in coverage["entries"]]
    if len(page_ids) != len(set(page_ids)) or len(page_titles) != len(set(page_titles)):
        errors.append("category page IDs and titles must be unique")
    if set(page_ids) != set(coverage_ids) or len(coverage_ids) != len(set(coverage_ids)):
        errors.append("coverage must contain each frozen page exactly once")

    frozen = {page["page_id"]: page for page in pages}
    for entry in coverage["entries"]:
        label = entry["page_title"]
        page = frozen.get(entry["page_id"])
        if page is None:
            continue
        if entry["revision"] != page["revision"] or label != page["title"]:
            errors.append(f"{label}: coverage/source revision or title mismatch")
        if entry["disposition"] not in ALLOWED_DISPOSITIONS:
            errors.append(f"{label}: invalid disposition {entry['disposition']!r}")
        for record in entry["catalog_records"]:
            if not (ROOT / record / "system.md").is_file():
                errors.append(f"{label}: missing catalog record {record}")

    seed_slugs = [seed["slug"] for seed in seeds]
    seed_pages = [seed["source_page"] for seed in seeds]
    if len(seeds) != 40 or len(seed_slugs) != len(set(seed_slugs)):
        errors.append("system seeds must contain 40 unique slugs")
    if len(seed_pages) != len(set(seed_pages)):
        errors.append("system seed source pages must be unique")
    frozen_by_title = {page["title"]: page for page in pages}
    for seed in seeds:
        page = frozen_by_title.get(seed["source_page"])
        record_path = ROOT / "systems" / seed["slug"] / "system.md"
        if page is None:
            errors.append(f"{seed['slug']}: source page absent from frozen corpus")
            continue
        if not record_path.is_file():
            errors.append(f"{seed['slug']}: generated system record missing")
            continue
        data = yaml.safe_load(record_path.read_text().split("---", 2)[1])
        provenance = data.get("discovery_provenance", [{}])[0]
        if provenance.get("source_revision") != page["revision"]:
            errors.append(f"{seed['slug']}: record provenance revision mismatch")

    if errors:
        raise SystemExit("\n".join(errors))

    counts: dict[str, int] = {}
    for entry in coverage["entries"]:
        counts[entry["disposition"]] = counts.get(entry["disposition"], 0) + 1
    print(
        "Gunkies coverage passed: "
        f"{len(pages)}/{len(pages)} pages resolved across "
        f"{source['category_count']} categories; {len(seeds)} added system records."
    )
    print(
        "System-bearing dispositions: "
        f"cataloged={counts['cataloged-system']}, "
        f"lineage_or_alias={counts['covered-lineage-or-alias']}, "
        f"release={counts['covered-release']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
