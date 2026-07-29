#!/usr/bin/env python3
"""Validate the curated Lars Brinkhoff preservation-source inventory."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory" / "preservation" / "larsbrinkhoff.json"

RELATIONSHIPS = {
    "profile-owned",
    "profile-fork",
    "external-project-with-verified-contribution",
}
ARTIFACT_KINDS = {
    "documentation-archive",
    "emulator-build",
    "format-recovery-tool",
    "media-image",
    "network-restoration",
    "oral-history",
    "software-history",
    "source-history",
    "source-reconstruction",
}


def main() -> None:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    snapshot = data["snapshot"]
    projects = data["projects"]
    errors: list[str] = []

    if snapshot["profile_public_repositories_screened"] != 208:
        errors.append("profile_public_repositories_screened must be 208")
    if snapshot["selected_preservation_projects"] != len(projects):
        errors.append("selected_preservation_projects does not match project count")
    if set(data["relationship_vocabulary"]) != RELATIONSHIPS:
        errors.append("relationship_vocabulary differs from validator")
    if set(data["artifact_kind_vocabulary"]) != ARTIFACT_KINDS:
        errors.append("artifact_kind_vocabulary differs from validator")

    repositories: set[str] = set()
    urls: set[str] = set()
    for index, project in enumerate(projects, start=1):
        label = project.get("repository", f"project {index}")
        repository = project.get("repository")
        url = project.get("url")
        relationship = project.get("relationship")
        kinds = project.get("artifact_kinds", [])

        if not repository or repository in repositories:
            errors.append(f"{label}: missing or duplicate repository")
        repositories.add(repository)
        if not url or url in urls:
            errors.append(f"{label}: missing or duplicate URL")
        urls.add(url)
        if relationship not in RELATIONSHIPS:
            errors.append(f"{label}: invalid relationship {relationship!r}")
        if not kinds or not set(kinds) <= ARTIFACT_KINDS:
            errors.append(f"{label}: invalid or empty artifact_kinds")

        if relationship == "external-project-with-verified-contribution":
            contributions = project.get("contributions")
            if not isinstance(contributions, int) or contributions <= 0:
                errors.append(f"{label}: external contribution is not verified")
        elif "contributions" in project:
            errors.append(f"{label}: contribution count is only valid externally")

        for system in project.get("systems", []):
            system_path = ROOT / system / "system.md"
            if not system.startswith("systems/") or not system_path.is_file():
                errors.append(f"{label}: missing catalog record {system}")

    if errors:
        raise SystemExit("\n".join(errors))

    mapped = sum(bool(project.get("systems")) for project in projects)
    print(
        "Validated Lars Brinkhoff preservation inventory: "
        f"{len(projects)} selected projects, {mapped} system-mapped, "
        f"{snapshot['profile_public_repositories_screened']} profile repositories screened."
    )


if __name__ == "__main__":
    main()
