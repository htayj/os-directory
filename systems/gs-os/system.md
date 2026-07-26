---
type: Operating System
title: GS/OS
description: Apple IIGS operating system succeeding ProDOS 16.
tags: [operating-system, apple-iigs, graphical]
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
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Apple], label: "GS/OS", position: 20, target: https://en.wikipedia.org/wiki/Apple_GS/OS, depth: 2, parent_position: 16 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: "GS/OS", kind: official, language: en, script: Latn, evidence: [gsos-reference], assertion_status: documented }
organizations:
  - { organization: Apple, roles: [developer, publisher], evidence: [gsos-reference], assertion_status: documented }
countries_of_origin: [US]
development_origins:
  - { country: US, organization: Apple, role: origin, evidence: [gsos-reference], assertion_status: provisional }
design_purposes:
  - { value: personal-computing, primary: true, source_term: "Apple IIGS programs that run under GS/OS", evidence: [gsos-reference], assertion_status: documented }
development_status: { value: inactive, evidence: [gsos-reference], assertion_status: provisional }
interfaces:
  - { name: "Apple IIGS desktop-style application environment", style: graphical, modalities: [keyboard, pointer], provisioning: bundled, access: local-session, evidence: [gsos-reference], assertion_status: documented }
gui_status:
  - { value: first-party, evidence: [gsos-reference], assertion_status: documented }
platforms:
  - { value: "Apple IIGS", evidence: [gsos-reference], assertion_status: documented }
architectures:
  - { value: 65816, evidence: [gsos-reference], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: gsos-reference, resource: "https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/os/gsos/gs_os_reference_vol_1.pdf", title: "GS/OS Reference, Volume 1", author: organization:Apple, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Apple_GS/OS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple Computer
    country_of_origin: United States
    purpose: null
    programming_languages: null
    first_release: 1988 ; 38 years ago ( 1988 )
    latest_release: GS/OS v4.02 (System Software 6.0.1) / May 6, 1993 ; 33 years ago
      ( 1993-05-06 )
    last_updated: GS/OS v4.02 (System Software 6.0.1) / May 6, 1993 ; 33 years ago
      ( 1993-05-06 )
    development_status: Historic
    source_model: Closed source
    os_family: GS/OS
    gui: null
    platforms: null
    kernel_type: Monolithic kernel
    license: Apple Software License Agreement
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q312
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

# GS/OS

## Overview

The GS/OS reference manual documents its Apple IIGS program environment and
desktop-style applications.[^gsos-reference]

[^gsos-reference]: [GS/OS Reference, Volume 1](https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/os/gsos/gs_os_reference_vol_1.pdf)
