#!/usr/bin/env python3
"""Pin unversioned Wikipedia sources in multilingual discovery manifests."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import requests


ROOT = Path(__file__).resolve().parents[1]
MULTILINGUAL = ROOT / "inventory" / "multilingual"
USER_AGENT = "HistoricalOSCatalog/0.1 (OKF research bundle)"
REVISION_RE = re.compile(r'"wgRevisionId":(\d+)')


def snapshot_url(url: str, revision: int) -> str:
    parsed = urlsplit(url)
    path = unquote(parsed.path)
    if not path.startswith("/wiki/"):
        return url
    title = path.removeprefix("/wiki/")
    return (
        f"{parsed.scheme}://{parsed.netloc}/w/index.php?"
        f"title={quote(title, safe='')}&oldid={revision}"
    )


def main() -> int:
    updated = 0
    for path in sorted(MULTILINGUAL.glob("*-candidates.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        sources = document.get("sources") or document.get("source_pages") or []
        changed = False
        for source in sources:
            url = source.get("url", "")
            if source.get("revision") is not None or "wikipedia.org" not in url:
                continue
            response = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=45,
            )
            response.raise_for_status()
            match = REVISION_RE.search(response.text)
            if not match:
                raise RuntimeError(f"Could not find revision ID in {url}")
            revision = int(match.group(1))
            source["revision"] = revision
            source["snapshot_url"] = snapshot_url(response.url, revision)
            changed = True
            updated += 1
        if changed:
            path.write_text(
                json.dumps(document, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    print(f"Pinned {updated} multilingual Wikipedia sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
