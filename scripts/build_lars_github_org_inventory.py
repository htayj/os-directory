#!/usr/bin/env python3
"""Freeze Lars Brinkhoff's publicly visible GitHub organizations and repositories."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "inventory" / "preservation"
API = "https://api.github.com"
USER = "larsbrinkhoff"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"


def api_get(path: str, params: dict[str, str | int] | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(
        f"{API}{path}",
        params=params or {},
        headers=headers,
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


def paginate(path: str, params: dict[str, str | int] | None = None) -> list[dict]:
    rows: list[dict] = []
    page = 1
    while True:
        batch = api_get(path, {"per_page": 100, "page": page, **(params or {})})
        rows.extend(batch)
        if len(batch) < 100:
            return rows
        page += 1


def main() -> int:
    memberships = paginate(f"/users/{USER}/orgs")
    organizations = []
    repository_count = 0
    for membership in sorted(memberships, key=lambda item: item["login"].casefold()):
        login = membership["login"]
        organization = api_get(f"/orgs/{login}")
        repositories = paginate(
            f"/orgs/{login}/repos",
            {"type": "public", "sort": "full_name", "direction": "asc"},
        )
        repo_rows = [
            {
                "name": repo["name"],
                "full_name": repo["full_name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "fork": repo["fork"],
                "archived": repo["archived"],
                "size_kib": repo["size"],
                "default_branch": repo["default_branch"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"],
                "pushed_at": repo["pushed_at"],
                "license_spdx": (
                    repo.get("license", {}).get("spdx_id")
                    if repo.get("license")
                    else None
                ),
            }
            for repo in repositories
        ]
        repository_count += len(repo_rows)
        organizations.append(
            {
                "login": login,
                "id": organization["id"],
                "url": organization["html_url"],
                "description": organization["description"],
                "public_repos_reported": organization["public_repos"],
                "public_repos_captured": len(repo_rows),
                "created_at": organization["created_at"],
                "updated_at": organization["updated_at"],
                "repositories": repo_rows,
            }
        )

    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    source = {
        "schema_version": "0.1",
        "subject": USER,
        "profile": f"https://github.com/{USER}",
        "membership_visibility": "public-only",
        "observed_at": observed_at,
        "organization_count": len(organizations),
        "repository_count": repository_count,
        "scope_note": (
            "The GitHub public organizations endpoint exposes only publicly visible "
            "memberships. Membership does not establish authorship, ownership, or "
            "contribution to every organization repository."
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "lars-github-org-source.json").write_text(
        json.dumps(source, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUT / "lars-github-org-repositories.json").write_text(
        json.dumps(organizations, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Captured {len(organizations)} public organizations and "
        f"{repository_count} public repositories."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
