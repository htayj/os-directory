---
type: Operating System
title: Alto Executive
description: Xerox Alto-family command executive and boot environment used to start Interlisp-D on Xerox 1100 Lisp workstations.
tags: [operating-system, executive, xerox, lisp-machine]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The Xerox Interlisp-D manual establishes boot behavior, command-executive role, local files, and the Xerox 1100 platform. Broader Alto lineage and release history remain outside this pass." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: lisp-machine-hardware-audit, language: en, source: xerox-1100-manual, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "Alto Executive", kind: official, language: en, script: Latn, evidence: [xerox-1100-manual], assertion_status: documented }
organizations:
  - { organization: Xerox, roles: [developer, vendor], evidence: [xerox-1100-manual], assertion_status: documented }
countries_of_origin: [US]
design_purposes:
  - { value: boot-and-command-execution, primary: true, evidence: [xerox-1100-manual], assertion_status: documented }
development_status: { value: inactive, evidence: [xerox-1100-manual], assertion_status: inferred, scope: { as_of: 2026-07-29 } }
rights_regime: { value: copyrighted-commercial-software, evidence: [xerox-1100-manual], assertion_status: provisional }
system_organization:
  - { value: executive, source_term: "Executive", evidence: [xerox-1100-manual], assertion_status: documented }
gui_status:
  - { value: text-command, evidence: [xerox-1100-manual], assertion_status: documented }
interfaces:
  - { name: "Alto Executive command interface", style: command-line, modalities: [keyboard], evidence: [xerox-1100-manual], assertion_status: documented }
hardware_platforms:
  - { value: "Xerox 1100 Scientific Information Processor", evidence: [xerox-1100-manual], assertion_status: documented }
machine_classes: [lisp-machine, workstation]
execution_environments:
  - { value: "Interlisp-D", relationship: launched-environment, evidence: [xerox-1100-manual], assertion_status: documented }
sources:
  - { id: xerox-1100-manual, resource: "https://xeroxparcarchive.computerhistory.org/eris/lispmanual/.CHAPX1100.PRESS%211.pdf", title: "Using Interlisp-D on the Xerox 1100", author: Xerox, source_kind: contemporary-system-manual }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: no-evidence-found
  note: No editor relationship was established during the incremental source-backed
    record addition.
text_editors: []
# END GENERATED TEXT EDITORS
---

# Overview

The Xerox manual states that the 1100 boots into the Alto Executive and that
its most important capability in this configuration is starting Interlisp-D.
It documents login, file, partition, diagnostic, and program-launch commands at
the Executive layer.[^xerox-1100-manual]

# Layering boundary

Alto Executive is cataloged separately from Interlisp-D. The manual explicitly
distinguishes the brief boot/command environment from the graphical Lisp
environment where users normally work.

[^xerox-1100-manual]: [Using Interlisp-D on the Xerox 1100](https://xeroxparcarchive.computerhistory.org/eris/lispmanual/.CHAPX1100.PRESS%211.pdf), sections 22.3–22.11.
