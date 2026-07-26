---
type: Operating System
title: Arthur
description: Acorn's short-lived ROM operating system for early ARM Archimedes computers.
tags: [operating-system, acorn, arm]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, reason: Reviewed catalog evidence does not state a license. }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Acorn Computers], label: Arthur, position: 1, target: https://en.wikipedia.org/wiki/Arthur_(operating_system), depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: Arthur, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: Arthur, kind: official, language: en, script: Latn, evidence: [chm], assertion_status: documented }
organizations:
  - { organization: Acorn Computers Ltd., roles: [developer, vendor], evidence: [chm], assertion_status: documented }
countries_of_origin: [GB]
development_origins:
  - { country: GB, organization: Acorn Computers Ltd., role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: desktop-computing, primary: true, evidence: [chm], assertion_status: documented }
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
lifecycle_events:
  - { kind: first-public-release, value: "1987", precision: year, qualifier: exact, evidence: [chm], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: proprietary, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
gui_status: { value: present, evidence: [wikipedia], assertion_status: provisional }
interfaces: []
hardware_platforms:
  - { platform: Acorn Archimedes, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [chm], assertion_status: documented }
architectures:
  - { value: ARM, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/Arthur_(operating_system), title: Arthur (operating system), source_kind: article }
  - { id: chm, resource: https://www.computerhistory.org/collections/catalog/102696284, title: Operating system ROM chip for Acorn Archimedes, author: organization:computer-history-museum, source_kind: catalog }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Arthur_(operating_system)
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: null
    country_of_origin: null
    purpose: null
    programming_languages: null
    first_release: null
    latest_release: null
    last_updated: null
    development_status: null
    source_model: null
    os_family: null
    gui: null
    platforms: null
    kernel_type: null
    license: null
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

Arthur was Acorn's 1987 ROM operating system for the Archimedes. The Computer
History Museum catalogs an Acorn-made 1987 ROM identified as “ARTHUR 1.1 ROM
1”.[^chm] Later RISC OS is related but remains separately cataloged because the
source list names Arthur independently.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Arthur_(operating_system)).
[^chm]: [Computer History Museum catalog](https://www.computerhistory.org/collections/catalog/102696284).
