---
type: Operating System
title: Plan 9 from Bell Labs
description: Bell Laboratories distributed operating system.
tags: [operating-system, distributed, bell-labs]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, "Bell Labs"], label: "Plan 9 from Bell Labs", position: 85, target: "https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs", depth: 1 }, { section: [Research, "Unix or Unix-like"], label: "Plan 9 from Bell Labs", position: 616, target: "https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs", depth: 1 }, { section: ["Network operating systems"], label: "Plan 9", position: 703, target: "https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs", depth: 1 }, { section: [Embedded, "Mobile operating systems"], label: "Plan 9 from Bell Labs", position: 804, target: "https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs", depth: 1 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "Plan 9 from Bell Labs", kind: official, language: en, script: Latn, evidence: [plan9-site], assertion_status: documented }]
organizations: [{ organization: "Bell Laboratories", roles: [developer], evidence: [plan9-site], assertion_status: documented }]
design_purposes: [{ value: distributed-computing, primary: true, evidence: [plan9-site], assertion_status: documented }]
development_status: { value: inactive, evidence: [plan9-site], assertion_status: provisional }
system_traits: [{ value: distributed, evidence: [plan9-site], assertion_status: documented }]
system_organization: [{ value: distributed-services, evidence: [plan9-site], assertion_status: provisional }]
interfaces: [{ name: "Plan 9 command interface", style: command-line, modalities: [keyboard], provisioning: bundled, access: terminal, evidence: [plan9-site], assertion_status: provisional }]
platforms: []
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: plan9-site, resource: "https://9p.io/plan9/", title: "Plan 9 from Bell Labs", source_kind: project-site }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Plan 9 Foundation, succeeding Bell Labs
    country_of_origin: United States
    purpose: Operating systems research, networked environments, general-purpose use
    programming_languages: Dialect of ANSI C
    first_release: 1992 ; 34 years ago ( 1992 ) (universities) / 1995 ; 31 years ago
      ( 1995 ) (general public)
    latest_release: null
    last_updated: null
    development_status: Current
    source_model: Open source
    os_family: null
    gui: rio / rc
    platforms: 'x86 / Vx32 , x86-64 , ARM , RISC-V , MIPS Historical: DEC Alpha ,
      SPARC , PowerPC'
    kernel_type: Monolithic
    license: '2021: MIT 2014: GPL-2.0-only 2002: LPL-1.02 2000: Plan 9 OSL'
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q217365
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: acme
  relationship: first-party
  interface_style: graphical
  source: https://9p.io/sys/doc/acme/acme.html
  source_kind: contemporary-system-paper
  assertion_status: documented
- name: sam
  relationship: first-party
  interface_style: graphical
  source: https://9p.io/sys/doc/sam/sam.html
  source_kind: contemporary-system-paper
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Plan 9 from Bell Labs

The Plan 9 project site identifies the system as a Bell Labs distributed OS.[^plan9-site]

[^plan9-site]: [Plan 9 from Bell Labs](https://9p.io/plan9/)
