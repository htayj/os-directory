#!/usr/bin/env python3
"""Resolve every frozen Gunkies category page to a catalog disposition."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory" / "gunkies"
PAGES = INVENTORY / "category-pages.json"
SEEDS = INVENTORY / "system-seeds.json"
OUTPUT = INVENTORY / "coverage.json"

NON_SYSTEM_CATEGORIES = {
    "Category:File Systems": "non-system-concept",
    "Category:OS Basics": "non-system-concept",
    "Category:OS Concepts": "non-system-concept",
    "Category:UNIX Applications": "supporting-software",
    "Category:UNIX Practical Guides": "supporting-document",
    "Category:UNIX": "supporting-document",
    "Category:OS/2": "supporting-document",
    "Category:DOS Enhancements": "supporting-software",
    "Category:Microsoft Operating Environments": "operating-environment",
    "Category:Operating Environments": "operating-environment",
    "Category:ULTRIX": "supporting-document",
    "Category:VMS Practical Guides": "supporting-document",
    "Category:VENIX Tutorials": "supporting-document",
    "Category:DEC Humor": "supporting-document",
    "Category:CSRG BSD": "supporting-document",
    "Category:PDP-11 Diagnostic Software": "diagnostic-software",
}

MANUAL_MAP: dict[str, tuple[str, list[str], str]] = {
    "AIX": ("covered-lineage-or-alias", ["systems/ibm-aix"], "Catalog title is IBM AIX."),
    "AmigaDOS": ("covered-lineage-or-alias", ["systems/amigaos"], "AmigaDOS is covered within the AmigaOS lineage."),
    "BSD": ("covered-lineage-or-alias", ["systems/berkeley-software-distribution"], "BSD family page."),
    "CP operating system": (
        "covered-lineage-or-alias",
        ["systems/cp-40", "systems/cp-67", "systems/cp-cms"],
        "The page describes the CP-40 and CP-67 virtual-machine lineage.",
    ),
    "Dell UNIX": ("covered-lineage-or-alias", ["systems/unix-system-v"], "Vendor System V distribution."),
    "Digital UNIX": ("covered-lineage-or-alias", ["systems/digital-unix"], "Catalog title is Tru64 UNIX."),
    "DOS": ("grouping-page", [], "Ambiguous DOS family/grouping rather than one operating-system identity."),
    "DOS-11": ("covered-lineage-or-alias", ["systems/batch-11-dos-11"], "Covered by the combined DEC BATCH-11/DOS-11 lineage."),
    "DOS/BATCH": ("covered-lineage-or-alias", ["systems/batch-11-dos-11"], "Covered by the combined DEC BATCH-11/DOS-11 lineage."),
    "MacMiNT": ("operating-environment", ["systems/mint"], "MiNT-based Macintosh operating environment."),
    "Mach": ("kernel-not-operating-system", [], "Mach is catalog-relevant kernel technology, not a standalone OS record here."),
    "MERT operating system": ("covered-lineage-or-alias", ["systems/mert"], "Catalog title is MERT."),
    "Microport System V": ("covered-lineage-or-alias", ["systems/system-v-at-386"], "Catalog title is Microport System V/AT 386."),
    "MicroVMS": ("covered-release", ["systems/vms"], "OpenVMS/VAX-VMS product variant."),
    "PDP-7 UNIX": ("covered-release", ["systems/research-unix"], "Early Research Unix hardware/version context."),
    "SINTRAN III": ("cataloged-system", ["systems/sintran-iii"], "Distinct SINTRAN III record."),
    "TROPIX Manual": ("supporting-document", ["systems/tropix"], "Manual for TROPIX."),
    "VM/370": ("covered-lineage-or-alias", ["systems/virtual-machine-facility-370"], "Covered by the VM lineage record."),
    "VMS": ("covered-lineage-or-alias", ["systems/vms"], "Catalog title is OpenVMS."),
    "Windows ME": ("covered-release", ["systems/windows"], "Windows lineage release."),
}

SUPPORTING_EXACT: dict[str, tuple[str, list[str], str]] = {
    "A UNIX™ Operating System for the DEC VAX-11/780 Computer": ("supporting-document", ["systems/unix-32v"], "Historical paper."),
    "BSD Daemon": ("supporting-software", ["systems/berkeley-software-distribution"], "Mascot, not an operating system."),
    "BSD Fast File System": ("non-system-concept", ["systems/berkeley-software-distribution"], "File system."),
    "BSD on VAX": ("supporting-document", ["systems/berkeley-software-distribution"], "Historical context page."),
    "Eedsp": ("hardware-or-site", ["systems/berkeley-software-distribution"], "A VAX host/site, not an operating system."),
    "ITS Internals Manual": ("supporting-document", ["systems/incompatible-timesharing-system"], "ITS manual."),
    "List of SITS system calls": ("supporting-document", ["systems/small-incompatible-timesharing-system"], "SITS interface list."),
    "Microsoft Windows-386 Being Delivered With Compaq 80386-Based PCs Through Dec. 31, 1987": ("supporting-document", ["systems/windows"], "Contemporary announcement."),
    "RTEM-11 - RT-11 Virtualization in 1982": ("supporting-document", ["systems/rt-11"], "Article about RT-11 virtualization."),
    "Running ITS (the Incompatible Timesharing System) on the KL-10": ("supporting-document", ["systems/incompatible-timesharing-system"], "ITS operating guide."),
    "Text terminals supported by WAITS": ("supporting-document", ["systems/waits"], "WAITS terminal inventory."),
    "The VMS-MicroVMS Merge": ("supporting-document", ["systems/vms"], "Product-line history."),
    "UNIX* System V and 4.1C BSD": ("supporting-document", ["systems/unix-system-v", "systems/berkeley-software-distribution"], "Comparative document."),
    "VENIX Graphics on the Professional": ("supporting-document", ["systems/pro-venix"], "PRO/VENIX graphics guide."),
    "Versions of important ITS software": ("supporting-document", ["systems/incompatible-timesharing-system"], "ITS software-version inventory."),
    "VMS Software, Inc.": ("organization", [], "Company page, not the VMS operating system."),
    "WAITS system directories": ("supporting-document", ["systems/waits"], "WAITS directory inventory."),
}


def normalize(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", "", folded)


def record_names() -> dict[str, list[str]]:
    result: dict[str, set[str]] = {}
    for path in sorted((ROOT / "systems").glob("*/system.md")):
        data = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        names = [data.get("title", "")]
        names.extend(
            entry.get("value", "")
            for entry in data.get("names", [])
            if isinstance(entry, dict)
        )
        for name in names:
            if name:
                result.setdefault(normalize(str(name)), set()).add(
                    path.parent.relative_to(ROOT).as_posix()
                )
    return {key: sorted(value) for key, value in result.items()}


def version_mapping(title: str) -> tuple[str, list[str], str] | None:
    mappings = [
        (r"^(2\.(9|10|11)BSD|3BSD|4BSD|4\.[1234]\s?BSD|4\.3 BSD.*|4\.4BSD.*|Net/[12])$", "systems/berkeley-software-distribution", "BSD release or distribution"),
        (r"^386 ?BSD(?:\s.*)?$", "systems/386bsd", "386BSD release, patch level, or announcement"),
        (r"^Darwin \d", "systems/darwin", "Darwin release or release notes"),
        (r"^FreeBSD \d", "systems/freebsd", "FreeBSD release or announcement"),
        (r"^NetBSD \d", "systems/netbsd", "NetBSD release, announcement, or build notes"),
        (r"^Linux \d", "systems/linux", "Linux kernel release"),
        (r"^ITS 138$", "systems/incompatible-timesharing-system", "ITS version"),
        (r"^(UNIX (First|Second|Third|Fourth|Fifth|Sixth) Edition|Unix Seventh Edition|Unix (Eighth|Ninth|Tenth) Edition)$", "systems/research-unix", "Research Unix edition"),
        (r"^(UNIX System III|UNIX System IV|Unix SYSVr[234]|USG UNIX)$", "systems/unix-system-v", "AT&T/USG Unix lineage version"),
        (r"^Windows (1\.0|2\.0|3\.[012]|95|98)(?:\s.*)?$", "systems/windows", "Microsoft Windows release or prerelease"),
        (r"^Microsoft Windows v3\.0", "systems/windows", "Microsoft Windows prerelease"),
        (r"^Windows NT 3\.[15]", "systems/windows-nt", "Windows NT prerelease, SDK, or compatibility list"),
        (r"^Mac Minix ", "systems/minix", "MINIX Macintosh port/version"),
    ]
    for pattern, record, note in mappings:
        if re.match(pattern, title, re.IGNORECASE):
            disposition = (
                "supporting-document"
                if any(
                    word in title.casefold()
                    for word in ("announcement", "release notes", "building notes", "hcl", "sdk")
                )
                else "covered-release"
            )
            return disposition, [record], note
    return None


def support_mapping(title: str) -> tuple[str, list[str], str] | None:
    lower = title.casefold()
    target = []
    if "ultrix" in lower:
        target = ["systems/ultrix"]
    elif "unix sixth edition" in lower or "unix v6" in lower:
        target = ["systems/research-unix"]
    elif "unix seventh edition" in lower or "seventh edition" in lower:
        target = ["systems/research-unix"]
    elif "unix/32v" in lower:
        target = ["systems/unix-32v"]
    elif "386bsd" in lower:
        target = ["systems/386bsd"]
    elif "2.9 bsd" in lower or "berkeley software tape" in lower:
        target = ["systems/berkeley-software-distribution"]
    elif "freebsd" in lower:
        target = ["systems/freebsd"]
    elif "minix" in lower:
        target = ["systems/minix"]
    if target and any(
        marker in lower
        for marker in (
            "advanced installation",
            "booting ",
            "installing ",
            "repairing ",
            "running ",
            "setting up ",
            "upgrading ",
            "building notes",
            "management services",
            "remote console",
            "remote installation",
        )
    ):
        return "supporting-document", target, "Installation, operation, or maintenance page."
    return None


def disposition(
    page: dict[str, Any],
    names: dict[str, list[str]],
    seed_pages: dict[str, str],
) -> tuple[str, list[str], str]:
    title = page["title"]
    if title in SUPPORTING_EXACT:
        return SUPPORTING_EXACT[title]
    if title in MANUAL_MAP:
        return MANUAL_MAP[title]
    if title in seed_pages:
        return "cataloged-system", [f"systems/{seed_pages[title]}"], "Curated Gunkies-discovered system record."
    version = version_mapping(title)
    if version:
        return version
    support = support_mapping(title)
    if support:
        return support
    matches = names.get(normalize(title), [])
    if matches:
        return "cataloged-system", matches, "Exact normalized catalog name or alias."
    for category, category_disposition in NON_SYSTEM_CATEGORIES.items():
        if category in page["categories"]:
            return category_disposition, [], f"Page belongs to {category}."
    if title in {"286 DOS-Extender", "386 DOS-Extender", "DOS extender", "DOS Protected Mode Interface", "DOS/4GW", "TSR", "Virtual DOS Machine", "Win32s", "WinG"}:
        return "supporting-software", [], "DOS or Windows support technology, not an operating system."
    if title == "QuickWin":
        return "operating-environment", [], "Application execution environment, not an operating system."
    if title == "Operating environment":
        return "non-system-concept", [], "Concept page."
    raise ValueError(f"Unresolved Gunkies page: {title}")


def main() -> int:
    pages = json.loads(PAGES.read_text(encoding="utf-8"))
    seeds = json.loads(SEEDS.read_text(encoding="utf-8"))
    seed_pages = {seed["source_page"]: seed["slug"] for seed in seeds}
    names = record_names()
    entries = []
    for page in pages:
        page_disposition, records, note = disposition(page, names, seed_pages)
        entries.append(
            {
                "page_title": page["title"],
                "page_id": page["page_id"],
                "url": page["url"],
                "revision": page["revision"],
                "categories": page["categories"],
                "disposition": page_disposition,
                "catalog_records": records,
                "note": note,
            }
        )
    payload = {
        "schema_version": "0.1",
        "as_of": "2026-07-29",
        "source": "inventory/gunkies/category-source.json",
        "scope_note": (
            "Every recursively discovered category page has a disposition. "
            "Category membership alone does not establish an operating-system identity."
        ),
        "entry_count": len(entries),
        "entries": entries,
    }
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["disposition"]] = counts.get(entry["disposition"], 0) + 1
    print(f"Resolved {len(entries)} Gunkies pages: {json.dumps(counts, sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
