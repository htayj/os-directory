#!/usr/bin/env python3
"""Derive multilingual catalog-batch status from result files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MULTILINGUAL = ROOT / "inventory" / "multilingual"
LEDGER = MULTILINGUAL / "batches.json"
RESULTS = MULTILINGUAL / "results"


def main() -> int:
    batches = json.loads(LEDGER.read_text(encoding="utf-8"))
    complete = 0
    for batch in batches:
        path = RESULTS / f"batch-{int(batch['batch']):03d}.json"
        batch["result"] = str(path.relative_to(ROOT)) if path.exists() else None
        batch["status"] = "complete" if path.exists() else "pending"
        complete += int(path.exists())
    LEDGER.write_text(
        json.dumps(batches, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated multilingual ledger: {complete}/{len(batches)} complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
