#!/usr/bin/env python3
"""Summarize completed deep-research batches for human merge review."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "inventory" / "deep-research" / "results"


def main() -> int:
    systems = sources = primary = claims = editors = unresolved = 0
    fields: Counter[str] = Counter()
    for path in sorted(RESULTS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"{data['batch_id']}:")
        for result in data.get("results", []):
            source_count = len(result.get("sources", []))
            primary_count = sum(
                source.get("primary") is True for source in result.get("sources", [])
            )
            claim_count = len(result.get("claims", []))
            editor_count = len(result.get("editor_associations", []))
            unresolved_count = len(result.get("unresolved", []))
            print(
                f"  {result['title']}: {source_count} sources "
                f"({primary_count} primary), {claim_count} claims, "
                f"{editor_count} editors, {unresolved_count} unresolved"
            )
            systems += 1
            sources += source_count
            primary += primary_count
            claims += claim_count
            editors += editor_count
            unresolved += unresolved_count
            fields.update(
                claim.get("field", "").split(".", 1)[0]
                for claim in result.get("claims", [])
                if claim.get("field")
            )
    print(
        f"Total: {systems} systems, {sources} sources ({primary} primary), "
        f"{claims} claims, {editors} editor associations, "
        f"{unresolved} unresolved dispositions."
    )
    if fields:
        print("Claims by field:")
        for field, count in sorted(fields.items()):
            print(f"  {field}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
