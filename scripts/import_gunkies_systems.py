#!/usr/bin/env python3
"""Create identity/core OKF records from curated Gunkies system seeds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "inventory" / "gunkies" / "system-seeds.json"
PAGES = ROOT / "inventory" / "gunkies" / "category-pages.json"
SYSTEMS = ROOT / "systems"
AS_OF = "2026-07-29"


def envelope(value: str, source_id: str) -> dict[str, Any]:
    return {
        "value": value,
        "evidence": [source_id],
        "assertion_status": "provisional",
    }


def record(seed: dict[str, Any], page: dict[str, Any]) -> dict[str, Any]:
    source_id = "gunkies-" + seed["slug"]
    known = set(seed)
    dispositions = []
    for field, seed_field in (
        ("programming_languages", "programming_languages"),
        ("rights_regime", "rights_regime"),
        ("licenses", "licenses"),
        ("kernels", "kernels"),
        ("gui_status", "gui_status"),
        ("first_release", "first_release"),
        ("latest_releases", "latest_release"),
        ("last_updated", "last_updated"),
    ):
        if seed_field not in known:
            dispositions.append(
                {
                    "field": field,
                    "disposition": "no-evidence-found",
                    "checked_at": AS_OF,
                    "reason": "Not established by the reviewed Gunkies page.",
                }
            )

    names = [
        {
            "value": seed["title"],
            "kind": "canonical",
            "language": "en",
            "script": "Latn",
            "evidence": [source_id],
            "assertion_status": "provisional",
        }
    ]
    names.extend(
        {
            "value": alias,
            "kind": "alias",
            "language": "en",
            "script": "Latn",
            "evidence": [source_id],
            "assertion_status": "provisional",
        }
        for alias in seed.get("aliases", [])
    )
    names.extend(
        {
            "value": native,
            "kind": "native-name",
            "evidence": [source_id],
            "assertion_status": "provisional",
        }
        for native in seed.get("native_names", [])
    )

    data: dict[str, Any] = {
        "type": "Operating System",
        "title": seed["title"],
        "description": seed["description"],
        "tags": ["operating-system", "gunkies-discovery", "historical"],
        "status": "draft",
        "generated": {"by": "codex/gpt-5", "at": f"{AS_OF}T00:00:00-04:00"},
        "schema_version": "0.1",
        "as_of": AS_OF,
        "catalog_completeness": {
            "level": "core",
            "note": (
                "Identity and selected core facts are source-reviewed against the "
                "frozen Gunkies revision. Explicit dispositions retain fields not "
                "established by that page."
            ),
        },
        "field_dispositions": dispositions,
        "source_list": {
            "title": "List of operating systems",
            "revision": 1365063001,
            "occurrences": [],
        },
        "discovery_provenance": [
            {
                "method": "gunkies-category-audit",
                "language": "en",
                "source": page["url"],
                "source_revision": page["revision"],
                "observed_at": AS_OF,
                "disposition": "included-system",
            }
        ],
        "names": names,
        "countries_of_origin": seed["countries"],
        "development_status": envelope("discontinued", source_id),
        "design_purposes": [
            envelope(value, source_id) | {"primary": index == 0}
            for index, value in enumerate(seed["purposes"])
        ],
        "hardware_platforms": [
            envelope(value, source_id) for value in seed["platforms"]
        ],
        "sources": [
            {
                "id": source_id,
                "resource": (
                    "https://gunkies.org/w/index.php?title="
                    + page["title"].replace(" ", "_")
                    + f"&oldid={page['revision']}"
                ),
                "title": page["title"],
                "source_kind": "historical-computing-wiki",
                "revision": page["revision"],
                "revision_timestamp": page["revision_timestamp"],
            }
        ],
    }
    if seed.get("organizations"):
        data["organizations"] = [
            {
                "organization": value,
                "roles": ["developer"],
                "evidence": [source_id],
                "assertion_status": "provisional",
            }
            for value in seed["organizations"]
        ]
    for field in (
        "programming_languages",
        "licenses",
        "kernels",
        "system_organization",
    ):
        if seed.get(field):
            data[field] = [envelope(value, source_id) for value in seed[field]]
    if seed.get("rights_regime"):
        data["rights_regime"] = envelope(seed["rights_regime"], source_id)
    if seed.get("gui_status"):
        data["gui_status"] = [envelope(value, source_id) for value in seed["gui_status"]]
    if seed.get("first_release"):
        data["first_release"] = envelope(seed["first_release"], source_id)
    if seed.get("latest_release"):
        data["latest_releases"] = [
            {
                "version": seed["latest_release"],
                "evidence": [source_id],
                "assertion_status": "provisional",
            }
        ]
    if seed.get("last_updated"):
        data["last_updated"] = envelope(seed["last_updated"], source_id)
    if seed.get("lineage"):
        data["lineage_relations"] = [
            {
                "target": value,
                "relation": "related-lineage",
                "evidence": [source_id],
                "assertion_status": "provisional",
            }
            for value in seed["lineage"]
        ]
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Regenerate all curated Gunkies seed records before editor enrichment.",
    )
    args = parser.parse_args()
    seeds = json.loads(SEEDS.read_text(encoding="utf-8"))
    pages = {
        page["title"]: page
        for page in json.loads(PAGES.read_text(encoding="utf-8"))
    }
    created = 0
    skipped = 0
    for seed in seeds:
        page = pages.get(seed["source_page"])
        if page is None:
            raise SystemExit(f"Missing Gunkies snapshot page: {seed['source_page']}")
        directory = SYSTEMS / seed["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        system_path = directory / "system.md"
        if system_path.exists() and not args.refresh:
            skipped += 1
            continue
        payload = yaml.safe_dump(
            record(seed, page),
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )
        system_path.write_text(f"---\n{payload}---\n", encoding="utf-8")
        (directory / "index.md").write_text(
            f"# {seed['title']}\n\n* [System record](system.md)\n",
            encoding="utf-8",
        )
        created += 1
    print(
        f"Created {created} Gunkies-discovered system records; "
        f"preserved {skipped} existing records."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
