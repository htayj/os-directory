---
type: Operating System
title: Acorn MOS
description: Machine Operating System firmware for Acorn's BBC Microcomputer range.
tags: [operating-system, acorn, bbc-micro, firmware]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Acorn Computers], label: MOS, position: 3, target: https://en.wikipedia.org/wiki/Acorn_MOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: MOS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: Machine Operating System, kind: official, language: en, script: Latn, evidence: [acorn-manual], assertion_status: documented }
  - { value: MOS, kind: short, language: en, script: Latn, evidence: [acorn-manual], assertion_status: documented }
organizations:
  - { organization: Acorn Computers Limited, roles: [developer, vendor], evidence: [acorn-manual], assertion_status: documented }
countries_of_origin: [GB]
development_origins:
  - { country: GB, organization: Acorn Computers Limited, role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: hardware-control, primary: true, evidence: [acorn-manual], assertion_status: documented }
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: proprietary, evidence: [wikipedia], assertion_status: provisional }
programming_languages:
  - { value: 6502 assembly language, evidence: [wikipedia], assertion_status: provisional }
system_organization:
  - { value: firmware-monitor, evidence: [acorn-manual], assertion_status: documented }
kernels: []
gui_status: { value: absent, evidence: [wikipedia], assertion_status: provisional }
interfaces:
  - { name: MOS command interface, style: command, evidence: [wikipedia], assertion_status: provisional }
hardware_platforms:
  - { platform: BBC Microcomputer range, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [acorn-manual], assertion_status: documented }
architectures:
  - { value: MOS Technology 6502, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/Acorn_MOS, title: Acorn MOS, source_kind: article }
  - { id: acorn-manual, resource: https://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Acorn_BBCSMOct85_Sec1.pdf, title: BBC Microcomputer service manual, author: organization:acorn-computers, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Acorn_MOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Acorn Computers
    country_of_origin: United Kingdom; Kingdom of Great Britain; Kingdom of England;
      United Kingdom of Great Britain and Ireland
    purpose: Personal computers
    programming_languages: 8-bit 6502 machine code (v0, v1) 65C02 machine code (v2–v5)
    first_release: Late 1981 ; 45 years ago ( 1981 )
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: Closed source
    os_family: null
    gui: Command-line interface (v3, v4, v5)
    platforms: BBC Micro , Acorn Electron , BBC Master series
    kernel_type: Monolithic
    license: null
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q350
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: no-evidence-found
  note: No editor relationship was found in the linked Wikipedia page or direct Wikidata
    text-editor platform statements; primary manuals and distribution manifests still
    require research.
text_editors: []
# END GENERATED TEXT EDITORS
---

## Overview

Acorn's contemporary service manual describes the MOS as a 16K ROM controlling
input and output devices through a defined interface.[^acorn-manual]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Acorn_MOS).
[^acorn-manual]: [Acorn BBC Microcomputer service manual](https://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Acorn_BBCSMOct85_Sec1.pdf).
