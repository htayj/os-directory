#!/usr/bin/env python3
"""Validate the public GitHub-organization preservation audit for Lars Brinkhoff."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRESERVATION = ROOT / "inventory" / "preservation"
SOURCE = PRESERVATION / "lars-github-org-source.json"
REPOSITORIES = PRESERVATION / "lars-github-org-repositories.json"
AUDIT = PRESERVATION / "lars-github-org-audit.json"

CLASSIFICATIONS = {
    "commercial-unrelated",
    "contemporary-technology",
    "empty-public-org",
    "general-community",
    "historical-computing",
    "historical-design-archive",
    "language-history",
    "preservation-focused",
}
ARTIFACT_KINDS = {
    "application-preservation",
    "documentation-archive",
    "emulator",
    "format-recovery-tool",
    "hardware-documentation",
    "hardware-restoration-tool",
    "language-runtime",
    "media-image",
    "network-restoration",
    "software-history",
    "source-history",
    "source-reconstruction",
}
REQUIRED_SYSTEMS = {
    "systems/bbn-exec-iii",
    "systems/colorforth",
    "systems/pdp-6-timesharing-system-1-4",
    "systems/ti-system-v-68",
}


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    organizations = json.loads(REPOSITORIES.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    errors: list[str] = []

    if source.get("membership_visibility") != "public-only":
        errors.append("source membership_visibility must be public-only")
    if source.get("organization_count") != len(organizations):
        errors.append("source organization_count differs from snapshot")

    logins = [org.get("login") for org in organizations]
    if None in logins or len(logins) != len(set(logins)):
        errors.append("organization snapshot contains missing or duplicate logins")

    repositories: dict[str, dict] = {}
    for org in organizations:
        login = org.get("login", "<unknown>")
        captured = org.get("repositories", [])
        if org.get("public_repos_reported") != len(captured):
            errors.append(f"{login}: reported repository count differs from captured list")
        if org.get("public_repos_captured") != len(captured):
            errors.append(f"{login}: captured repository count differs from list")
        for repository in captured:
            full_name = repository.get("full_name")
            if not full_name or full_name in repositories:
                errors.append(f"{login}: missing or duplicate repository {full_name!r}")
            else:
                repositories[full_name] = repository

    if source.get("repository_count") != len(repositories):
        errors.append("source repository_count differs from snapshot")

    audit_orgs = audit.get("organizations", [])
    audit_logins = [org.get("login") for org in audit_orgs]
    if set(audit_logins) != set(logins) or len(audit_logins) != len(logins):
        errors.append("audit must disposition every snapshot organization exactly once")
    for org in audit_orgs:
        if org.get("classification") not in CLASSIFICATIONS:
            errors.append(
                f"{org.get('login', '<unknown>')}: invalid classification "
                f"{org.get('classification')!r}"
            )

    selected: set[str] = set()
    mapped_systems: set[str] = set()
    for cluster in audit.get("clusters", []):
        login = cluster.get("organization")
        if login not in set(logins):
            errors.append(f"cluster references unknown organization {login!r}")
        kinds = set(cluster.get("artifact_kinds", []))
        if not kinds or not kinds <= ARTIFACT_KINDS:
            errors.append(f"{login}: invalid or empty artifact_kinds")
        for full_name in cluster.get("repositories", []):
            if full_name in selected:
                errors.append(f"duplicate selected repository {full_name}")
            selected.add(full_name)
            if full_name not in repositories:
                errors.append(f"selected repository absent from snapshot: {full_name}")
            if login and not full_name.startswith(f"{login}/"):
                errors.append(f"{full_name}: repository does not belong to cluster org {login}")
        for system in cluster.get("systems", []):
            mapped_systems.add(system)
            path = ROOT / system / "system.md"
            if not system.startswith("systems/") or not path.is_file():
                errors.append(f"{login}: missing catalog record {system}")

    if not REQUIRED_SYSTEMS <= mapped_systems:
        errors.append(
            "required organization-discovered systems are not all mapped: "
            + ", ".join(sorted(REQUIRED_SYSTEMS - mapped_systems))
        )

    if errors:
        raise SystemExit("\n".join(errors))

    print(
        "Validated Lars Brinkhoff public GitHub organization audit: "
        f"{len(organizations)} organizations, {len(repositories)} repositories, "
        f"{len(selected)} preservation selections, {len(mapped_systems)} system mappings."
    )


if __name__ == "__main__":
    main()
