---
type: Operating System
title: AMSDOS
description: Amstrad disk operating system for CPC computers and their disk interface.
tags: [operating-system, disk-operating-system, amstrad-cpc]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  - { field: organizations, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_status, disposition: unknown, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26, evidence: [amstrad-manual] }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, evidence: [amstrad-manual] }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: no-evidence-found, checked_at: 2026-07-26, evidence: [amstrad-manual] }
  - { field: kernels, disposition: not-applicable, checked_at: 2026-07-26, reason: "The reviewed manual describes a disk operating system extension, not a separately named kernel." }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26, reason: "The documented interface is Amstrad BASIC commands." }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amstrad], label: AMSDOS, position: 11, target: https://en.wikipedia.org/wiki/AMSDOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: AMSDOS, kind: official, language: en, script: Latn, evidence: [amstrad-manual], assertion_status: documented }
design_purposes:
  - { value: personal-computing, primary: true, source_term: "disc operating system", evidence: [amstrad-manual], assertion_status: documented }
target_audiences:
  - { value: "Amstrad CPC users with the DDI-1 disk interface", evidence: [amstrad-manual], assertion_status: documented }
interfaces:
  - { name: "AMSDOS external commands", style: command-line, modalities: [keyboard], provisioning: ROM, access: local-console, evidence: [amstrad-manual], assertion_status: documented }
platforms:
  - { value: "Amstrad CPC 464 with DDI-1; CPC disk systems", evidence: [amstrad-manual], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: amstrad-manual, resource: "https://www.cpcwiki.eu/imgs/3/3f/DDI-1_User_Manual.pdf", title: "Amstrad Disc Drive and Interface DDI-1 Manual", author: organization:amstrad, source_kind: manual }
---

# AMSDOS

## Overview

AMSDOS is the disk operating system documented as extending Amstrad BASIC on
the CPC when the DDI-1 disc interface is fitted.[^amstrad-manual]

[^amstrad-manual]: [Amstrad Disc Drive and Interface DDI-1 Manual](https://www.cpcwiki.eu/imgs/3/3f/DDI-1_User_Manual.pdf)
