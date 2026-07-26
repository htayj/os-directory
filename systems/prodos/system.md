---
type: Operating System
title: ProDOS
description: Apple II operating-system lineage comprising 8-bit and 16-bit streams.
tags: [operating-system, apple-ii, disk-operating-system]
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
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Apple], label: ProDOS, position: 19, target: https://en.wikipedia.org/wiki/Apple_ProDOS, depth: 2, parent_position: 16 }
    - { section: ["Disk operating systems (DOS)"], label: "ProDOS (operating system for the Apple II series computers)", position: 684, target: https://en.wikipedia.org/wiki/Apple_ProDOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: ProDOS, kind: official, language: en, script: Latn, evidence: [apple-iigs-reference], assertion_status: documented }
  - { value: "ProDOS 8", kind: former, language: en, script: Latn, evidence: [apple-iigs-reference], assertion_status: documented }
design_purposes:
  - { value: personal-computing, primary: true, source_term: "operating system", evidence: [apple-iigs-reference], assertion_status: documented }
development_status: { value: unknown, evidence: [apple-iigs-reference], assertion_status: unknown }
interfaces:
  - { name: "ProDOS system interface", style: command-line, modalities: [keyboard], provisioning: bundled, access: local-console, evidence: [apple-iigs-reference], assertion_status: provisional }
platforms:
  - { value: "8-bit Apple II computers", evidence: [apple-iigs-reference], assertion_status: documented }
architectures:
  - { value: "6502-family", evidence: [apple-iigs-reference], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: apple-iigs-reference, resource: "https://apple2.gs/downloads/library/Apple%20IIGS%20Toolbox%20Reference%20Volume%201.pdf", title: "Apple IIGS Toolbox Reference", author: organization:Apple, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Apple_ProDOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple Computer
    country_of_origin: United States
    purpose: null
    programming_languages: Assembly language
    first_release: October 1983 ; 42 years ago ( 1983-10 )
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: Closed source (but version 1.7)
    os_family: SOS
    gui: primarily text user interface
    platforms: Apple II
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

# ProDOS

## Overview

Apple documentation calls ProDOS 8 the standard operating system for most
8-bit Apple II computers and distinguishes it from ProDOS 16.[^apple-iigs-reference]

[^apple-iigs-reference]: [Apple IIGS Toolbox Reference](https://apple2.gs/downloads/library/Apple%20IIGS%20Toolbox%20Reference%20Volume%201.pdf)
