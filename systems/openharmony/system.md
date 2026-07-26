---
type: Operating System
title: OpenHarmony
description: Draft inventory record for OpenHarmony.
tags: [operating-system]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
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
discovery_provenance: [{ method: english-list, language: en, native_label: "OpenHarmony", source: wikipedia, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "OpenHarmony", kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }]
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
sources: [{ id: wikipedia, resource: https://en.wikipedia.org/wiki/OpenHarmony, title: "OpenHarmony", source_kind: article }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/OpenHarmony
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: OpenAtom
    country_of_origin: People's Republic of China
    purpose: Embedded systems , Smartphones , Personal computers , Aerospace
    programming_languages: C , C++ , ArkTS , JS , and others
    first_release: September 10, 2020 ; 5 years ago ( 2020-09-10 )
    latest_release: 6.1 / March 9, 2026 ; 4 months ago ( 2026-03-09 )
    last_updated: 6.1 / March 9, 2026 ; 4 months ago ( 2026-03-09 )
    development_status: Current
    source_model: Free and open source
    os_family: Distributed Operating System
    gui: HarmonyOS Design (Design System) for OpenHarmony modified ( multi-touch ,
      GUI )
    platforms: ARM , RISC-V , IA-32 , x86-64 , LoongArch
    kernel_type: Kernel-agnostic. Usually liteos_a ( micro ) or liteos_m ( monolithic
      ). Some userspace components cross-compile via a subset of pthreads and "CMSIS-RTOS"
      . APIs.
    license: Apache license
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q115490384
# END GENERATED ENWIKI INFOBOX
---

## Overview

This draft record preserves a distinct operating-system identity found through the frozen source list.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/OpenHarmony).
