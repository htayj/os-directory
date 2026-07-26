#!/usr/bin/env python3
"""Validate multilingual discovery normalization and catalog-batch coverage."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MULTILINGUAL = ROOT / "inventory" / "multilingual"
MANIFESTS = MULTILINGUAL / "manifests"
RESULTS = MULTILINGUAL / "results"
REQUIRED_ATTRIBUTES = (
    "developer",
    "country_of_origin",
    "purpose",
    "programming_languages",
    "first_release",
    "latest_release",
    "last_updated",
    "development_status",
    "source_model",
    "os_family",
    "gui",
    "platforms",
    "kernel_type",
    "license",
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    manifests = sorted(MANIFESTS.glob("batch-*.json"))
    expected_total = 0
    completed = 0
    cataloged = 0

    for manifest_path in manifests:
        manifest = load(manifest_path)
        batch = int(manifest["batch"])
        expected = [item["candidate_id"] for item in manifest["candidates"]]
        expected_total += len(expected)
        result_path = RESULTS / f"batch-{batch:03d}.json"
        if not result_path.exists():
            continue
        completed += 1
        document = load(result_path)
        items = document.get("results", document if isinstance(document, list) else [])
        actual = [item.get("candidate_id") for item in items]
        if Counter(actual) != Counter(expected):
            errors.append(
                f"{result_path.relative_to(ROOT)}: candidate mismatch; "
                f"missing={sorted(set(expected) - set(actual))}, "
                f"extra={sorted(set(actual) - set(expected), key=str)}"
            )
        for item in items:
            candidate_id = item.get("candidate_id")
            if item.get("disposition") != "included-system":
                errors.append(
                    f"{result_path.relative_to(ROOT)}:{candidate_id}: "
                    "catalog manifest result must be included-system"
                )
            raw_path = item.get("path")
            if not isinstance(raw_path, str):
                errors.append(
                    f"{result_path.relative_to(ROOT)}:{candidate_id}: missing path"
                )
                continue
            path = ROOT / raw_path
            required = (
                path / "system.md",
                path / "index.md",
                path / "releases" / "index.md",
                path / "artifacts" / "index.md",
            )
            for required_path in required:
                if not required_path.exists():
                    errors.append(
                        f"{result_path.relative_to(ROOT)}:{candidate_id}: missing "
                        f"{required_path.relative_to(ROOT)}"
                    )
            system_path = path / "system.md"
            if not system_path.exists():
                continue
            try:
                frontmatter = yaml.safe_load(
                    system_path.read_text(encoding="utf-8").split("---", 2)[1]
                )
            except (IndexError, yaml.YAMLError) as exc:
                errors.append(
                    f"{system_path.relative_to(ROOT)}: invalid frontmatter: {exc}"
                )
                continue
            attribute_envelope = frontmatter.get("first_pass_attributes", {})
            attributes = attribute_envelope.get("fields", attribute_envelope)
            dispositions = frontmatter.get(
                "first_pass_attribute_dispositions",
                attribute_envelope.get("dispositions", {}),
            )
            for field in REQUIRED_ATTRIBUTES:
                if field not in attributes:
                    errors.append(
                        f"{system_path.relative_to(ROOT)}: missing "
                        f"first_pass_attributes.{field}"
                    )
                if field not in dispositions:
                    errors.append(
                        f"{system_path.relative_to(ROOT)}: missing "
                        f"first_pass_attribute_dispositions.{field}"
                    )
            provenance = frontmatter.get("discovery_provenance", [])
            if not any(
                entry.get("native_label")
                and entry.get("language")
                and entry.get("source")
                for entry in provenance
                if isinstance(entry, dict)
            ):
                errors.append(
                    f"{system_path.relative_to(ROOT)}: missing native discovery "
                    "label, language, or source"
                )
        cataloged += len(items)

    if args.require_complete and completed != len(manifests):
        errors.append(
            f"incomplete: {completed}/{len(manifests)} multilingual batches complete"
        )
    print(
        f"Multilingual coverage: {completed}/{len(manifests)} batches, "
        f"{cataloged}/{expected_total} supplemental systems cataloged."
    )
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
