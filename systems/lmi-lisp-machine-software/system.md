---
type: Operating System
title: LMI Lisp Machine Software
description: Lisp Machines, Inc.'s integrated Lisp-machine system software for Series III and Lambda hardware.
tags: [operating-system, lisp-machine, lmi, lambda]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The June 1982 vendor overview establishes platforms, purpose, facilities, Lisp implementation, and ZMACS; chronology and license terms remain unresolved." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: lisp-machine-hardware-audit, language: en, source: gunkies-lisp-machine, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "LMI Lisp Machine Software", kind: official, language: en, script: Latn, evidence: [lmi-overview], assertion_status: documented }
organizations:
  - { organization: "Lisp Machines, Inc.", roles: [developer, vendor, publisher], evidence: [lmi-overview], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: commercial-product, primary: true, evidence: [lmi-overview], assertion_status: documented }
design_purposes:
  - { value: interactive-software-development, primary: true, evidence: [lmi-overview], assertion_status: documented }
  - { value: large-lisp-application-development, primary: true, evidence: [lmi-overview], assertion_status: documented }
development_status: { value: inactive, evidence: [lmi-overview], assertion_status: inferred, scope: { as_of: 2026-07-29 } }
rights_regime: { value: copyrighted-commercial-software, evidence: [lmi-overview], assertion_status: documented }
programming_languages:
  - { language: "Lisp Machine Lisp", extent: primary, evidence: [lmi-overview], assertion_status: documented }
system_organization:
  - { value: integrated-lisp-environment, evidence: [lmi-overview], assertion_status: documented }
gui_status:
  - { value: graphical, evidence: [lmi-overview], assertion_status: documented }
interfaces:
  - { name: "Lisp listener and window system", style: graphical-and-listener, modalities: [keyboard, pointing-device], evidence: [lmi-overview], assertion_status: documented }
hardware_platforms:
  - { value: "LMI Series III", evidence: [lmi-overview], assertion_status: documented }
  - { value: "LMI Lambda", evidence: [lmi-overview], assertion_status: documented }
machine_classes: [lisp-machine, workstation]
lineage:
  - { relationship: fork-descendant, target: /systems/mit-lisp-machine-system-software/, evidence: [lmi-overview], assertion_status: documented }
sources:
  - { id: gunkies-lisp-machine, resource: "https://gunkies.org/w/index.php?title=LISP_machine&oldid=36748", title: "LISP machine", source_kind: historical-computing-wiki }
  - { id: lmi-overview, resource: "https://www.bitsavers.org/pdf/lmi/LMI_LispSW_Overview_Jun82.pdf", title: "Overview of the LMI Lisp Machine Software", author: "Lisp Machines, Inc.", date: 1982-06, source_kind: vendor-software-overview }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: ZMACS
  relationship: integral
  interface_style: graphical
  source: https://bitsavers.org/pdf/lmi/LMI_LispSW_Overview_Jun82.pdf
  source_kind: vendor-software-overview
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Overview

LMI's June 1982 overview describes an integrated hardware/software system that
executes on both Series III and Lambda machines. It documents the Lisp
interpreter, compilers, window system, file and network software, debugger, and
other resident facilities.[^lmi-overview]

# Text editor

The overview calls ZMACS the heart of the software environment and documents it
as a screen-oriented real-time editor integrated with the running Lisp world.

[^lmi-overview]: [Overview of the LMI Lisp Machine Software](https://www.bitsavers.org/pdf/lmi/LMI_LispSW_Overview_Jun82.pdf), pp. 1–7.
