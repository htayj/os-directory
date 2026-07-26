#!/usr/bin/env python3
"""Group provisional GUI/interface source terms across system records."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = ROOT / "systems"
OUTPUT = ROOT / "inventory" / "interface-environment-candidates.json"


def main() -> int:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in sorted(SYSTEMS.glob("*/system.md")):
        frontmatter = yaml.safe_load(record.read_text(encoding="utf-8").split("---", 2)[1])
        snapshot = frontmatter.get("first_pass_attributes", {})
        fields = snapshot.get("fields", {})
        source_term = fields.get("gui")
        if not source_term:
            continue
        grouped[source_term].append(
            {
                "system": str(record.parent.relative_to(ROOT)),
                "system_title": frontmatter.get("title"),
                "source": snapshot.get("source"),
            }
        )

    candidates = [
        {
            "source_term": source_term,
            "disposition": "needs-review",
            "note": (
                "Raw infobox interface term; review whether it names a desktop "
                "environment, window system, shell, generic interface style, or mixture."
            ),
            "hosts": hosts,
        }
        for source_term, hosts in sorted(grouped.items(), key=lambda item: item[0].casefold())
    ]
    document = {
        "schema_version": "0.1",
        "as_of": "2026-07-26",
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    OUTPUT.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(candidates)} raw interface-environment candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
