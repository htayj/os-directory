#!/usr/bin/env python3
"""Validate the generated GitHub Pages data against the catalog inventory."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def main() -> int:
    errors: list[str] = []
    required = ("index.html", "styles.css", "app.js", "data.json", ".nojekyll")
    for name in required:
        if not (SITE / name).is_file():
            errors.append(f"site/{name}: missing")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    data = json.loads((SITE / "data.json").read_text(encoding="utf-8"))
    inventory = json.loads(
        (ROOT / "inventory" / "text-editor-associations.json").read_text(
            encoding="utf-8"
        )
    )
    records = sorted((ROOT / "systems").glob("*/system.md"))
    rows = data.get("systems", [])
    paths = [row.get("record_path") for row in rows]
    expected_paths = [record.relative_to(ROOT).as_posix() for record in records]

    if paths != expected_paths:
        errors.append("site rows do not exactly match sorted system record paths")
    if len({row.get("id") for row in rows}) != len(rows):
        errors.append("site rows contain duplicate IDs")
    if any(not row.get("title") for row in rows):
        errors.append("one or more site rows lack a title")
    if any(
        not row.get("record_url", "").startswith("https://github.com/")
        for row in rows
    ):
        errors.append("one or more site rows lack a GitHub record URL")

    associations = sum(len(row.get("editors", [])) for row in rows)
    inventory_associations = sum(
        len(system["associations"]) for system in inventory["systems"]
    )
    if associations < inventory_associations:
        errors.append(
            f"site has only {associations} associations; baseline inventory has "
            f"{inventory_associations}. Deep-research overlays may increase but "
            "must not reduce this count"
        )
    if data.get("stats", {}).get("systems") != len(records):
        errors.append("site system statistic is incorrect")
    if data.get("stats", {}).get("associations") != associations:
        errors.append("site association statistic is incorrect")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Pages validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Pages validation passed: {len(rows)} system rows and "
        f"{associations} editor associations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
