---
type: Operating System
title: RISC iX
description: Acorn's UNIX System V-derived operating system for ARM workstations.
tags: [operating-system, acorn, unix, arm]
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
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, reason: The administrator guide identifies UNIX trademarks but does not establish distribution licensing. }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Acorn Computers], label: RISC iX, position: 4, target: https://en.wikipedia.org/wiki/RISC_iX, depth: 1 }
    - { section: [Proprietary, Other, Other proprietary Unix-like and POSIX-compliant], label: RISC iX – derived from BSD 4.3, by Acorn computers, for their ARM family of machines, position: 546, target: https://en.wikipedia.org/wiki/RISC_iX, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: RISC iX, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: RISC iX, kind: official, language: en, script: Latn, evidence: [acorn-guide], assertion_status: documented }
organizations:
  - { organization: Acorn Computers Limited, roles: [developer, vendor], evidence: [acorn-guide], assertion_status: documented }
countries_of_origin: [GB]
development_origins:
  - { country: GB, organization: Acorn Computers Limited, role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: workstation-computing, primary: true, evidence: [acorn-guide], assertion_status: documented }
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
lifecycle_events:
  - { kind: first-public-release, value: "1989", precision: year, qualifier: exact, evidence: [wikipedia], assertion_status: provisional }
rights_regime: { value: copyrighted, evidence: [acorn-guide], assertion_status: documented }
software_freedom_status: { value: proprietary, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization:
  - { value: unix-derived, source_term: UNIX System V, evidence: [acorn-guide], assertion_status: documented }
kernels:
  - { name: UNIX System V kernel, architecture: unknown, evidence: [acorn-guide], assertion_status: documented }
gui_status: { value: unknown, evidence: [acorn-guide], assertion_status: documented }
interfaces:
  - { name: UNIX shell, style: command, evidence: [acorn-guide], assertion_status: documented }
hardware_platforms:
  - { platform: Acorn R140/R260 workstations, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [acorn-guide], assertion_status: documented }
architectures:
  - { value: ARM, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/RISC_iX, title: RISC iX, source_kind: article }
  - { id: acorn-guide, resource: https://www.4corn.co.uk/archive/docs/Acorn%20R140%20RISC%20iX%20System%20Administrator%27s%20Guide-opt.pdf, title: Acorn RISC iX System Administrator's Guide, author: organization:acorn-computers, source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/RISC_iX
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Acorn Computers Ltd
    country_of_origin: United Kingdom; Kingdom of Great Britain; Kingdom of England;
      United Kingdom of Great Britain and Ireland
    purpose: null
    programming_languages: C , ARM assembly
    first_release: 1988 ; 38 years ago ( 1988 )
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: null
    os_family: Unix-like
    gui: Graphical user interface
    platforms: Acorn Archimedes
    kernel_type: null
    license: null
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q350
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

RISC iX is the UNIX-oriented system documented by Acorn for its R140 and R260
machines.[^acorn-guide] Its second list occurrence is preserved above.

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/RISC_iX).
[^acorn-guide]: [Acorn RISC iX System Administrator's Guide](https://www.4corn.co.uk/archive/docs/Acorn%20R140%20RISC%20iX%20System%20Administrator%27s%20Guide-opt.pdf).
