#!/usr/bin/env python3
"""Validate Terra deep-research results against their assigned manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ROOT / "inventory" / "deep-research" / "manifests"
RESULTS = ROOT / "inventory" / "deep-research" / "results"
ASSERTION_STATUSES = {"documented", "inferred", "disputed", "provisional", "unknown"}
IDENTITY_STATUSES = {"confirmed", "corrected", "ambiguous", "not-a-system"}
DISPOSITIONS = {
    "not-researched",
    "no-evidence-found",
    "unknown",
    "disputed",
    "not-applicable",
    "withheld",
}
EDITOR_RELATIONSHIPS = {
    "integral",
    "bundled-default",
    "bundled-optional",
    "first-party",
    "native",
    "ported",
    "supported-platform",
    "historically-prominent",
    "development-host-tool",
    "other",
}


def valid_url(value: str | None) -> bool:
    if not value:
        return False
    parsed = urlsplit(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(batch_id: str, require_complete: bool) -> list[str]:
    errors: list[str] = []
    manifest_path = MANIFESTS / f"{batch_id}.json"
    result_path = RESULTS / f"{batch_id}.json"
    if not manifest_path.exists():
        return [f"{batch_id}: manifest does not exist"]
    if not result_path.exists():
        return [] if not require_complete else [f"{batch_id}: result does not exist"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result.get("batch_id") != batch_id:
        errors.append(f"{batch_id}: result batch_id does not match")
    expected = {item["path"]: item for item in manifest["systems"]}
    actual = {item.get("path"): item for item in result.get("results", [])}
    if set(actual) != set(expected):
        errors.append(
            f"{batch_id}: expected paths {sorted(expected)}, got {sorted(actual)}"
        )
        return errors

    for path, item in actual.items():
        prefix = f"{batch_id}/{path}"
        if item.get("identity_status") not in IDENTITY_STATUSES:
            errors.append(f"{prefix}: invalid identity_status")
        if not item.get("research_summary"):
            errors.append(f"{prefix}: missing research_summary")
        sources = item.get("sources", [])
        source_ids = [source.get("id") for source in sources]
        if len(sources) < 2:
            errors.append(f"{prefix}: fewer than two consulted sources")
        if not any(source.get("primary") is True for source in sources):
            errors.append(f"{prefix}: no primary source")
        if len(source_ids) != len(set(source_ids)) or any(not value for value in source_ids):
            errors.append(f"{prefix}: source IDs are missing or duplicated")
        for source in sources:
            if not source.get("title") or not valid_url(source.get("url")):
                errors.append(f"{prefix}: invalid source {source.get('id')}")
            if not source.get("source_kind") or not source.get("language"):
                errors.append(f"{prefix}: incomplete source metadata {source.get('id')}")

        covered: set[str] = set()
        for claim in item.get("claims", []):
            field = claim.get("field")
            if not field:
                errors.append(f"{prefix}: claim missing field")
                continue
            covered.add(field.split(".", 1)[0])
            if claim.get("value") in (None, "", [], {}):
                errors.append(f"{prefix}: empty claim value for {field}")
            if claim.get("assertion_status") not in ASSERTION_STATUSES:
                errors.append(f"{prefix}: invalid assertion status for {field}")
            references = claim.get("source_ids", [])
            if not references or not set(references).issubset(source_ids):
                errors.append(f"{prefix}: invalid source references for {field}")
            if not claim.get("locator") or not claim.get("evidence_note"):
                errors.append(f"{prefix}: claim lacks locator/evidence note for {field}")

        for editor in item.get("editor_associations", []):
            covered.add("text_editors")
            if (
                not editor.get("name")
                or editor.get("relationship") not in EDITOR_RELATIONSHIPS
                or editor.get("assertion_status") not in ASSERTION_STATUSES
            ):
                errors.append(f"{prefix}: invalid editor association")
            references = editor.get("source_ids", [])
            if not references or not set(references).issubset(source_ids):
                errors.append(f"{prefix}: invalid editor source references")
            if not editor.get("locator") or not editor.get("evidence_note"):
                errors.append(f"{prefix}: editor lacks locator/evidence note")

        for unresolved in item.get("unresolved", []):
            field = unresolved.get("field")
            if field:
                covered.add(field.split(".", 1)[0])
            if unresolved.get("disposition") not in DISPOSITIONS:
                errors.append(f"{prefix}: invalid unresolved disposition for {field}")
            if not unresolved.get("reason"):
                errors.append(f"{prefix}: unresolved field lacks reason for {field}")
            if not set(unresolved.get("source_ids", [])).issubset(source_ids):
                errors.append(f"{prefix}: invalid unresolved source references for {field}")

        targets = set(expected[path]["missing_fields"])
        missing_coverage = sorted(targets - covered)
        if missing_coverage:
            errors.append(
                f"{prefix}: target fields neither claimed nor unresolved: "
                f"{missing_coverage}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_ids", nargs="*")
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    batch_ids = args.batch_ids or sorted(path.stem for path in MANIFESTS.glob("*.json"))
    errors = [
        error
        for batch_id in batch_ids
        for error in validate(batch_id, args.require_complete)
    ]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Deep-research validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Deep-research validation passed for {len(batch_ids)} batch(es).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
