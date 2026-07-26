---
type: Operating System
title: ARX
description: Unreleased Acorn graphical operating-system project for ARM Archimedes computers.
tags: [operating-system, acorn, arm, unreleased]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  - { field: lifecycle_events, disposition: no-evidence-found, checked_at: 2026-07-26, reason: No primary dated release record located; the project was unreleased. }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Acorn Computers], label: ARX, position: 2, target: https://en.wikipedia.org/wiki/ARX_(operating_system), depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: ARX, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: ARX, kind: official, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }
organizations:
  - { organization: Acorn Computers Ltd., roles: [developer], evidence: [wikipedia], assertion_status: provisional }
countries_of_origin: [GB]
development_origins:
  - { country: US, place: Palo Alto, organization: Acorn Research Centre, role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: office-computing, primary: true, evidence: [wikipedia], assertion_status: provisional }
development_status: { value: ended, evidence: [wikipedia], assertion_status: provisional }
distribution_status: { value: unreleased, evidence: [wikipedia], assertion_status: provisional }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: proprietary, evidence: [wikipedia], assertion_status: provisional }
programming_languages:
  - { value: Modula-2+, evidence: [wikipedia], assertion_status: provisional }
system_organization:
  - { value: microkernel, evidence: [wikipedia], assertion_status: provisional }
kernels:
  - { name: ARX microkernel, architecture: microkernel, evidence: [wikipedia], assertion_status: provisional }
gui_status: { value: present, evidence: [wikipedia], assertion_status: provisional }
interfaces:
  - { name: ARX window system, style: graphical, evidence: [wikipedia], assertion_status: provisional }
hardware_platforms:
  - { platform: Acorn Archimedes, support_origin: intended-target, support_status: unreleased, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
architectures:
  - { value: ARM, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/ARX_(operating_system), title: ARX (operating system), source_kind: article }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/ARX_(operating_system)
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Acorn Computers Ltd.
    country_of_origin: United Kingdom; Kingdom of Great Britain; Kingdom of England;
      United Kingdom of Great Britain and Ireland
    purpose: Low cost paperless office computing workstation
    programming_languages: Modula-2+
    first_release: null
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: null
    os_family: Unix-like
    gui: Graphical user interface and special keyboard keys
    platforms: ARM
    kernel_type: Microkernel
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q350
# END GENERATED ENWIKI INFOBOX
---

## Overview

ARX was Acorn's unfinished graphical operating-system project for the ARM
Archimedes line. It is retained as an independently named, unreleased system;
the discovery source describes its cancellation rather than a shipped release.[^wikipedia]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/ARX_(operating_system)).
