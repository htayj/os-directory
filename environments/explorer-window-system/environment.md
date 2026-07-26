---
type: Window System
title: Explorer Window System
description: Integral graphical window system of Texas Instruments' Explorer System Software.
tags: [graphical-environment, window-system, lisp-machine, explorer]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness:
  level: core
  note: Identity and integration are documented from TI manuals; detailed architecture remains incomplete.
field_dispositions:
  - field: first_release
    disposition: no-evidence-found
    checked_at: 2026-07-26
  - field: implementation_languages
    disposition: not-researched
    checked_at: 2026-07-26
discovery_provenance:
  - method: host-system-component-audit
    language: en
    native_label: Explorer Window System
    source: window-reference
    observed_at: 2026-07-26
    disposition: included-environment
names:
  - value: Explorer Window System
    kind: official
    language: en
    script: Latn
    evidence: [window-reference, release-4.1]
    assertion_status: documented
organizations:
  - organization: https://www.ti.com/
    roles: [developer, publisher, vendor, rights-holder]
    evidence: [window-reference]
    assertion_status: documented
countries_of_origin: [US]
development_contexts:
  - value: commercial-product
    primary: true
    evidence: [window-reference]
    assertion_status: documented
design_purposes:
  - value: software-development
    primary: true
    note: Integrated graphical interaction for Explorer development tools and applications.
    evidence: [window-reference, system-glossary]
    assertion_status: documented
development_status:
  value: discontinued
  evidence: [host-system]
  assertion_status: inferred
rights_regime:
  value: copyrighted
  evidence: [window-reference]
  assertion_status: documented
software_freedom_status:
  value: proprietary
  evidence: [window-reference]
  assertion_status: documented
licenses: []
environment_kind: window-system
host_systems:
  - system: /systems/explorer-system-software/system.md
    relationship: integral-component
    provisioning: built-in
    evidence: [release-4.1, window-reference]
    assertion_status: documented
host_relationship: integral
display_architecture:
  - value: bitmapped hierarchical window system
    evidence: [system-glossary, window-reference]
    assertion_status: documented
ui_paradigms:
  - { value: direct-manipulation, evidence: [window-reference], assertion_status: documented }
  - { value: menu-based, evidence: [window-reference], assertion_status: documented }
window_model:
  - value: hierarchical windows associated with processes and implemented as flavor instances
    evidence: [system-glossary]
    assertion_status: documented
input_model:
  - modalities: [keyboard, pointer]
    evidence: [system-glossary, window-reference]
    assertion_status: documented
desktop_components:
  - { value: System Access Menu, evidence: [release-4.1], assertion_status: documented }
application_model:
  - value: Lisp processes using windows as input/output streams
    evidence: [system-glossary]
    assertion_status: documented
toolkits: []
environment_apis: []
bundled_applications:
  - { value: Zmacs, provisioning: built-in, evidence: [system-glossary], assertion_status: documented }
hardware_platforms:
  - platform: Texas Instruments Explorer family
    support_origin: original-target
    support_status: supported
    execution_mode: native
    evidence: [window-reference, release-4.1]
    assertion_status: documented
source_preservation:
  survival: substantial
  access: public
  authorization: permission-unclear
  evidence: [source-archive]
documentation_preservation:
  survival: substantial
  access: public
  authorization: permission-unclear
  evidence: [window-reference]
known_gaps:
  - { value: Exact first and final releases, assertion_status: unknown }
  - { value: Complete API and toolkit boundary, assertion_status: unknown }
sources:
  - id: window-reference
    resource: https://bitsavers.org/pdf/ti/explorer/2243200-0001B_windowSys.pdf
    title: Explorer Window System Reference
    language: en
    author: organization:texas-instruments
    source_kind: contemporary-reference-manual
    accessed: 2026-07-26
  - id: system-glossary
    resource: https://bitsavers.org/pdf/ti/explorer/2243134-0001A_Glossary_6-87.pdf
    title: Explorer System Glossary
    language: en
    author: organization:texas-instruments
    source_kind: contemporary-system-manual
    publication_date: 1987-06
    accessed: 2026-07-26
  - id: release-4.1
    resource: https://bitsavers.org/pdf/ti/explorer/2549844-0001C_4.1relNotes.pdf
    title: Explorer Release 4.1 Software Release Information
    language: en
    author: organization:texas-instruments
    source_kind: contemporary-release-notes
    publication_date: 1987-06
    accessed: 2026-07-26
  - id: host-system
    resource: /systems/explorer-system-software/system.md
    title: Explorer System Software catalog record
    source_kind: catalog-record
  - id: source-archive
    resource: https://archive.org/details/ti-explorer
    title: TI Explorer Lisp Machine Source Code (1991)
    source_kind: preserved-source-snapshot
    accessed: 2026-07-26
---

# Overview

The Explorer Window System is the integral graphical window system of Explorer
System Software. TI documented it separately and release 4.1 contains a
distinct window-system change section, so it receives an environment record
without being mistaken for the operating system.

# Architecture

TI's glossary defines a window as a rectangular display region associated with
a process and acting as an input/output stream. Windows are flavor instances
arranged in a hierarchy; the screen is the hierarchy's top node. The system
directs keyboard and mouse input to the appropriate process.

# Host Relationship

On Explorer I and II the window system was integral to the native Lisp
environment. The microExplorer variant instead presented Explorer software
through the Macintosh II window system, so that hosted presentation path must
not be conflated with the native Explorer Window System.

# Open Questions

* Which APIs were stable public interfaces versus internal implementation?
* How did the native window system differ across monochrome, color, and
  multiple-screen configurations?
* Which source directories constitute the complete window-system component?
