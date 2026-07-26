---
type: Operating System
title: RSTS/E
description: DEC multiuser time-sharing operating system for PDP-11 computers.
tags: [operating-system, dec, pdp-11, timesharing]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: provisional, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: interfaces, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: architectures, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: List of operating systems, revision: 1365063001, occurrences: [{ section: [Proprietary, "Digital Equipment Corporation , Compaq , Hewlett-Packard , Hewlett Packard Enterprise"], label: "RSTS/E – multi-user time-sharing OS for PDP-11s", position: 167, target: https://en.wikipedia.org/wiki/RSTS/E, depth: 1 }] }
discovery_provenance: [{ method: english-list, language: en, native_label: RSTS/E, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: RSTS/E, kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }]
organizations: [{ organization: Digital Equipment Corporation, roles: [developer, vendor], evidence: [wikipedia], assertion_status: provisional }]
countries_of_origin: []
design_purposes: [{ value: timesharing, primary: true, evidence: [wikipedia], assertion_status: provisional }]
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
interfaces: []
hardware_platforms: [{ platform: PDP-11, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }]
architectures: []
sources: [{ id: wikipedia, resource: https://en.wikipedia.org/wiki/RSTS/E, title: RSTS/E, source_kind: article }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/RSTS/E
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Digital Equipment Corporation , later Mentec
    country_of_origin: United States
    purpose: null
    programming_languages: MACRO-11 assembly language , BASIC-PLUS -2, DCL
    first_release: 1970 ; 56 years ago ( 1970 )
    latest_release: RSTS V10.1 / 1992 ; 34 years ago ( 1992 )
    last_updated: RSTS V10.1 / 1992 ; 34 years ago ( 1992 )
    development_status: No development, still available
    source_model: Closed source
    os_family: null
    gui: 'Command-line interface : DCL (Digital Command Language)'
    platforms: PDP-11
    kernel_type: Time-sharing operating systems
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q690079
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: EDT
  relationship: first-party
  interface_style: full-screen-text
  source: https://en.wikipedia.org/wiki/EDT_(text_editor)
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

## Overview

RSTS/E is retained as DEC's named PDP-11 time-sharing system.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/RSTS/E).
