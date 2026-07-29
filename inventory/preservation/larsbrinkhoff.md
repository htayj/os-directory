---
type: Inventory
title: Lars Brinkhoff preservation-source audit
description: Curated operating-system preservation projects selected after screening every public repository on Lars Brinkhoff's GitHub profile.
tags: [inventory, preservation, operating-system, source-history]
status: active
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
---

# Lars Brinkhoff preservation-source audit

Snapshot date: **2026-07-29**

All 208 public repositories visible on
[Lars Brinkhoff's GitHub profile](https://github.com/larsbrinkhoff) were
screened by repository metadata. Twenty-seven projects were then selected for
README, repository-tree, or contributor review because they preserve operating
systems, source histories, media, documentation, editors, networking, or the
tools needed to recover and run them.

This is a preservation-source inventory, not an authorship claim. The
machine-readable inventory distinguishes:

* `profile-owned` repositories;
* `profile-fork` repositories, which may be useful without being Lars's
  original work; and
* `external-project-with-verified-contribution` repositories, for which the
  GitHub contributor endpoint showed a nonzero contribution count at the
  snapshot date.

## High-value system clusters

| Cluster | Projects | Catalog use |
| --- | --- | --- |
| ITS | `PDP-10/its`, `its-history`, `ooits`, `its-manual`, `its-archives`, `its-interviews`, `its-book` | Runnable reconstruction, early-version recovery, source history, manuals, archives, and oral history |
| Small ITS / SITS | `pdp11/sits`, `mit-logo-and-sits-raw-files` | Newly cataloged PDP-11/45 system, runnable SIMH installation, raw files, and TINTE editor evidence |
| TENEX and TOPS | `build-tenex`, `tops20-v2`, `pdp10-periodic-build`, `pdp10-its-disassembler` | Build attempts, release media, periodic reconstruction, and file/tape recovery |
| BSD and early Unix | `2bsd`, `prebuilt-emulator-images-with-interesting-software-installed`, `pdp7-unix` | Distribution tapes, runnable images, and an explicitly labeled profile fork |
| DTSS | `dtss-backup` | Newly cataloged Dartmouth system and a multisite source/documentation aggregation |
| Lisp machines and editor history | `emacs-history`, `lmfs-tape` | Editor lineage and LMFS extraction; individual tapes still require implementation/version identification |
| VMS | `vmsbackup` | An explicitly labeled backup-tool fork |
| Cross-system recovery | `tape-lab`, `tools-for-unusual-tape-formats`, `image-tape`, `open-simh` | Media recovery and emulation infrastructure; not treated as evidence for a single OS |

The external [`PDP-10/its`](https://github.com/PDP-10/its) project reported
1,435 contributions by `larsbrinkhoff`, while
[`pdp11/sits`](https://github.com/pdp11/sits) reported 5. Those counts are an
API snapshot, not a timeless measure of authorship or project ownership.

See [larsbrinkhoff.json](larsbrinkhoff.json) for the complete selected-project
list, artifact classifications, notes, and catalog-system mappings.
