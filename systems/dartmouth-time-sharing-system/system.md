---
type: Operating System
title: Dartmouth Time-Sharing System
description: Dartmouth College's educational general-purpose timesharing operating-system lineage, commonly abbreviated DTSS.
tags: [operating-system, timesharing, dartmouth, education, dtss]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "Dartmouth sources establish origin, educational purpose, 1964 operation, major hardware generations, and 1993 phase-out. Implementation language, license, kernel taxonomy, and editor relationships remain unresolved." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29, reason: "BASIC was a hosted language; the reviewed sources do not establish it as the implementation language of DTSS." }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: preservation-repository-audit, language: en, source: lars-dtss-backup, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "Dartmouth Time-Sharing System", kind: official, language: en, script: Latn, evidence: [dartmouth-1960s, dartmouth-exhibit], assertion_status: documented }
  - { value: DTSS, kind: acronym, language: en, script: Latn, evidence: [dartmouth-1960s], assertion_status: documented }
organizations:
  - { organization: "Dartmouth College", roles: [developer, operator], evidence: [dartmouth-1960s, dartmouth-1970s], assertion_status: documented }
  - { organization: "DTSS Incorporated", roles: [commercializer], evidence: [dartmouth-1970s], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: academic-educational-system, primary: true, evidence: [dartmouth-1960s], assertion_status: documented }
design_purposes:
  - { value: broad-access-to-computing, primary: true, evidence: [dartmouth-1960s], assertion_status: documented }
  - { value: interactive-education, primary: true, evidence: [dartmouth-1960s], assertion_status: documented }
target_audiences:
  - { value: "Dartmouth students and faculty", evidence: [dartmouth-1960s], assertion_status: documented }
development_status: { value: discontinued, evidence: [dartmouth-1970s], assertion_status: documented }
lifecycle_events:
  - { date: 1964-05-01, kind: first-successful-operation, evidence: [dartmouth-1960s], assertion_status: documented }
  - { date: 1967, kind: "GE-635 generation operational", evidence: [dartmouth-1960s], assertion_status: documented }
  - { date: 1972, kind: commercial-organization-formed, evidence: [dartmouth-1970s], assertion_status: documented }
  - { date: 1993, kind: phased-out, evidence: [dartmouth-1970s], assertion_status: documented }
first_release: { date: 1964-05-01, evidence: [dartmouth-1960s], assertion_status: documented }
system_organization:
  - { value: executive-based-timesharing-system, source_term: "DTSS executive programs", evidence: [dartmouth-1970s], assertion_status: documented }
gui_status:
  - { value: non-graphical-terminal, evidence: [dartmouth-1960s], assertion_status: documented }
interfaces:
  - { name: "Teletype interactive sessions", style: terminal, modalities: [keyboard, printed-output], evidence: [dartmouth-1960s], assertion_status: documented }
hardware_platforms:
  - { value: "GE-225 / DATANET-30", evidence: [dartmouth-1960s, dartmouth-exhibit], assertion_status: documented }
  - { value: "GE-235 / GE-265", evidence: [dartmouth-exhibit], assertion_status: documented }
  - { value: "GE-635", evidence: [dartmouth-1960s, dartmouth-exhibit], assertion_status: documented }
machine_classes: [mainframe]
source_preservation: { value: partial-multisite-backup, evidence: [lars-dtss-backup], assertion_status: documented }
documentation_preservation: { value: manuals-scans-and-proofed-listings, evidence: [lars-dtss-backup, bitsavers-dtss], assertion_status: documented }
repositories:
  - { resource: "https://github.com/larsbrinkhoff/dtss-backup", relationship: multisite-preservation-backup, evidence: [lars-dtss-backup], assertion_status: documented }
archives:
  - { resource: "https://bitsavers.org/pdf/dartmouth/dtss/", relationship: documentation-archive, evidence: [bitsavers-dtss], assertion_status: documented }
sources:
  - { id: dartmouth-1960s, resource: "https://www.dartmouth.edu/its-tools/archive/history/timeline/1960s.html", title: "Dartmouth Computing Timeline: The 1960s", source_kind: institutional-history }
  - { id: dartmouth-1970s, resource: "https://www.dartmouth.edu/its-tools/archive/history/timeline/1970s.html", title: "Dartmouth Computing Timeline: The 1970s", source_kind: institutional-history }
  - { id: dartmouth-exhibit, resource: "https://www.library.dartmouth.edu/exhibits/sharing-the-computer", title: "Sharing the Computer", author: "Dartmouth Libraries", source_kind: institutional-exhibit }
  - { id: lars-dtss-backup, resource: "https://github.com/larsbrinkhoff/dtss-backup", title: "Backup of DTSS and Dartmouth BASIC", source_kind: preservation-aggregation }
  - { id: bitsavers-dtss, resource: "https://bitsavers.org/pdf/dartmouth/dtss/", title: "Dartmouth DTSS documentation archive", source_kind: documentation-archive }
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

DTSS was designed at Dartmouth to make interactive computing broadly
accessible to students and faculty. Dartmouth records its first successful
simultaneous execution at 4 a.m. on May 1, 1964 and documents later GE-635
operation, commercialization, and eventual phase-out.[^dartmouth]

# Preservation

Lars Brinkhoff's repository backs up DTSS material from Dartmouth, Bitsavers,
Columbia, Cornell, and other historical sites, including executive listings,
manual scans, proofed material, and later system documentation.[^backup]

[^dartmouth]: [Dartmouth Computing Timeline: The 1960s](https://www.dartmouth.edu/its-tools/archive/history/timeline/1960s.html).
[^backup]: [Backup of DTSS and Dartmouth BASIC](https://github.com/larsbrinkhoff/dtss-backup).
