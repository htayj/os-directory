#!/usr/bin/env python3
"""Validate the structural OKF v0.2 rules used by this bundle."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESERVED = {"index.md", "log.md"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
DATE_HEADING_RE = re.compile(r"^## \d{4}-\d{2}-\d{2}$")


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        closing = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML frontmatter delimiter") from exc
    try:
        data = yaml.safe_load("\n".join(lines[1:closing]))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data, "\n".join(lines[closing + 1 :])


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = unquote(urlsplit(raw_target).path)
    if not target or target.startswith(("#", "//")):
        return None
    if urlsplit(raw_target).scheme:
        return None
    if target.startswith("/"):
        candidate = ROOT / target.removeprefix("/")
    else:
        candidate = source.parent / target
    return candidate.resolve()


def validate() -> list[str]:
    errors: list[str] = []
    markdown_files = sorted(ROOT.rglob("*.md"))

    for path in markdown_files:
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        if path.name not in RESERVED:
            try:
                data, _ = frontmatter(path)
                if not isinstance(data.get("type"), str) or not data["type"].strip():
                    errors.append(f"{relative}: missing non-empty type")
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"{relative}: {exc}")
        elif path.name == "index.md" and relative == Path("index.md"):
            try:
                data, _ = frontmatter(path)
                if data.get("okf_version") != "0.2":
                    errors.append("index.md: okf_version must be \"0.2\"")
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"index.md: {exc}")
        elif text.startswith("---"):
            errors.append(f"{relative}: only the root index.md may have frontmatter")

        if path.name == "log.md":
            for line in text.splitlines():
                if line.startswith("## ") and not DATE_HEADING_RE.fullmatch(line):
                    errors.append(f"{relative}: invalid date heading {line!r}")

        for match in LINK_RE.finditer(text):
            candidate = local_link_target(path, match.group(1))
            if candidate is None:
                continue
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: local link escapes bundle: {match.group(1)}")
                continue
            if not candidate.exists():
                errors.append(f"{relative}: broken local link: {match.group(1)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"OKF validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    count = len(list(ROOT.rglob("*.md")))
    print(f"OKF v0.2 validation passed for {count} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
