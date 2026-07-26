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
---

## Overview

Amiga Unix (also called Amix) was Commodore's System V UNIX port. The retained
project documentation identifies the 2500UX and 3000UX as its official machines;
the original release notes are supplied for the Amiga UNIX system.[^amigaunix-wiki]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Amiga_Unix).
[^amigaunix-wiki]: [Amiga Unix project documentation](https://amigaunix.com/doku.php/home).
[^release-notes]: [UNIX System V Release 4 release notes](https://www.amigaunix.com/lib/exe/fetch.php/manuals%3Av2releasenotes.pdf).
