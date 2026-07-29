#!/usr/bin/env python3
"""Validate the machine-to-operating-system coverage audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory" / "lisp-machine-os-coverage.json"
EXPECTED_MACHINES = {
    "MIT CONS",
    "MIT CADR",
    "Symbolics Lisp-machine families",
    "Lisp Machines, Inc. Series III and Lambda",
    "Texas Instruments Explorer family",
    "Xerox D-machines and commercial Lisp workstations",
    "TAKITAC-7",
    "EVLIS",
    "ELIS and ELIS-8100/8200",
    "FACOM α",
    "LIME",
}
ALLOWED_DISPOSITIONS = {
    "cataloged",
    "cataloged-with-layering-note",
    "no-separate-operating-system-established",
    "integrated-language-environment-not-established-as-os",
    "host-operating-system-unresolved",
}


def frontmatter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])


def main() -> int:
    errors: list[str] = []
    payload = json.loads(INVENTORY.read_text(encoding="utf-8"))
    if payload.get("source", {}).get("revision") != 36748:
        errors.append("source revision must remain pinned to Gunkies revision 36748")
    entries = payload.get("entries", [])
    names = [entry.get("machine") for entry in entries]
    if len(names) != len(set(names)):
        errors.append("machine names are not unique")
    missing = EXPECTED_MACHINES - set(names)
    extra = set(names) - EXPECTED_MACHINES
    if missing:
        errors.append(f"missing machines: {sorted(missing)}")
    if extra:
        errors.append(f"unexpected machines: {sorted(extra)}")

    record_count = 0
    for entry in entries:
        machine = entry.get("machine", "<missing>")
        disposition = entry.get("disposition")
        records = entry.get("catalog_records")
        if disposition not in ALLOWED_DISPOSITIONS:
            errors.append(f"{machine}: invalid disposition {disposition}")
        if not isinstance(entry.get("associated_software"), list):
            errors.append(f"{machine}: associated_software must be a list")
        if not isinstance(entry.get("evidence"), list) or not entry["evidence"]:
            errors.append(f"{machine}: evidence must be a non-empty list")
        if not isinstance(records, list):
            errors.append(f"{machine}: catalog_records must be a list")
            continue
        if disposition.startswith("cataloged") and not records:
            errors.append(f"{machine}: cataloged disposition has no record")
        for relative in records:
            record = ROOT / relative / "system.md"
            if not record.is_file():
                errors.append(f"{machine}: missing record {relative}")
                continue
            record_count += 1
            if frontmatter(record).get("type") != "Operating System":
                errors.append(f"{machine}: {relative} is not an Operating System")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(
            f"Lisp-machine coverage validation failed with {len(errors)} error(s).",
            file=sys.stderr,
        )
        return 1
    print(
        f"Lisp-machine coverage passed: {len(entries)}/{len(EXPECTED_MACHINES)} "
        f"machine entries and {record_count} catalog mappings."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
