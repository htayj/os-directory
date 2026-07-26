#!/usr/bin/env python3
"""Extract every list occurrence from the frozen English Wikipedia baseline."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "inventory"
API = "https://en.wikipedia.org/w/api.php"
ARTICLE_BASE = "https://en.wikipedia.org"
PAGE_TITLE = "List of operating systems"
REVISION = 1365063001
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"
EDIT_RE = re.compile(r"\s*\[\s*edit\s*\]\s*$", re.IGNORECASE)


def api_get(params: dict[str, str | int]) -> dict:
    response = requests.get(
        API,
        params={"format": "json", "formatversion": "2", **params},
        headers={"User-Agent": USER_AGENT},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


def direct_content(item: Tag) -> Tag:
    fragment = BeautifulSoup(str(item), "html.parser").find("li")
    assert fragment is not None
    for nested in fragment.find_all(["ul", "ol"], recursive=False):
        nested.decompose()
    return fragment


def clean_heading(tag: Tag) -> str:
    text = tag.get_text(" ", strip=True)
    return EDIT_RE.sub("", text).strip()


def build() -> tuple[dict, list[dict]]:
    revision_data = api_get(
        {
            "action": "query",
            "prop": "revisions",
            "rvprop": "ids|timestamp",
            "revids": REVISION,
        }
    )
    page = revision_data["query"]["pages"][0]
    revision = page["revisions"][0]
    if revision["revid"] != REVISION or page["title"] != PAGE_TITLE:
        raise RuntimeError("MediaWiki returned an unexpected baseline revision")

    parsed = api_get(
        {
            "action": "parse",
            "oldid": REVISION,
            "prop": "text",
        }
    )
    html = parsed["parse"]["text"]
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one(".mw-parser-output") or soup

    headings: dict[int, str] = {}
    occurrence_by_tag: dict[int, int] = {}
    occurrences: list[dict] = []
    stopped = False

    for tag in content.find_all(["h2", "h3", "h4", "h5", "h6", "li"]):
        if tag.name and tag.name.startswith("h"):
            level = int(tag.name[1])
            heading = clean_heading(tag)
            if level == 2 and heading == "See also":
                stopped = True
                break
            headings[level] = heading
            for deeper in range(level + 1, 7):
                headings.pop(deeper, None)
            continue

        if stopped or tag.name != "li":
            continue

        body = direct_content(tag)
        label = body.get_text(" ", strip=True)
        if not label:
            continue

        direct_links = []
        for link in body.find_all("a", href=True):
            href = link["href"]
            direct_links.append(
                {
                    "label": link.get_text(" ", strip=True),
                    "target": urljoin(ARTICLE_BASE, href),
                    "article": href.startswith("/wiki/")
                    and ":" not in href.removeprefix("/wiki/").split("#", 1)[0],
                }
            )

        parent_item = tag.find_parent("li")
        parent_position = occurrence_by_tag.get(id(parent_item)) if parent_item else None
        position = len(occurrences) + 1
        occurrence_by_tag[id(tag)] = position

        occurrences.append(
            {
                "position": position,
                "section": [headings[level] for level in sorted(headings)],
                "depth": len(tag.find_parents(["ul", "ol"])),
                "parent_position": parent_position,
                "label": label,
                "links": direct_links,
            }
        )

    retrieved_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    source = {
        "schema_version": "0.1",
        "title": PAGE_TITLE,
        "page_id": page["pageid"],
        "revision": REVISION,
        "revision_timestamp": revision["timestamp"],
        "permalink": (
            "https://en.wikipedia.org/w/index.php?"
            f"title=List_of_operating_systems&oldid={REVISION}"
        ),
        "retrieved_at": retrieved_at,
        "parsed_html_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest(),
        "occurrence_count": len(occurrences),
    }
    return source, occurrences


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    source, occurrences = build()
    write_json(OUT / "english-list-source.json", source)
    write_json(OUT / "english-list-occurrences.json", occurrences)
    print(
        f"Wrote {len(occurrences)} baseline occurrences from revision "
        f"{source['revision']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
