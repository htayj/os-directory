---
type: Operating System
title: TI System V/68
description: Texas Instruments' Motorola 68000-family UNIX System V port for the TI S1500 and HP 9000-1500 workstation lineage.
tags: [operating-system, unix, system-v, texas-instruments, preservation]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The preservation organization establishes product identity, platform, proprietary preservation constraints, filesystem artifacts, and a surviving System V Release 3.2.2.1 installation. Original release date, implementation language, kernel subtype, interface, and editor set require vendor-manual and media-level research." }
field_dispositions: [{field: text_editors, disposition: no-evidence-found, checked_at: '2026-07-29'}, {field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29, reason: The repository identifies licensed commercial software but not a reusable license identifier.}, {field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: gui_status, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: public-github-organization-audit, language: en, source: "https://github.com/TI-S1500/TISYSV68-FS", observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "TI System V/68", kind: product-name, language: en, script: Latn, evidence: [tisysv-repo, ti-org], assertion_status: documented }
organizations:
  - { organization: "Texas Instruments", roles: [developer, vendor], evidence: [tisysv-repo, ti-org], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: commercial-vendor-unix-port, primary: true, evidence: [tisysv-repo], assertion_status: documented }
design_purposes:
  - { value: workstation-unix, primary: true, evidence: [tisysv-repo, ti-org], assertion_status: documented }
development_status: { value: discontinued-with-restricted-preservation, evidence: [tisysv-repo], assertion_status: documented }
rights_regime: { value: commercial-proprietary, evidence: [tisysv-repo], assertion_status: documented }
hardware_platforms:
  - { value: "TI S1500 / HP 9000-1500", evidence: [tisysv-repo, ti-org], assertion_status: documented }
architectures:
  - { value: "Motorola 68000 family", source_term: "System V/68", evidence: [tisysv-repo], assertion_status: provisional }
machine_classes: [workstation]
lineage_relations:
  - { target: "UNIX System V", relation: vendor-port-of, evidence: [tisysv-repo], assertion_status: documented }
latest_releases:
  - { version: "System V Release 3.2.2.1 preserved installation", evidence: [tisysv-repo], assertion_status: documented }
binary_preservation: { value: extracted-installed-filesystems-restricted, evidence: [tisysv-repo], assertion_status: documented }
preservation_gaps:
  - { value: "Repository access is restricted because preserved filesystems contain PII and licensed proprietary software", evidence: [tisysv-repo], assertion_status: documented }
repositories:
  - { resource: "https://github.com/TI-S1500/TISYSV68-FS", relationship: restricted-filesystem-preservation, evidence: [tisysv-repo], assertion_status: documented }
  - { resource: "https://github.com/TI-S1500/s5fstool", relationship: filesystem-recovery-tool, evidence: [ti-org], assertion_status: documented }
sources:
  - { id: tisysv-repo, resource: "https://github.com/TI-S1500/TISYSV68-FS", title: "TI System V/68 Extracted Filesystems", source_kind: preservation-project }
  - { id: ti-org, resource: "https://github.com/TI-S1500", title: "TI S1500 / HP 9000-1500 preservation organization", source_kind: preservation-organization }
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

# Preservation boundary

The filesystem repository explicitly restricts access because it contains
personal information and licensed commercial software. The catalog records its
existence and metadata without redistributing or inspecting restricted content.
