---
type: Operating System
title: A/UX
description: Apple Unix operating-system distribution for Macintosh computers.
tags: [operating-system, unix, macintosh]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, Apple], label: "A/UX (UNIX System V with BSD extensions)", position: 28, target: "https://en.wikipedia.org/wiki/A/UX", depth: 2, parent_position: 26 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "A/UX", kind: official, language: en, script: Latn, evidence: [aux-manual], assertion_status: documented }]
organizations: [{ organization: Apple, roles: [developer, publisher], evidence: [aux-manual], assertion_status: documented }]
design_purposes: [{ value: software-development, primary: true, source_term: "A/UX Programming Languages and Tools", evidence: [aux-manual], assertion_status: documented }]
development_status: { value: discontinued, evidence: [aux-manual], assertion_status: provisional }
system_organization: [{ value: distinct-kernel, source_term: UNIX, evidence: [aux-manual], assertion_status: provisional }]
interfaces: [{ name: "A/UX command interface", style: command-line, modalities: [keyboard], provisioning: bundled, access: local-console, evidence: [aux-manual], assertion_status: documented }]
platforms: [{ value: Macintosh, evidence: [aux-manual], assertion_status: provisional }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: aux-manual, resource: "https://ftpmirror.your.org/pub/misc/bitsavers/pdf/apple/mac/a_ux/aux_1.0/AUX_1.0_Programming_Languages_and_Tools_Volume_2_1987.pdf", title: "A/UX Programming Languages and Tools", author: organization:Apple, source_kind: manual }
---

# A/UX

Apple's A/UX manual documents its command-oriented Unix environment and development tools.[^aux-manual]

[^aux-manual]: [A/UX Programming Languages and Tools](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/apple/mac/a_ux/aux_1.0/AUX_1.0_Programming_Languages_and_Tools_Volume_2_1987.pdf)
