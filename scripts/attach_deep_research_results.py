#!/usr/bin/env python3
"""Attach validated deep-research snapshots to their operating-system records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml

from validate_deep_research_results import RESULTS, validate


ROOT = Path(__file__).resolve().parents[1]
BLOCK_START = "# BEGIN GENERATED DEEP RESEARCH"
BLOCK_END = "# END GENERATED DEEP RESEARCH"


def attach(record: Path, batch: dict, result: dict) -> None:
    text = record.read_text(encoding="utf-8")
    if BLOCK_START in text:
        start = text.index(BLOCK_START)
        end = text.index(BLOCK_END, start) + len(BLOCK_END)
        text = text[:start].rstrip() + "\n" + text[end:].lstrip("\n")
    snapshot = {
        "deep_research": {
            "batch_id": batch["batch_id"],
            "researcher": batch.get("researcher"),
            "researched_at": batch.get("researched_at"),
            "identity_status": result["identity_status"],
            "research_summary": result["research_summary"],
            "sources": result["sources"],
            "claims": result.get("claims", []),
            "editor_associations": result.get("editor_associations", []),
            "unresolved": result.get("unresolved", []),
        }
    }
    block = (
        f"{BLOCK_START}\n"
        + yaml.safe_dump(
            snapshot,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=100,
        ).rstrip()
        + f"\n{BLOCK_END}"
    )
    closing = text.find("\n---", 4)
    if closing < 0:
        raise ValueError(f"{record}: missing closing front matter delimiter")
    text = text[:closing].rstrip() + "\n" + block + text[closing:]
    record.write_text(re.sub(r"\n+\Z", "\n", text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_ids", nargs="+")
    args = parser.parse_args()
    errors = [
        error
        for batch_id in args.batch_ids
        for error in validate(batch_id, require_complete=True)
    ]
    if errors:
        raise SystemExit("\n".join(errors))
    attached = 0
    for batch_id in args.batch_ids:
        batch = json.loads((RESULTS / f"{batch_id}.json").read_text(encoding="utf-8"))
        for result in batch["results"]:
            record = ROOT / result["path"] / "system.md"
            attach(record, batch, result)
            attached += 1
    print(f"Attached validated deep research to {attached} system records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
