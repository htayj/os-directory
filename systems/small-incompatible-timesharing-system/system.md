---
type: Operating System
title: Small Incompatible Timesharing System
description: MIT AI Laboratory's multi-user PDP-11/45 timesharing system for Logo and other PDP-11 programs, commonly called SITS or Small ITS.
tags: [operating-system, timesharing, mit, pdp-11, sits]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The preservation project establishes identity, purpose, platform, multi-user facilities, runnable reconstruction, and surviving TINTE binary. Implementation language, rights, and kernel taxonomy remain unresolved." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: preservation-repository-audit, language: en, source: sits-repository, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "Small Incompatible Timesharing System", kind: expanded-name, language: en, script: Latn, evidence: [sits-repository, gunkies-sits], assertion_status: documented }
  - { value: SITS, kind: acronym, language: en, script: Latn, evidence: [sits-repository], assertion_status: documented }
  - { value: "Small ITS", kind: common-name, language: en, script: Latn, evidence: [lars-raw-files], assertion_status: documented }
organizations:
  - { organization: "MIT Artificial Intelligence Laboratory Logo group", roles: [developer], evidence: [sits-repository, gunkies-sits], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: academic-research, primary: true, evidence: [sits-repository], assertion_status: documented }
design_purposes:
  - { value: educational-computing, primary: true, source_term: "environment suitable for running Logo", evidence: [sits-repository], assertion_status: documented }
  - { value: general-purpose-multilanguage-timesharing, primary: true, evidence: [sits-repository], assertion_status: documented }
target_audiences:
  - { value: "MIT Logo researchers and learners", evidence: [sits-repository], assertion_status: documented }
development_status: { value: inactive-original-with-runnable-preservation, evidence: [sits-repository], assertion_status: documented, scope: { as_of: 2026-07-29 } }
lifecycle_events:
  - { date: "1974/1975", kind: implementation-completed, evidence: [sits-repository], assertion_status: documented }
first_release: { date: 1974, evidence: [gunkies-sits], assertion_status: provisional }
system_organization:
  - { value: timesharing-executive, source_term: "general purpose multi-language timesharing system", evidence: [sits-repository], assertion_status: documented }
gui_status:
  - { value: mixed-terminal-and-graphics-display, evidence: [sits-repository], assertion_status: documented }
interfaces:
  - { name: "DDT command environment", style: command, modalities: [keyboard], evidence: [sits-repository], assertion_status: documented }
  - { name: "TV, vector, and raster display sessions", style: graphical-terminal, modalities: [keyboard, display], evidence: [sits-repository], assertion_status: documented }
hardware_platforms:
  - { value: "DEC PDP-11/45", evidence: [sits-repository, gunkies-sits], assertion_status: documented }
machine_classes: [minicomputer]
user_model:
  - { value: multi-user, evidence: [sits-repository], assertion_status: documented }
process_task_thread_model:
  - { value: "multiple processes per program and multiple jobs per user", evidence: [sits-repository], assertion_status: documented }
filesystems:
  - { value: "Multics-like tree-structured file system with potential access control", evidence: [sits-repository], assertion_status: documented }
source_preservation: { value: partial-raw-files-and-binaries, evidence: [sits-repository, lars-raw-files], assertion_status: documented }
binary_preservation: { value: runnable-under-emulation, evidence: [sits-repository], assertion_status: documented }
emulation:
  - { emulator: SIMH, status: runnable, evidence: [sits-repository], assertion_status: documented }
repositories:
  - { resource: "https://github.com/pdp11/sits", relationship: reconstruction, evidence: [sits-repository], assertion_status: documented }
  - { resource: "https://github.com/larsbrinkhoff/mit-logo-and-sits-raw-files", relationship: raw-source-preservation, evidence: [lars-raw-files], assertion_status: documented }
sources:
  - { id: sits-repository, resource: "https://github.com/pdp11/sits", title: "The SITS Timesharing System", source_kind: preservation-project }
  - { id: lars-raw-files, resource: "https://github.com/larsbrinkhoff/mit-logo-and-sits-raw-files", title: "MIT Logo and SITS raw files", source_kind: preservation-source-repository }
  - { id: gunkies-sits, resource: "https://gunkies.org/wiki/SITS", title: "SITS", source_kind: historical-computing-wiki }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: TINTE
  relationship: integral
  interface_style: full-screen-text
  source: https://github.com/pdp11/sits
  source_kind: preservation-project
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Overview

SITS was a general-purpose multi-language timesharing system built by MIT's
Logo group for a PDP-11/45. The preservation project quotes the contemporary
description of its tree-structured file system, access-control design,
multi-process programs, multiple jobs per user, and display support.[^sits]

# Preservation

The reconstruction builds a runnable system from preserved binaries and
automates disk formatting and installation under SIMH. Lars Brinkhoff's
separate raw-files repository preserves the recovered MIT Logo and SITS input
material. The surviving system includes the TINTE editor binary.

[^sits]: [The SITS Timesharing System](https://github.com/pdp11/sits).
