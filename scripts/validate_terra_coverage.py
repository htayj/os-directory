#!/usr/bin/env python3
"""Validate partial or complete coverage of Terra first-pass manifests."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
MANIFESTS = INVENTORY / "terra-manifests"
RESULTS = INVENTORY / "terra-results"

DISPOSITIONS = {
    "included-system",
    "included-release",
    "included-edition",
    "included-environment",
    "system",
    "release",
    "edition",
    "alias",
    "family",
    "environment",
    "non-os",
    "grouping",
    "duplicate",
    "excluded",
    "not-an-operating-system",
    "insufficient-evidence",
    "needs-review",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def result_items(document: object) -> list[dict]:
    if isinstance(document, list):
        return document
    if isinstance(document, dict):
        for key in ("results", "candidates", "entries"):
            value = document.get(key)
            if isinstance(value, list):
                return value
    raise ValueError("result must be a list or contain results/candidates/entries")


def referenced_paths(item: dict) -> list[str]:
    paths: list[str] = []
    for key in ("path", "record_path", "system_path"):
        value = item.get(key)
        if isinstance(value, str):
            paths.append(value)
    for key in ("paths", "record_paths", "output_paths"):
        value = item.get(key)
        if isinstance(value, list):
            paths.extend(entry for entry in value if isinstance(entry, str))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="fail unless every batch has a result file",
    )
    args = parser.parse_args()

    errors: list[str] = []
    manifests = sorted(MANIFESTS.glob("batch-*.json"))
    expected_global: list[str] = []
    completed_batches = 0
    reviewed_candidates = 0
    disposition_counts: Counter[str] = Counter()

    for manifest_path in manifests:
        manifest = load(manifest_path)
        batch = int(manifest["batch"])
        expected = [item["candidate_id"] for item in manifest["candidates"]]
        expected_global.extend(expected)
        result_path = RESULTS / f"batch-{batch:03d}.json"
        if not result_path.exists():
            continue

        completed_batches += 1
        try:
            document = load(result_path)
            items = result_items(document)
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"{result_path.relative_to(ROOT)}: {exc}")
            continue

        actual = [item.get("candidate_id") for item in items]
        if Counter(actual) != Counter(expected):
            missing = sorted(set(expected) - set(actual))
            extra = sorted(set(actual) - set(expected), key=str)
            errors.append(
                f"{result_path.relative_to(ROOT)}: candidate mismatch; "
                f"missing={missing}, extra={extra}"
            )

        for item in items:
            candidate_id = item.get("candidate_id")
            disposition = item.get("disposition")
            if not isinstance(disposition, str):
                errors.append(
                    f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                    "missing string disposition"
                )
                continue
            disposition_counts[disposition] += 1
            if disposition not in DISPOSITIONS:
                errors.append(
                    f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                    f"unsupported disposition {disposition!r}"
                )
            for raw_path in referenced_paths(item):
                path = ROOT / raw_path
                if raw_path.startswith("/") or ".." in Path(raw_path).parts:
                    errors.append(
                        f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                        f"unsafe record path {raw_path!r}"
                    )
                elif not path.exists():
                    errors.append(
                        f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                        f"record path does not exist: {raw_path}"
                    )
                elif disposition == "included-system":
                    required = (
                        path / "system.md",
                        path / "index.md",
                        path / "releases" / "index.md",
                        path / "artifacts" / "index.md",
                    )
                    for required_path in required:
                        if not required_path.exists():
                            errors.append(
                                f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                                "included-system skeleton is missing "
                                f"{required_path.relative_to(ROOT)}"
                            )
        reviewed_candidates += len(items)

    duplicate_manifest_ids = [
        candidate_id
        for candidate_id, count in Counter(expected_global).items()
        if count != 1
    ]
    if duplicate_manifest_ids:
        errors.append(
            "candidate IDs do not occur exactly once across manifests: "
            + ", ".join(sorted(duplicate_manifest_ids))
        )

    if args.require_complete and completed_batches != len(manifests):
        errors.append(
            f"incomplete: {completed_batches}/{len(manifests)} batches have results"
        )

    print(
        f"Terra coverage: {completed_batches}/{len(manifests)} batches, "
        f"{reviewed_candidates}/{len(expected_global)} candidates reviewed."
    )
    if disposition_counts:
        summary = ", ".join(
            f"{key}={value}" for key, value in sorted(disposition_counts.items())
        )
        print(f"Dispositions: {summary}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
