#!/usr/bin/env python3
"""Audit research gaps and build non-overlapping Terra deep-dive manifests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "inventory" / "deep-research"
MANIFESTS = OUTPUT / "manifests"
RESULTS = OUTPUT / "results"
AUDIT_DATE = "2026-07-29"
WAVE_001_DATE = "2026-07-27"

FIELD_SOURCES = {
    "organizations": ("organizations",),
    "countries_of_origin": ("countries_of_origin", "development_origins"),
    "design_purposes": ("design_purposes", "development_contexts", "design_goals"),
    "development_status": ("development_status",),
    "lifecycle_events": (
        "lifecycle_events",
        "first_release",
        "latest_releases",
        "last_updated",
    ),
    "rights_regime": ("rights_regime", "software_freedom_status"),
    "licenses": ("licenses",),
    "programming_languages": ("programming_languages",),
    "system_organization": ("system_organization",),
    "kernels": ("kernels",),
    "interfaces": ("interfaces", "gui_status", "shells", "window_systems"),
    "platforms": ("hardware_platforms", "architectures"),
    "text_editors": ("text_editors",),
}
MISSING_DISPOSITIONS = {"not-researched", "no-evidence-found", "unknown"}

WAVE_001 = {
    "wave-001-batch-001": {
        "theme": "historical academic and research systems",
        "systems": [
            "compatible-time-sharing-system",
            "waits",
            "xinu",
            "xv6",
            "v",
        ],
    },
    "wave-001-batch-002": {
        "theme": "commercial and proprietary platform systems",
        "systems": [
            "z-vm",
            "vxworks",
            "workplace-os",
            "windows-iot",
            "xbox-system-software",
        ],
    },
    "wave-001-batch-003": {
        "theme": "non-English and regionally documented systems",
        "systems": [
            "z80-rio",
            "waha-linux",
            "human68k",
            "ptos-nec",
            "tmaxos",
        ],
    },
}


def frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def is_empty(value: Any) -> bool:
    return value in (None, "", [], {})


def missing_fields(data: dict[str, Any], include_deep_research: bool = True) -> list[str]:
    dispositions = {
        item.get("field"): item.get("disposition")
        for item in data.get("field_dispositions", [])
        if isinstance(item, dict)
    }
    deep = data.get("deep_research", {}) if include_deep_research else {}
    deep_claims = {
        claim.get("field", "").split(".", 1)[0]
        for claim in deep.get("claims", [])
        if claim.get("field")
    }
    if deep.get("editor_associations"):
        deep_claims.add("text_editors")
    missing = []
    for field, keys in FIELD_SOURCES.items():
        if field in deep_claims:
            continue
        has_value = field in deep_claims or any(
            not is_empty(data.get(key)) for key in keys
        )
        disposition = dispositions.get(field)
        if not has_value or disposition in MISSING_DISPOSITIONS:
            missing.append(field)
    return missing


def provisional_fields(data: dict[str, Any]) -> list[str]:
    result = []
    first_pass = data.get("first_pass_attributes", {}).get("fields", {})
    for field, value in first_pass.items():
        if not is_empty(value):
            result.append(field)
    return sorted(set(result))


def compact_source(source: Any) -> dict[str, Any]:
    if not isinstance(source, dict):
        return {}
    return {
        key: source.get(key)
        for key in (
            "id",
            "title",
            "resource",
            "archived_resource",
            "source_kind",
            "language",
            "revision",
        )
        if source.get(key) not in (None, "", [], {})
    }


def candidate(
    record: Path, include_deep_research: bool = True
) -> dict[str, Any]:
    data = frontmatter(record)
    missing = missing_fields(data, include_deep_research)
    languages = sorted(
        {
            item.get("language")
            for item in data.get("discovery_provenance", [])
            if isinstance(item, dict) and item.get("language")
        }
    )
    aliases = [
        item.get("value")
        for item in data.get("names", [])
        if isinstance(item, dict) and item.get("value")
    ]
    priority = len(missing) * 10
    priority += 8 if "text_editors" in missing else 0
    priority += 5 if data.get("catalog_completeness", {}).get("level") == "inventory" else 0
    priority += 3 if any(language != "en" for language in languages) else 0
    return {
        "path": record.parent.relative_to(ROOT).as_posix(),
        "title": data.get("title", record.parent.name),
        "aliases": aliases,
        "discovery_languages": languages,
        "catalog_level": data.get("catalog_completeness", {}).get("level"),
        "missing_fields": missing,
        "provisional_fields": provisional_fields(data),
        "first_pass_attributes": data.get("first_pass_attributes", {}),
        "existing_sources": [
            compact
            for source in data.get("sources", [])
            if (compact := compact_source(source))
        ],
        "existing_text_editors": data.get("text_editors", []),
        "priority_score": priority,
    }


def main() -> int:
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)
    candidates = {
        item["path"].split("/", 1)[1]: item
        for record in sorted((ROOT / "systems").glob("*/system.md"))
        if (item := candidate(record))
    }
    original_candidates = {
        item["path"].split("/", 1)[1]: item
        for record in sorted((ROOT / "systems").glob("*/system.md"))
        if (item := candidate(record, include_deep_research=False))
    }
    ranked = sorted(
        candidates.values(),
        key=lambda item: (-item["priority_score"], item["title"].casefold()),
    )
    (OUTPUT / "candidates-ranked.json").write_text(
        json.dumps(
            {
                "schema_version": "0.1",
                "as_of": AUDIT_DATE,
                "core_fields": list(FIELD_SOURCES),
                "systems": ranked,
            },
            ensure_ascii=False,
            indent=2,
            default=str,
        )
        + "\n",
        encoding="utf-8",
    )

    assigned: set[str] = set()
    for batch_id, definition in WAVE_001.items():
        systems = []
        for slug in definition["systems"]:
            if slug not in original_candidates:
                raise ValueError(f"{batch_id}: unknown system {slug}")
            if slug in assigned:
                raise ValueError(f"{batch_id}: duplicate assignment {slug}")
            assigned.add(slug)
            systems.append(original_candidates[slug])
        payload = {
            "schema_version": "0.1",
            "batch_id": batch_id,
            "theme": definition["theme"],
            "as_of": WAVE_001_DATE,
            "agent_guide": "schema/deep-research-agent-guide.md",
            "result_path": f"inventory/deep-research/results/{batch_id}.json",
            "systems": systems,
        }
        (MANIFESTS / f"{batch_id}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n",
            encoding="utf-8",
        )
    print(
        f"Built ranked audit for {len(ranked)} systems and "
        f"{len(WAVE_001)} wave-001 manifests ({len(assigned)} systems)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
