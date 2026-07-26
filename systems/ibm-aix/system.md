---
type: Operating System
title: IBM AIX
description: IBM enterprise UNIX operating system, including the Apple-customized deployment noted in the source list.
tags: [operating-system, ibm, unix, aix]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: interfaces, disposition: not-researched, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Apple], label: IBM AIX (Apple-customized), position: 36, target: https://en.wikipedia.org/wiki/IBM_AIX, depth: 2, parent_position: 35 }
discovery_provenance:
  - { method: english-list, language: en, native_label: IBM AIX, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names: [{ value: IBM AIX, kind: official, language: en, script: Latn, evidence: [ibm], assertion_status: documented }]
organizations: [{ organization: IBM, roles: [developer, vendor], evidence: [ibm], assertion_status: documented }]
countries_of_origin: []
design_purposes: [{ value: enterprise-computing, primary: true, evidence: [ibm], assertion_status: documented }]
development_status: { value: active, evidence: [ibm], assertion_status: documented }
support_status: { value: active, evidence: [ibm], assertion_status: documented }
distribution_status: { value: commercial, evidence: [ibm], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [ibm], assertion_status: documented }
software_freedom_status: { value: proprietary, evidence: [ibm], assertion_status: documented }
programming_languages: []
system_organization: [{ value: unix, evidence: [ibm], assertion_status: documented }]
kernels: []
interfaces: []
hardware_platforms: [{ platform: IBM Power servers, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [ibm], assertion_status: documented }]
architectures: [{ value: Power, execution_mode: native, evidence: [ibm], assertion_status: documented }]
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/IBM_AIX, title: IBM AIX, source_kind: article }
  - { id: ibm, resource: https://www.ibm.com/downloads/documents/us-en/12bb2fad89cd4cf7, title: IBM AIX on IBM Power, author: organization:ibm, source_kind: brochure }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/IBM_AIX
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: IBM
    country_of_origin: United States
    purpose: Workstation , Server
    programming_languages: C
    first_release: February 1986 ; 40 years ago ( 1986-02 )
    latest_release: 7.3 TL4 (7.3.4) / December 2025 ; 7 months ago ( 2025-12 )
    last_updated: 7.3 TL4 (7.3.4) / December 2025 ; 7 months ago ( 2025-12 )
    development_status: Current
    source_model: Closed source ; formerly source available
    os_family: Unix ( System V )
    gui: KornShell (ksh88), Common Desktop Environment , ( Plasma Workspaces and GNOME
      optional)
    platforms: 'Current: Power ISA Former: IBM ROMP , IBM POWER , PowerPC , x86 (
      IBM PS/2 ), System/370 , ESA/390 , IA-64 ( Itanium )'
    kernel_type: Monolithic with dynamically loadable modules
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q37156
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

AIX is retained as IBM's independently named operating-system lineage; the
Apple-customized list context denotes a deployment, not a new identity. IBM
describes it as its enterprise UNIX operating system for Power servers.[^ibm]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/IBM_AIX).
[^ibm]: [IBM AIX on IBM Power](https://www.ibm.com/downloads/documents/us-en/12bb2fad89cd4cf7).
