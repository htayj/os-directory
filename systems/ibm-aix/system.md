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
---

## Overview

AIX is retained as IBM's independently named operating-system lineage; the
Apple-customized list context denotes a deployment, not a new identity. IBM
describes it as its enterprise UNIX operating system for Power servers.[^ibm]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/IBM_AIX).
[^ibm]: [IBM AIX on IBM Power](https://www.ibm.com/downloads/documents/us-en/12bb2fad89cd4cf7).
