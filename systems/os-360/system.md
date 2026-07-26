---
type: Operating System
title: OS/360
description: Draft inventory record for OS/360.
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
discovery_provenance: [{ method: english-list, language: en, native_label: "OS/360", source: wikipedia, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "OS/360", kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }]
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
sources: [{ id: wikipedia, resource: https://en.wikipedia.org/wiki/OS/360, title: "OS/360", source_kind: article }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/OS/360
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: IBM
    country_of_origin: null
    purpose: IBM mainframe computers
    programming_languages: Assembly language , Basic Systems Language (BSL)
    first_release: March 31, 1966 ; 60 years ago ( 1966-03-31 )
    latest_release: 21.8 / August 1972 ; 53 years ago ( 1972-08 )
    last_updated: 21.8 / August 1972 ; 53 years ago ( 1972-08 )
    development_status: null
    source_model: null
    os_family: OS/360 and successors
    gui: null
    platforms: S/360 , S/370
    kernel_type: N/A
    license: Public domain
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: TSO EDIT
  relationship: first-party
  interface_style: line
  source: https://www.ibm.com/docs/en/zos/3.2.0?topic=edit-using-editor
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
  note: Applies to OS/360 configurations with TSO.
# END GENERATED TEXT EDITORS
---

## Overview

This draft record preserves a distinct operating-system identity found through the frozen source list.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/OS/360).
