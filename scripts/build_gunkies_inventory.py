#!/usr/bin/env python3
"""Freeze the recursive Computer History Wiki operating-system category corpus."""

from __future__ import annotations

import hashlib
import json
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "inventory" / "gunkies"
API = "https://gunkies.org/w/api.php"
ROOT_CATEGORY = "Category:Operating Systems"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"


def api_get(params: dict[str, str | int]) -> dict[str, Any]:
    response = requests.get(
        API,
        params={"format": "json", "formatversion": "2", **params},
        headers={"User-Agent": USER_AGENT},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


def category_members(title: str) -> list[dict[str, Any]]:
    members: list[dict[str, Any]] = []
    continuation: dict[str, str] = {}
    while True:
        payload = api_get(
            {
                "action": "query",
                "list": "categorymembers",
                "cmtitle": title,
                "cmlimit": "max",
                "cmtype": "page|subcat",
                **continuation,
            }
        )
        members.extend(payload["query"]["categorymembers"])
        if "continue" not in payload:
            return members
        continuation = payload["continue"]


def page_revisions(page_ids: list[int]) -> dict[int, dict[str, Any]]:
    revisions: dict[int, dict[str, Any]] = {}
    for offset in range(0, len(page_ids), 50):
        payload = api_get(
            {
                "action": "query",
                "prop": "info|revisions",
                "inprop": "url",
                "rvprop": "ids|timestamp|content",
                "pageids": "|".join(str(value) for value in page_ids[offset : offset + 50]),
            }
        )
        for page in payload["query"]["pages"]:
            revision = page["revisions"][0]
            content = revision.get("content", "")
            revisions[page["pageid"]] = {
                "title": page["title"],
                "url": page["fullurl"],
                "revision": revision["revid"],
                "revision_timestamp": revision["timestamp"],
                "wikitext_sha256": hashlib.sha256(
                    content.encode("utf-8")
                ).hexdigest(),
            }
    return revisions


def build() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    queue = deque([(ROOT_CATEGORY, 0)])
    seen_categories: set[str] = set()
    categories: list[dict[str, Any]] = []
    pages: dict[int, dict[str, Any]] = {}

    while queue:
        category, depth = queue.popleft()
        if category in seen_categories:
            continue
        seen_categories.add(category)
        members = category_members(category)
        categories.append(
            {
                "title": category,
                "depth": depth,
                "page_members": sum(member["ns"] == 0 for member in members),
                "subcategory_members": sum(member["ns"] == 14 for member in members),
            }
        )
        for member in members:
            if member["ns"] == 14:
                queue.append((member["title"], depth + 1))
            elif member["ns"] == 0:
                page = pages.setdefault(
                    member["pageid"],
                    {
                        "page_id": member["pageid"],
                        "title": member["title"],
                        "categories": [],
                    },
                )
                page["categories"].append(category)

    revisions = page_revisions(
        [page["page_id"] for page in sorted(pages.values(), key=lambda row: row["page_id"])]
    )
    page_rows = []
    for page in sorted(pages.values(), key=lambda row: row["title"].casefold()):
        page_rows.append(
            page
            | revisions[page["page_id"]]
            | {"categories": sorted(page["categories"])}
        )

    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    source = {
        "schema_version": "0.1",
        "title": "Computer History Wiki recursive operating-system category corpus",
        "root_category": ROOT_CATEGORY,
        "root_url": "https://gunkies.org/wiki/Category:Operating_Systems",
        "observed_at": observed_at,
        "maximum_category_depth": max(row["depth"] for row in categories),
        "category_count": len(categories),
        "page_count": len(page_rows),
        "scope_note": (
            "Every namespace-0 page reachable through recursive category membership "
            "below the root is retained. Category membership is a "
            "discovery signal, not proof that a page describes an operating system."
        ),
        "categories": sorted(categories, key=lambda row: (row["depth"], row["title"])),
    }
    return source, page_rows


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    source, pages = build()
    write_json(OUT / "category-source.json", source)
    write_json(OUT / "category-pages.json", pages)
    print(
        f"Captured {source['page_count']} unique pages across "
        f"{source['category_count']} categories."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
