---
type: Operating System
title: SymbOS
description: Freeware Z80-based multitasking operating system for several 8-bit computer families.
tags: [operating-system, z80, multitasking, graphical]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: organizations, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amstrad], label: SymbOS, position: 15, target: https://en.wikipedia.org/wiki/SymbOS, depth: 1 }
    - { section: ["Generic, commodity, and other"], label: "SymbOS (GUI based multitasking operating system for Z80 computers)", position: 731, target: https://en.wikipedia.org/wiki/SymbOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: SymbOS, kind: official, language: en, script: Latn, evidence: [symbos-site], assertion_status: documented }
design_purposes:
  - { value: personal-computing, primary: true, source_term: "Z80 based multitasking operating system", evidence: [symbos-manual], assertion_status: documented }
development_status: { value: active, evidence: [symbos-site], assertion_status: documented }
distribution_status: { value: public, evidence: [symbos-site], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [symbos-site], assertion_status: provisional }
software_freedom_status: { value: no-known-license, note: "The official site calls it freeware; that alone does not establish a license.", evidence: [symbos-site], assertion_status: documented }
licenses: []
system_organization:
  - { value: unknown, source_term: "multitasking operating system", evidence: [symbos-manual], assertion_status: documented }
gui_status:
  - { value: first-party, evidence: [symbos-manual], assertion_status: documented }
interfaces:
  - { name: SymbOS graphical desktop, style: graphical, modalities: [keyboard, pointer], provisioning: bundled, access: local-session, evidence: [symbos-manual], assertion_status: documented }
platforms:
  - { value: "Amstrad CPC, MSX, Amstrad PCW, Enterprise, Amstrad NC, ZX Spectrum Next", evidence: [symbos-site], assertion_status: documented }
architectures:
  - { value: Z80, evidence: [symbos-manual], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: symbos-site, resource: "https://symbos.org/download.htm", title: "SymbOS downloads", author: organization:SymbiosiS, source_kind: project-site }
  - { id: symbos-manual, resource: "https://www.symbos.org/download/20170830-V30/symbos-manual.pdf", title: "SymbOS 3.0 Installation and User Manual", author: organization:SymbiosiS, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/SymbOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: SymbiosiS
    country_of_origin: null
    purpose: null
    programming_languages: Assembly language ( Zilog Z80 )
    first_release: 1 May 2006 ; 20 years ago ( 2006-05-01 )
    latest_release: 4.0 / 31 January 2025 ; 17 months ago ( 2025-01-31 )
    last_updated: 4.0 / 31 January 2025 ; 17 months ago ( 2025-01-31 )
    development_status: Current
    source_model: Freeware
    os_family: null
    gui: Graphical user interface
    platforms: Amstrad CPC , MSX , Amstrad PCW , Amstrad NC100 , Amstrad NC200 , Enterprise
      64/128 , ZX Spectrum Next , Virtual Machine
    kernel_type: Microkernel
    license: null
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

# SymbOS

## Overview

The official project distributes SymbOS packages and documentation for several
Z80-based computer families.[^symbos-site]

[^symbos-site]: [SymbOS downloads](https://symbos.org/download.htm)
