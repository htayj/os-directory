---
type: Operating System
title: Genera
description: Symbolics' Lisp-written operating system and integrated software-development environment for Symbolics Lisp machines and later virtual platforms.
tags: [operating-system, lisp-machine, symbolics, genera]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "Vendor documentation establishes OS/environment identity, Lisp implementation, interface, editor, and platform families. Product chronology and license terms need a versioned pass." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: kernels, disposition: not-applicable, checked_at: 2026-07-29, reason: "Genera Concepts contrasts its open integrated architecture with conventional protected-core kernels." }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: lisp-machine-hardware-audit, language: en, source: gunkies-lisp-machine, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: Genera, kind: official, language: en, script: Latn, evidence: [genera-concepts], assertion_status: documented }
  - { value: Open Genera, kind: product-variant, language: en, script: Latn, evidence: [open-genera-guide], assertion_status: documented }
organizations:
  - { organization: Symbolics, roles: [developer, vendor, publisher], evidence: [genera-concepts], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: commercial-product, primary: true, evidence: [genera-concepts], assertion_status: documented }
design_purposes:
  - { value: evolutionary-software-development, primary: true, evidence: [genera-concepts], assertion_status: documented }
  - { value: artificial-intelligence-application-development, primary: false, evidence: [genera-concepts], assertion_status: documented }
development_status: { value: historical-commercial-lineage, evidence: [genera-index], assertion_status: provisional }
rights_regime: { value: copyrighted-commercial-software, evidence: [genera-concepts], assertion_status: documented }
programming_languages:
  - { language: Lisp, extent: primary, evidence: [genera-concepts], assertion_status: documented }
system_organization:
  - { value: integrated-lisp-environment, source_term: "encompasses what you normally think of as an operating system", evidence: [genera-concepts], assertion_status: documented }
kernels:
  - { architecture: no-protected-conventional-kernel-boundary, evidence: [genera-concepts], assertion_status: documented }
gui_status:
  - { value: graphical, evidence: [genera-concepts], assertion_status: documented }
interfaces:
  - { name: "Dynamic Windows and Command Processor", style: graphical-and-command, modalities: [keyboard, pointing-device], evidence: [genera-concepts], assertion_status: documented }
hardware_platforms:
  - { value: "Symbolics 3600 family", evidence: [genera-index], assertion_status: documented }
  - { value: "Symbolics XL and UX families", evidence: [genera-index], assertion_status: documented }
  - { value: "Symbolics MacIvory", evidence: [genera-index], assertion_status: documented }
  - { value: "Symbolics NXP1000", evidence: [genera-index], assertion_status: documented }
virtual_platforms:
  - { value: "DEC Alpha with Digital UNIX via Open Genera", evidence: [open-genera-guide], assertion_status: documented }
machine_classes: [lisp-machine, workstation, virtual-machine]
lineage:
  - { relationship: fork-descendant, target: /systems/mit-lisp-machine-system-software/, evidence: [genera-concepts], assertion_status: documented }
sources:
  - { id: gunkies-lisp-machine, resource: "https://gunkies.org/w/index.php?title=LISP_machine&oldid=36748", title: "LISP machine", source_kind: historical-computing-wiki }
  - { id: genera-concepts, resource: "https://bitsavers.org/pdf/symbolics/software/genera_8/Genera_Concepts.pdf", title: "Genera Concepts", author: Symbolics, source_kind: official-system-manual }
  - { id: genera-index, resource: "https://bitsavers.org/pdf/symbolics/software/genera_8/", title: "Symbolics Genera 8 documentation index", source_kind: documentation-archive-index }
  - { id: open-genera-guide, resource: "https://bitsavers.org/pdf/symbolics/software/genera_8/Open_Genera_Installation_Guide.pdf", title: "Open Genera Installation Guide", author: Symbolics, source_kind: official-installation-guide }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: Zmacs
  relationship: integral
  interface_style: graphical
  source: https://bitsavers.org/pdf/symbolics/software/genera_8/Genera_Workbook.pdf
  source_kind: official-system-manual
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Overview

Symbolics describes Genera as a whole environment encompassing what would
conventionally be separated into an operating system, commands, utilities, and
applications. The resident activities are Lisp functions, and the environment
is written in Lisp.[^genera-concepts]

# System organization

Genera Concepts explicitly contrasts Genera with conventional operating systems
having a protected core or kernel. This record preserves that terminology
instead of forcing Genera into a monolithic/microkernel taxonomy.

# Platforms and editor

The Genera 8 documentation includes installation guides for 3600, XL, UX,
MacIvory, and NXP1000 families. Open Genera later hosted the environment on DEC
Alpha/Digital UNIX. Zmacs is the integrated editor.[^genera-index]

[^genera-concepts]: [Genera Concepts](https://bitsavers.org/pdf/symbolics/software/genera_8/Genera_Concepts.pdf), “Genera — A Short Conceptual Tour.”
[^genera-index]: [Symbolics Genera 8 documentation index](https://bitsavers.org/pdf/symbolics/software/genera_8/).
