---
type: Operating System
title: RISC OS
description: Modular graphical operating system originally developed by Acorn for ARM computers.
tags: [operating-system, acorn, arm, graphical]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, reason: Reviewed project material establishes ongoing stewardship but not a complete license expression. }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Acorn Computers], label: RISC OS, position: 5, target: https://en.wikipedia.org/wiki/RISC_OS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: RISC OS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: RISC OS, kind: official, language: en, script: Latn, evidence: [riscos-community], assertion_status: documented }
organizations:
  - { organization: Acorn Computers Ltd., roles: [creator, developer], evidence: [riscos-community], assertion_status: documented }
  - { organization: RISC OS Open Ltd., roles: [maintainer], evidence: [riscos-community], assertion_status: documented }
countries_of_origin: [GB]
development_origins:
  - { country: GB, organization: Acorn Computers Ltd., role: origin, evidence: [riscos-community], assertion_status: documented }
design_purposes:
  - { value: desktop-computing, primary: true, evidence: [riscos-brochure], assertion_status: documented }
development_status: { value: active, evidence: [riscos-community], assertion_status: documented }
support_status: { value: active, evidence: [riscos-community], assertion_status: documented }
distribution_status: { value: active, evidence: [riscos-community], assertion_status: documented }
lifecycle_events:
  - { kind: first-public-release, value: "1989", precision: year, qualifier: exact, evidence: [riscos-brochure], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [riscos-community], assertion_status: documented }
software_freedom_status: { value: mixed, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization:
  - { value: modular, evidence: [wikipedia], assertion_status: provisional }
kernels: []
gui_status: { value: integrated, evidence: [wikipedia], assertion_status: provisional }
interfaces:
  - { name: RISC OS desktop and windowing system, style: graphical, evidence: [wikipedia], assertion_status: provisional }
hardware_platforms:
  - { platform: ARM computers, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [riscos-brochure], assertion_status: documented }
architectures:
  - { value: ARM, execution_mode: native, evidence: [riscos-brochure], assertion_status: documented }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/RISC_OS, title: RISC OS, source_kind: article }
  - { id: riscos-community, resource: https://riscoscommunity.org/about/, title: About RISC OS Community, author: organization:risc-os-community, source_kind: project-site }
  - { id: riscos-brochure, resource: https://www.riscos.com/the_archive/rol/brochure/a4.pdf, title: RISC OS fact sheet, source_kind: brochure }
---

## Overview

RISC OS is a graphical ARM operating system originally developed by Acorn and
now maintained by RISC OS Open according to the project community site.[^riscos-community]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/RISC_OS).
[^riscos-community]: [RISC OS Community](https://riscoscommunity.org/about/).
[^riscos-brochure]: [RISC OS fact sheet](https://www.riscos.com/the_archive/rol/brochure/a4.pdf).
