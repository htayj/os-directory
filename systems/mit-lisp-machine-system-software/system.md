---
type: Operating System
title: MIT Lisp Machine system software
description: MIT AI Laboratory's Lisp Machine Lisp operating system and integrated environment for the CONS/CADR lineage.
tags: [operating-system, lisp-machine, mit, cadr]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "Identity, language, interface, editor, and CADR-family scope are documented; chronology, licensing, and modern kernel taxonomy remain unresolved." }
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
  - { value: "MIT Lisp Machine system software", kind: descriptive, language: en, script: Latn, evidence: [mit-lm-manual], assertion_status: documented }
  - { value: "Lisp Machine operating system", kind: contemporary-descriptive, language: en, script: Latn, evidence: [mit-lm-manual], assertion_status: documented }
organizations:
  - { organization: "MIT Artificial Intelligence Laboratory", roles: [developer], evidence: [mit-lm-manual], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: academic-research, primary: true, evidence: [mit-lm-manual], assertion_status: documented }
design_purposes:
  - { value: artificial-intelligence-research, primary: true, evidence: [mit-lm-manual], assertion_status: documented }
  - { value: interactive-software-development, primary: true, evidence: [mit-lm-manual], assertion_status: documented }
development_status: { value: inactive, evidence: [mit-lm-manual], assertion_status: inferred, scope: { as_of: 2026-07-29 } }
rights_regime: { value: copyright-status-not-fully-researched, assertion_status: unknown }
programming_languages:
  - { language: "Lisp Machine Lisp", extent: primary, evidence: [mit-lm-manual], assertion_status: documented }
system_organization:
  - { value: integrated-lisp-environment, source_term: "\"operating system\"", evidence: [mit-lm-manual], assertion_status: documented }
gui_status:
  - { value: graphical, evidence: [mit-lm-manual], assertion_status: documented }
interfaces:
  - { name: "Lisp listener and window system", style: graphical-and-listener, modalities: [keyboard, pointing-device], evidence: [mit-lm-manual], assertion_status: documented }
hardware_platforms:
  - { value: "MIT CONS", evidence: [gunkies-lisp-machine], assertion_status: documented }
  - { value: "MIT CADR", evidence: [mit-lm-manual, gunkies-lisp-machine], assertion_status: documented }
machine_classes: [lisp-machine, workstation]
known_gaps:
  - { value: "The sources do not define a modern monolithic, microkernel, or hybrid classification.", assertion_status: documented }
sources:
  - { id: gunkies-lisp-machine, resource: "https://gunkies.org/w/index.php?title=LISP_machine&oldid=36748", title: "LISP machine", source_kind: historical-computing-wiki }
  - { id: mit-lm-manual, resource: "https://bitsavers.org/pdf/mit/cadr/chinual_3rdEd_Mar81.pdf", title: "Lisp Machine Manual, third edition", date: 1981-03, source_kind: contemporary-system-manual }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: Zwei
  relationship: integral
  interface_style: graphical
  source: https://bitsavers.org/pdf/mit/cadr/chinual_3rdEd_Mar81.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Overview

The 1981 manual explicitly says that it describes both the Lisp Machine
language and its “operating system.” It presents an integrated system rather
than a separately named kernel and userland.[^mit-lm-manual]

# Implementation and interfaces

The system used Lisp Machine Lisp throughout its software environment. The
manual documents the graphical window system, processes, storage and file
facilities, networking, and the integrated Zwei editor.[^mit-lm-manual]

# Platforms

This record covers the MIT CONS/CADR software lineage. It does not silently
extend to the later, independently maintained LMI, Symbolics, or TI forks.

[^mit-lm-manual]: [Lisp Machine Manual, third edition](https://bitsavers.org/pdf/mit/cadr/chinual_3rdEd_Mar81.pdf), preface and editor sections.
