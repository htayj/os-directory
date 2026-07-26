#!/usr/bin/env python3
"""Rebuild the human-readable operating-system index from system records."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYSTEMS = ROOT / "systems"


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip().strip("\"'")


def main() -> int:
    entries: list[tuple[str, str, str]] = []
    for record in sorted(SYSTEMS.glob("*/system.md")):
        text = record.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            frontmatter = text.split("---", 2)[1]
        except IndexError:
            continue
        title = scalar(frontmatter, "title") or record.parent.name
        description = scalar(frontmatter, "description")
        entries.append((title.casefold(), record.parent.name, title, description))

    lines = [
        "# Operating Systems",
        "",
        (
            "Draft system-lineage records currently present in this bundle. "
            "Their individual completeness and field dispositions are authoritative."
        ),
        "",
    ]
    for _, slug, title, description in sorted(entries):
        suffix = f" - {description}" if description else ""
        lines.append(f"* [{title}]({slug}/){suffix}")
    lines.extend(
        [
            "",
            "# Adding a System",
            "",
            "Create `systems/<system-slug>/system.md` from",
            "[`templates/operating-system.md.template`](../templates/operating-system.md.template).",
            "Put release records in `systems/<system-slug>/releases/` and artifact records in",
            "`systems/<system-slug>/artifacts/`.",
            "",
        ]
    )
    (SYSTEMS / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote systems index with {len(entries)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
