---
type: Operating System
title: FreeBSD
description: Draft inventory record for FreeBSD.
tags: [operating-system]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-26 }
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
discovery_provenance: [{ method: english-list, language: en, native_label: "FreeBSD", source: wikipedia, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "FreeBSD", kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }]
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
sources: [{ id: wikipedia, resource: https://en.wikipedia.org/wiki/FreeBSD, title: "FreeBSD", source_kind: article }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/FreeBSD
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: The FreeBSD Project
    country_of_origin: null
    purpose: Servers , workstations , embedded systems , network firewalls
    programming_languages: C (C11)
    first_release: 1 November 1993 ; 32 years ago ( 1993-11-01 )
    latest_release: 15.1 (16 June 2026 ; 34 days ago ( 2026-06-16 ) ) [ ± ] 14.4 (10
      March 2026 ; 4 months ago ( 2026-03-10 ) ) [ ± ]
    last_updated: 15.1 (16 June 2026 ; 34 days ago ( 2026-06-16 ) ) [ ± ] 14.4 (10
      March 2026 ; 4 months ago ( 2026-03-10 ) ) [ ± ]
    development_status: Current
    source_model: Open source
    os_family: Unix-like ( BSD )
    gui: 'Unix shells : sh or tcsh (user-selectable) csh (in the past)'
    platforms: 'Tier 1: 64-bit x86 (amd64) , 64-bit ARM (originally only 32-bit x86,
      i386 , 32-bit x86 now with tier 2 support and additionally 64-bit RISC-V , 32-bit
      ARMv7, 64-bit PowerPC ; previously supported e.g. MIPS , IA-64 and SPARC )'
    kernel_type: Monolithic with dynamically loadable modules
    license: FreeBSD License , FreeBSD Documentation License
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: Bluefish
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q651027
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: dte
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q88926112
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: ee
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://man.freebsd.org/cgi/man.cgi?ee(1)
  source_kind: official-system-manual
  assertion_status: documented
- name: Epsilon
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q5383949
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: vi
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://en.wikipedia.org/wiki/Vi_(text_editor)
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
- name: Zed
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q112301707
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

## Overview

This draft record preserves a distinct operating-system identity found through the frozen source list.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/FreeBSD).
