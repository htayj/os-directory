#!/usr/bin/env python3
"""Validate text-editor inventory coverage and generated record blocks."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory" / "text-editor-associations.json"
RELATIONSHIPS = {
    "integral",
    "bundled-default",
    "bundled-optional",
    "first-party",
    "native",
    "ported",
    "historically-prominent",
    "supported-platform",
    "development-host-tool",
    "other",
}
STATUSES = {"documented", "provisional"}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening front matter delimiter")
    return yaml.safe_load(text.split("---", 2)[1])


def main() -> int:
    errors: list[str] = []
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    entries = inventory.get("systems", [])
    records = sorted((ROOT / "systems").glob("*/system.md"))
    expected = {str(path.parent.relative_to(ROOT)) for path in records}
    actual = [entry.get("path") for entry in entries]

    if len(actual) != len(set(actual)):
        errors.append("inventory contains duplicate system paths")
    missing = sorted(expected - set(actual))
    extra = sorted(set(actual) - expected)
    if missing:
        errors.append(f"inventory missing {len(missing)} paths: {missing[:5]}")
    if extra:
        errors.append(f"inventory has {len(extra)} unknown paths: {extra[:5]}")

    for entry in entries:
        path = entry.get("path", "<missing-path>")
        associations = entry.get("associations")
        if not isinstance(associations, list):
            errors.append(f"{path}: associations is not a list")
            continue
        expected_disposition = "has-associations" if associations else "no-evidence-found"
        if entry.get("disposition") != expected_disposition:
            errors.append(f"{path}: incorrect inventory disposition")
        seen: set[str] = set()
        for association in associations:
            name = association.get("name")
            if not name:
                errors.append(f"{path}: association missing name")
            elif name.casefold() in seen:
                errors.append(f"{path}: duplicate editor name {name}")
            else:
                seen.add(name.casefold())
            if association.get("relationship") not in RELATIONSHIPS:
                errors.append(f"{path}: invalid relationship for {name}")
            if association.get("assertion_status") not in STATUSES:
                errors.append(f"{path}: invalid assertion status for {name}")
            if not association.get("source"):
                errors.append(f"{path}: source missing for {name}")
            if not association.get("source_kind"):
                errors.append(f"{path}: source kind missing for {name}")

    by_path = {entry["path"]: entry for entry in entries}
    for record in records:
        path = str(record.parent.relative_to(ROOT))
        try:
            data = frontmatter(record)
        except Exception as exc:
            errors.append(f"{path}: cannot parse front matter: {exc}")
            continue
        if "text_editors" not in data:
            errors.append(f"{path}: record lacks text_editors")
            continue
        if data["text_editors"] != by_path[path]["associations"]:
            errors.append(f"{path}: record associations differ from inventory")
        research = data.get("text_editor_research", {})
        if research.get("disposition") != by_path[path]["disposition"]:
            errors.append(f"{path}: record research disposition differs from inventory")
        dispositions = [
            item
            for item in data.get("field_dispositions", [])
            if item.get("field") == "text_editors"
        ]
        if len(dispositions) != 1:
            errors.append(f"{path}: expected one text-editor field disposition")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Text-editor validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    associations = sum(len(entry["associations"]) for entry in entries)
    covered = sum(bool(entry["associations"]) for entry in entries)
    print(
        f"Text-editor validation passed: {len(records)}/{len(records)} systems "
        f"accounted for; {covered} have {associations} associations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
