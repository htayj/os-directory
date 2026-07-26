---
type: Operating System
title: Amiga Unix
description: Commodore port of AT&T UNIX System V for Amiga 2500UX and 3000UX systems.
tags: [operating-system, amiga, unix, commodore]
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
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amiga Inc.], label: Amiga Unix (a.k.a. Amix), position: 10, target: https://en.wikipedia.org/wiki/Amiga_Unix, depth: 1 }
    - { section: [Proprietary, Other, Other proprietary Unix-like and POSIX-compliant], label: Amiga Unix (Amiga ports of Unix System V release 3.2 with Amiga A2500UX and SVR4 with Amiga A3000UX. Started in 1990, last version was in 1992), position: 525, target: https://en.wikipedia.org/wiki/Amiga_Unix, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: Amiga Unix, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: Amiga UNIX, kind: official, language: en, script: Latn, evidence: [release-notes], assertion_status: documented }
  - { value: Amix, kind: alias, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }
organizations:
  - { organization: Commodore, roles: [developer, vendor], evidence: [amigaunix-wiki], assertion_status: documented }
countries_of_origin: [US]
development_origins:
  - { country: US, organization: Commodore, role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: unix-workstation, primary: true, evidence: [release-notes], assertion_status: documented }
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
lifecycle_events:
  - { kind: first-public-release, value: "1990", precision: year, qualifier: exact, evidence: [amigaunix-wiki], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [release-notes], assertion_status: documented }
software_freedom_status: { value: proprietary, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization:
  - { value: unix-derived, source_term: UNIX System V Release 4, evidence: [release-notes], assertion_status: documented }
kernels:
  - { name: UNIX System V kernel, architecture: unknown, evidence: [release-notes], assertion_status: documented }
gui_status: { value: unknown, evidence: [release-notes], assertion_status: documented }
interfaces:
  - { name: UNIX shell, style: command, evidence: [release-notes], assertion_status: documented }
hardware_platforms:
  - { platform: Amiga 2500UX, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [amigaunix-wiki], assertion_status: documented }
  - { platform: Amiga 3000UX, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [amigaunix-wiki], assertion_status: documented }
architectures:
  - { value: Motorola 68000 family, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/Amiga_Unix, title: Amiga Unix, source_kind: article }
  - { id: amigaunix-wiki, resource: https://amigaunix.com/doku.php/home, title: Amiga Unix Wiki, source_kind: project-site }
  - { id: release-notes, resource: https://www.amigaunix.com/lib/exe/fetch.php/manuals%3Av2releasenotes.pdf, title: UNIX System V Release 4 release notes, source_kind: release-note }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Amiga_Unix
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Commodore-Amiga, Inc.
    country_of_origin: United States
    purpose: null
    programming_languages: null
    first_release: 1991 ; 35 years ago ( 1991 )
    latest_release: 2.1 / 1992
    last_updated: 2.1 / 1992
    development_status: Historic
    source_model: primarily closed source
    os_family: Unix ( SVR4 )
    gui: null
    platforms: Motorola 68030
    kernel_type: Monolithic
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q208305
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

Amiga Unix (also called Amix) was Commodore's System V UNIX port. The retained
project documentation identifies the 2500UX and 3000UX as its official machines;
the original release notes are supplied for the Amiga UNIX system.[^amigaunix-wiki]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Amiga_Unix).
[^amigaunix-wiki]: [Amiga Unix project documentation](https://amigaunix.com/doku.php/home).
[^release-notes]: [UNIX System V Release 4 release notes](https://www.amigaunix.com/lib/exe/fetch.php/manuals%3Av2releasenotes.pdf).
