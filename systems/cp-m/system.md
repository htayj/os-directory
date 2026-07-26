---
type: Operating System
title: CP/M
description: Digital Research operating-system lineage for 8080, 8085, and Z80 systems.
tags: [operating-system, 8-bit, digital-research]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, "Digital Research, Inc."], label: "CP/M", position: 114, target: "https://en.wikipedia.org/wiki/CP/M", depth: 1 }, { section: [Proprietary, "Digital Research, Inc."], label: "CP/M for Intel 8080/8085 and Zilog Z80", position: 115, target: "https://en.wikipedia.org/wiki/CP/M", depth: 2, parent_position: 114 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "CP/M", kind: official, language: en, script: Latn, evidence: [cp-m-manual], assertion_status: documented }]
organizations: [{ organization: "Digital Research", roles: [developer, publisher], evidence: [cp-m-manual], assertion_status: documented }]
design_purposes: [{ value: personal-computing, primary: true, source_term: "Control Program for Microcomputers", evidence: [cp-m-manual], assertion_status: documented }]
development_status: { value: discontinued, evidence: [cp-m-manual], assertion_status: provisional }
interfaces: [{ name: "CP/M command console", style: command-line, modalities: [keyboard], provisioning: bundled, access: terminal, evidence: [cp-m-manual], assertion_status: documented }]
platforms: [{ value: "Intel 8080, Intel 8085, Zilog Z80", evidence: [cp-m-manual], assertion_status: documented }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: cp-m-manual, resource: "https://www.gaby.de/cpm/manuals/archive/cpm22htm/", title: "CP/M 2.2 Alteration Guide and User Manual", author: organization:Digital-Research, source_kind: manual }
---

# CP/M

CP/M is retained as the Digital Research operating-system lineage, with its
numbered and platform-specific variants represented separately as releases.[^cp-m-manual]

[^cp-m-manual]: [CP/M 2.2 Alteration Guide and User Manual](https://www.gaby.de/cpm/manuals/archive/cpm22htm/)
