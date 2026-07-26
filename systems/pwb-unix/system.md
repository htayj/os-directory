---
type: Operating System
title: PWB/UNIX
description: Bell Laboratories Programmer's Workbench Unix system.
tags: [operating-system, unix, bell-labs]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: provisional, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, "Bell Labs"], label: "PWB/UNIX", position: 73, target: "https://en.wikipedia.org/wiki/PWB/UNIX", depth: 3, parent_position: 71 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "PWB/UNIX", kind: official, language: en, script: Latn, evidence: [pwb-manual], assertion_status: documented }]
organizations: [{ organization: "Bell Telephone Laboratories", roles: [developer, publisher], evidence: [pwb-manual], assertion_status: documented }]
design_purposes: [{ value: software-development, primary: true, source_term: "Programmer's Workbench", evidence: [pwb-manual], assertion_status: documented }]
development_status: { value: discontinued, evidence: [pwb-manual], assertion_status: provisional }
interfaces: [{ name: "PWB/UNIX command interface", style: command-line, modalities: [keyboard], provisioning: bundled, access: terminal, evidence: [pwb-manual], assertion_status: provisional }]
platforms: []
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: pwb-manual, resource: "https://bitsavers.org/pdf/att/unix/PWB_UNIX/PWB_UNIX_Users_Manual_Edition_1.0_197705.pdf", title: "PWB/UNIX User's Manual, Edition 1.0", author: organization:Bell-Telephone-Laboratories, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/PWB/UNIX
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: AT&T Bell Laboratories
    country_of_origin: United States
    purpose: null
    programming_languages: C
    first_release: July 1, 1977 ; 49 years ago ( 1977-07-01 )
    latest_release: '2.0'
    last_updated: '2.0'
    development_status: Discontinued
    source_model: null
    os_family: Unix
    gui: Command-line interface ( PWB shell )
    platforms: DEC PDP-11
    kernel_type: null
    license: null
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q217365
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: ed
  relationship: bundled-default
  interface_style: line
  source: https://en.wikipedia.org/wiki/Ed_(software)
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
- name: vi
  relationship: historically-prominent
  interface_style: full-screen-text
  source: https://en.wikipedia.org/wiki/Vi_(text_editor)
  source_kind: editor-history-secondary-reference
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

# PWB/UNIX

The preserved 1977 PWB/UNIX manual identifies Bell Telephone Laboratories as
publisher and documents the named system.[^pwb-manual]

[^pwb-manual]: [PWB/UNIX User's Manual, Edition 1.0](https://bitsavers.org/pdf/att/unix/PWB_UNIX/PWB_UNIX_Users_Manual_Edition_1.0_197705.pdf)
