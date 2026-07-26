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
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: provisional, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
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
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/CP/M
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Digital Research, Inc. , Gary Kildall
    country_of_origin: United States
    purpose: null
    programming_languages: PL/M , Assembly language
    first_release: 1974 ; 52 years ago ( 1974 )
    latest_release: 3.1 / 1983 ; 43 years ago ( 1983 )
    last_updated: 3.1 / 1983 ; 43 years ago ( 1983 )
    development_status: Historical
    source_model: Originally closed source , now open source
    os_family: null
    gui: Command-line interface (CCP.COM)
    platforms: Intel 8080 , Intel 8085 , Zilog Z80 , Zilog Z8000 , Intel 8086 , Motorola
      68000
    kernel_type: Monolithic kernel
    license: Originally proprietary , now BSD -like
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q117514
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: ED
  relationship: bundled-default
  interface_style: line
  source: https://en.wikipedia.org/wiki/CP/M#Commands
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
- name: Perfect Writer
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q19903540
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

# CP/M

CP/M is retained as the Digital Research operating-system lineage, with its
numbered and platform-specific variants represented separately as releases.[^cp-m-manual]

[^cp-m-manual]: [CP/M 2.2 Alteration Guide and User Manual](https://www.gaby.de/cpm/manuals/archive/cpm22htm/)
