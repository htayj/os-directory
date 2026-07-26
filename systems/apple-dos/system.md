---
type: Operating System
title: Apple DOS
description: Apple disk operating-system lineage for Apple II computers.
tags: [operating-system, disk-operating-system, apple-ii]
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
  - { field: development_status, disposition: unknown, checked_at: 2026-07-26 }
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
    - { section: [Proprietary, Apple], label: "Apple DOS", position: 17, target: https://en.wikipedia.org/wiki/Apple_DOS, depth: 2, parent_position: 16 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: "Apple DOS", kind: official, language: en, script: Latn, evidence: [apple-dos-manual], assertion_status: documented }
design_purposes:
  - { value: personal-computing, primary: true, source_term: "DOS", evidence: [apple-dos-manual], assertion_status: documented }
interfaces:
  - { name: "Apple DOS commands", style: command-line, modalities: [keyboard], provisioning: bundled, access: local-console, evidence: [apple-dos-manual], assertion_status: documented }
platforms:
  - { value: "Apple II family", evidence: [apple-dos-manual], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: apple-dos-manual, resource: "https://www.applelogic.org/UserManuals.html", title: "Apple II DOS Manual collection", author: organization:Apple, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Apple_DOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple Computer
    country_of_origin: United States
    purpose: null
    programming_languages: Assembly
    first_release: 1978 ; 48 years ago ( 1978 )
    latest_release: 3.3 / 1980 ; 46 years ago ( 1980 )
    last_updated: 3.3 / 1980 ; 46 years ago ( 1980 )
    development_status: Discontinued
    source_model: Closed source
    os_family: Apple DOS
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

# Apple DOS

## Overview

Apple DOS is retained as a distinct Apple II disk-operating-system lineage;
the contemporary Apple DOS manual is preserved in the cited manual collection.[^apple-dos-manual]

[^apple-dos-manual]: [Apple II DOS Manual collection](https://www.applelogic.org/UserManuals.html)
