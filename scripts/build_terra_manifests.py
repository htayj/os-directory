#!/usr/bin/env python3
"""Build deterministic Terra-worker manifests from frozen list occurrences."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
MANIFESTS = INVENTORY / "terra-manifests"
BATCH_SIZE = 10
BREAK_RE = re.compile(r"\s+(?:–|—|-)\s+")


def article_title(url: str) -> str | None:
    path = unquote(urlsplit(url).path)
    if not path.startswith("/wiki/"):
        return None
    return path.removeprefix("/wiki/").split("#", 1)[0].replace("_", " ")


def subject_from_label(label: str) -> str:
    return BREAK_RE.split(label, maxsplit=1)[0].strip().rstrip(" .,:;")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    return slug or "unnamed-system"


def unique_slug(base: str, used: set[str]) -> str:
    value = base
    counter = 2
    while value in used:
        value = f"{base}-{counter}"
        counter += 1
    used.add(value)
    return value


def main() -> int:
    occurrences = json.loads(
        (INVENTORY / "english-list-occurrences.json").read_text(encoding="utf-8")
    )
    child_positions = {
        item["parent_position"]
        for item in occurrences
        if item["parent_position"] is not None
    }

    grouped: dict[str, list[dict]] = defaultdict(list)
    seeds: dict[str, dict] = {}
    for occurrence in occurrences:
        article_links = [link for link in occurrence["links"] if link["article"]]
        first = article_links[0] if article_links else None
        subject = subject_from_label(occurrence["label"])
        canonical_title = None
        canonical_url = None

        if first:
            link_label = first["label"].strip()
            label_start = occurrence["label"].lstrip()
            if link_label and label_start.startswith(link_label):
                subject = link_label
                canonical_title = article_title(first["target"])
                canonical_url = first["target"]

        has_children = occurrence["position"] in child_positions
        if canonical_url:
            key = f"url:{canonical_url}"
        else:
            key = f"label:{subject.casefold()}:{'parent' if has_children else 'leaf'}"

        grouped[key].append(
            {
                "position": occurrence["position"],
                "section": occurrence["section"],
                "depth": occurrence["depth"],
                "parent_position": occurrence["parent_position"],
                "label": occurrence["label"],
                "links": occurrence["links"],
                "has_children": has_children,
            }
        )
        seeds.setdefault(
            key,
            {
                "title": subject,
                "canonical_title": canonical_title,
                "canonical_url": canonical_url,
            },
        )

    used: set[str] = set()
    candidates: list[dict] = []
    for key, candidate_occurrences in grouped.items():
        seed = seeds[key]
        candidate_id = unique_slug(slugify(seed["title"]), used)
        candidates.append(
            {
                "candidate_id": candidate_id,
                "suggested_title": seed["title"],
                "canonical_title": seed["canonical_title"],
                "canonical_url": seed["canonical_url"],
                "initial_disposition": "needs-review",
                "occurrences": candidate_occurrences,
            }
        )

    candidates.sort(key=lambda item: item["occurrences"][0]["position"])
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    for old in MANIFESTS.glob("batch-*.json"):
        old.unlink()

    batches = []
    for offset in range(0, len(candidates), BATCH_SIZE):
        number = offset // BATCH_SIZE + 1
        filename = f"batch-{number:03d}.json"
        batch = {
            "schema_version": "0.1",
            "source_revision": 1365063001,
            "batch": number,
            "candidates": candidates[offset : offset + BATCH_SIZE],
        }
        (MANIFESTS / filename).write_text(
            json.dumps(batch, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        batches.append(
            {
                "batch": number,
                "manifest": f"inventory/terra-manifests/{filename}",
                "candidate_count": len(batch["candidates"]),
                "status": "pending",
            }
        )

    (INVENTORY / "terra-batches.json").write_text(
        json.dumps(batches, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (INVENTORY / "terra-candidates.json").write_text(
        json.dumps(candidates, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(candidates)} Terra candidates in {len(batches)} batches "
        f"of at most {BATCH_SIZE}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
