---
type: Operating System
title: BBN Exec III
description: A preserved executive system for Bolt, Beranek and Newman's PDP-1-class computer, currently represented by sorted documentation and listings.
tags: [operating-system, executive, bbn, pdp-1, preservation]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: identity, note: "The organization repository establishes the Exec III identity, BBN association, PDP-1 platform family, and document-preservation state. Purpose beyond executive operation, dates, language, interface, kernel, license, and runnable status remain unresolved." }
field_dispositions: [{field: text_editors, disposition: no-evidence-found, checked_at: '2026-07-29'}, {field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: gui_status, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: public-github-organization-audit, language: en, source: "https://github.com/BBN-1D/Exec-III", observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "BBN Exec III", kind: catalog-title, language: en, script: Latn, evidence: [exec-iii-repo], assertion_status: documented }
  - { value: "Exec-III", kind: repository-name, language: en, script: Latn, evidence: [exec-iii-repo], assertion_status: documented }
organizations:
  - { organization: "Bolt, Beranek and Newman", roles: [developer], evidence: [exec-iii-repo], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: research-organization-system-software, primary: true, evidence: [exec-iii-repo], assertion_status: provisional }
design_purposes:
  - { value: computer-executive-operation, primary: true, evidence: [exec-iii-repo], assertion_status: provisional }
development_status: { value: discontinued-with-documentary-preservation, evidence: [exec-iii-repo], assertion_status: documented }
hardware_platforms:
  - { value: "BBN PDP-1 / PDP-1D family", evidence: [exec-iii-repo, bbn-org], assertion_status: provisional }
machine_classes: [mainframe]
source_preservation: { value: hardcopy-listings-awaiting-transcription, evidence: [exec-iii-repo], assertion_status: documented }
documentation_preservation: { value: sorted-document-collection, evidence: [exec-iii-repo], assertion_status: documented }
repositories:
  - { resource: "https://github.com/BBN-1D/Exec-III", relationship: documentation-and-listing-preservation, evidence: [exec-iii-repo], assertion_status: documented }
sources:
  - { id: exec-iii-repo, resource: "https://github.com/BBN-1D/Exec-III", title: "Exec-III", source_kind: preservation-project }
  - { id: bbn-org, resource: "https://github.com/BBN-1D", title: "BBN-1D GitHub organization", source_kind: preservation-organization }
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

The repository describes a document and listing collection that still requires
transcription. This record therefore does not claim surviving machine-readable
source or a runnable reconstruction.
