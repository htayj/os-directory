---
type: Operating System
title: Windows NT
description: Draft inventory record for Windows NT.
tags: [operating-system]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: provisional, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: organizations, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: design_purposes, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: interfaces, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: architectures, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: List of operating systems, revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, native_label: "Windows NT", source: wikipedia, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "Windows NT", kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }]
organizations: []
countries_of_origin: []
design_purposes: []
development_status: { value: unknown, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: unknown, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
interfaces: []
hardware_platforms: []
architectures: []
sources: [{ id: wikipedia, resource: https://en.wikipedia.org/wiki/Windows_NT, title: "Windows NT", source_kind: article }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Windows_NT
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Microsoft , with Dave Cutler as the lead architect
    country_of_origin: United States
    purpose: null
    programming_languages: C , Assembly language (core) C++ , Rust (user mode applications,
      kernel graphical subsystem) C++ , C# (user mode applications, shell)
    first_release: July 27, 1993 ; 32 years ago ( 1993-07-27 ) (as Windows NT 3.1
      )
    latest_release: 26H1 (10.0.28000.2525) (July 14, 2026 ; 12 days ago ( 2026-07-14
      ) ) [ ± ] 25H2 (10.0.26200.8894) (July 18, 2026 ; 8 days ago ( 2026-07-18 )
      ) [ ± ]
    last_updated: 26H1 (10.0.28000.2525) (July 14, 2026 ; 12 days ago ( 2026-07-14
      ) ) [ ± ] 25H2 (10.0.26200.8894) (July 18, 2026 ; 8 days ago ( 2026-07-18 )
      ) [ ± ]
    development_status: Current
    source_model: Closed-source Source-available (through Shared Source Initiative
      )
    os_family: null
    gui: Graphical ( Windows shell )
    platforms: x86-64 and ARM64 (and historically Intel i860 , DEC Alpha , Itanium
      , MIPS , PowerPC , IA-32 and ARM32 )
    kernel_type: Hybrid [ citation needed ]
    license: 'Depending on version, edition or customer choice: Trialware , commercial
      software , volume licensing , OEM -only, SaaS , S+S [ a ]'
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q2283
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: Metapad
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q11777663
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Notepad
  relationship: bundled-default
  interface_style: graphical
  source: https://en.wikipedia.org/wiki/Windows_Notepad
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
- name: WordPad
  relationship: bundled-default
  interface_style: graphical
  source: https://en.wikipedia.org/wiki/WordPad
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

## Overview

This draft record preserves a distinct operating-system identity found through the frozen source list.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Windows_NT).
