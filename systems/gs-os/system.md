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
---

# GS/OS

## Overview

The GS/OS reference manual documents its Apple IIGS program environment and
desktop-style applications.[^gsos-reference]

[^gsos-reference]: [GS/OS Reference, Volume 1](https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/os/gsos/gs_os_reference_vol_1.pdf)
