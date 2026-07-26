#!/usr/bin/env python3
"""Derive Terra batch status from result-file presence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
LEDGER = INVENTORY / "terra-batches.json"
RESULTS = INVENTORY / "terra-results"


def main() -> int:
    batches = json.loads(LEDGER.read_text(encoding="utf-8"))
    complete = 0
    for batch in batches:
        result = RESULTS / f"batch-{int(batch['batch']):03d}.json"
        batch["result"] = str(result.relative_to(ROOT)) if result.exists() else None
        batch["status"] = "first-pass-complete" if result.exists() else "pending"
        complete += int(result.exists())
    LEDGER.write_text(
        json.dumps(batches, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated Terra ledger: {complete}/{len(batches)} batches complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
