---
type: Operating System
title: Inferno
description: Distributed operating-system lineage derived from Plan 9.
tags: [operating-system, distributed, plan-9]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: provisional, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, "Bell Labs"], label: Inferno, position: 86, target: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", depth: 1 }, { section: [Research, "Unix or Unix-like"], label: Inferno, position: 617, target: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", depth: 2 }, { section: ["Network operating systems"], label: Inferno, position: 704, target: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", depth: 2 }, { section: [Embedded, "Mobile operating systems"], label: Inferno, position: 796, target: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", depth: 1 }, { section: [Embedded, Routers], label: Inferno, position: 831, target: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", depth: 1 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: Inferno, kind: official, language: en, script: Latn, evidence: [inferno-discovery], assertion_status: provisional }]
design_purposes: [{ value: distributed-computing, primary: true, evidence: [inferno-discovery], assertion_status: provisional }]
development_status: { value: unknown, evidence: [inferno-discovery], assertion_status: unknown }
system_traits: [{ value: distributed, evidence: [inferno-discovery], assertion_status: provisional }]
system_organization: [{ value: distributed-services, evidence: [inferno-discovery], assertion_status: provisional }]
interfaces: []
platforms: []
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: inferno-discovery, resource: "https://en.wikipedia.org/wiki/Inferno_(operating_system)", title: "Inferno (operating system)", source_kind: article }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Inferno_(operating_system)
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Bell Labs , Vita Nuova Holdings
    country_of_origin: United States; United Kingdom; Canada
    purpose: null
    programming_languages: C , Limbo
    first_release: 1996 ; 30 years ago ( 1996 )
    latest_release: 4th Edition / March 28, 2015 ; 11 years ago ( 2015-03-28 )
    last_updated: 4th Edition / March 28, 2015 ; 11 years ago ( 2015-03-28 )
    development_status: Discontinued
    source_model: Open-source
    os_family: null
    gui: null
    platforms: ARM , PA-RISC , MIPS , PowerPC , SPARC , x86
    kernel_type: Virtual machine ( Dis )
    license: '2021: MIT 2005: Dual [ a ] 2003: Dual [ b ] 2000: Inferno [ c ] Original:
      Proprietary'
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q967165
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
  relationship: ported
  interface_style: graphical
  source: https://9p.io/sys/doc/acme/acme.html
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

# Inferno

Inferno is retained as a separately named distributed system; stronger primary evidence is pending.
