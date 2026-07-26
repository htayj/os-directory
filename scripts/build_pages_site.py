#!/usr/bin/env python3
"""Build the static GitHub Pages data set from OKF operating-system records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
OUTPUT = SITE / "data.json"
REPOSITORY_URL = "https://github.com/htayj/os-directory"


def frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter")
    return yaml.safe_load(text.split("---", 2)[1])


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, (str, int, float)):
        return str(value)
    if isinstance(value, list):
        return "; ".join(part for item in value if (part := scalar(item)))
    if isinstance(value, dict):
        for key in (
            "value",
            "name",
            "title",
            "country",
            "language",
            "platform",
            "architecture",
            "identifier",
            "license",
            "organization",
        ):
            if value.get(key) not in (None, "", [], {}):
                return scalar(value[key])
    return ""


def list_values(values: Any, keys: tuple[str, ...]) -> list[str]:
    if values in (None, "", [], {}):
        return []
    values = values if isinstance(values, list) else [values]
    result: list[str] = []
    for item in values:
        if isinstance(item, dict):
            value = next((scalar(item.get(key)) for key in keys if scalar(item.get(key))), "")
        else:
            value = scalar(item)
        if value and value not in result:
            result.append(value)
    return result


def first_pass(data: dict[str, Any], field: str) -> str:
    return scalar(data.get("first_pass_attributes", {}).get("fields", {}).get(field))


def prefer(values: list[str], fallback: str) -> list[str]:
    return values or ([fallback] if fallback else [])


def system_row(record: Path) -> dict[str, Any]:
    data = frontmatter(record)
    relative = record.relative_to(ROOT).as_posix()
    editor_research = data.get("text_editor_research", {})
    completeness = data.get("catalog_completeness", {})

    countries = prefer(
        list_values(data.get("countries_of_origin"), ("country", "value", "name")),
        first_pass(data, "country_of_origin"),
    )
    purposes = prefer(
        list_values(data.get("design_purposes"), ("value", "name")),
        first_pass(data, "purpose"),
    )
    languages = prefer(
        list_values(data.get("programming_languages"), ("language", "name", "value")),
        first_pass(data, "programming_languages"),
    )
    licenses = prefer(
        list_values(data.get("licenses"), ("identifier", "name", "value", "license")),
        first_pass(data, "license"),
    )
    kernels = prefer(
        list_values(data.get("kernels"), ("architecture", "name", "value", "type")),
        first_pass(data, "kernel_type"),
    )
    platforms = list_values(
        data.get("hardware_platforms"), ("platform", "name", "value")
    )
    platforms.extend(
        value
        for value in list_values(
            data.get("architectures"), ("architecture", "name", "value")
        )
        if value not in platforms
    )
    platforms = prefer(platforms, first_pass(data, "platforms"))

    gui = list_values(data.get("gui_status"), ("value", "name", "style"))
    gui.extend(
        value
        for value in list_values(data.get("interfaces"), ("style", "name", "value"))
        if value not in gui
    )
    gui = prefer(gui, first_pass(data, "gui"))

    editors = []
    for editor in data.get("text_editors", []):
        editors.append(
            {
                "name": scalar(editor.get("name")),
                "relationship": scalar(editor.get("relationship")),
                "interface_style": scalar(editor.get("interface_style")),
                "assertion_status": scalar(editor.get("assertion_status")),
                "source": scalar(editor.get("source")),
                "source_kind": scalar(editor.get("source_kind")),
                "note": scalar(editor.get("note")),
            }
        )

    status = scalar(data.get("development_status")) or first_pass(
        data, "development_status"
    )
    return {
        "id": record.parent.name,
        "title": scalar(data.get("title")) or record.parent.name,
        "description": scalar(data.get("description")),
        "record_path": relative,
        "record_url": f"{REPOSITORY_URL}/blob/main/{relative}",
        "catalog_level": scalar(completeness.get("level")),
        "catalog_status": scalar(data.get("status")),
        "development_status": status,
        "country": countries,
        "purpose": purposes,
        "programming_language": languages,
        "license": licenses,
        "first_release": first_pass(data, "first_release"),
        "latest_release": first_pass(data, "latest_release"),
        "last_updated": first_pass(data, "last_updated"),
        "gui": gui,
        "platform": platforms,
        "kernel": kernels,
        "editor_disposition": scalar(editor_research.get("disposition"))
        or ("has-associations" if editors else "no-evidence-found"),
        "editor_checked_at": scalar(editor_research.get("checked_at")),
        "editors": editors,
    }


def main() -> int:
    rows = [
        system_row(record)
        for record in sorted((ROOT / "systems").glob("*/system.md"))
    ]
    associations = [editor for row in rows for editor in row["editors"]]
    payload = {
        "schema_version": "0.1",
        "as_of": max((row["editor_checked_at"] for row in rows), default=""),
        "repository": REPOSITORY_URL,
        "stats": {
            "systems": len(rows),
            "systems_with_editors": sum(bool(row["editors"]) for row in rows),
            "associations": len(associations),
            "unique_editors": len(
                {editor["name"].casefold() for editor in associations}
            ),
            "documented_associations": sum(
                editor["assertion_status"] == "documented"
                for editor in associations
            ),
            "provisional_associations": sum(
                editor["assertion_status"] == "provisional"
                for editor in associations
            ),
        },
        "systems": rows,
    }
    SITE.mkdir(exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Built {OUTPUT.relative_to(ROOT)} with {len(rows)} systems and "
        f"{len(associations)} editor associations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
