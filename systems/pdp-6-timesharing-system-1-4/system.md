---
type: Operating System
title: PDP-6 Timesharing System 1.4
description: A preserved version of Digital Equipment Corporation's manufacturer-supported PDP-6 multiprogramming and time-sharing system.
tags: [operating-system, timesharing, dec, pdp-6, preservation]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The preservation repository and contemporary manual establish identity, purpose, developer, platform, and reconstruction status. Release date, implementation language, kernel taxonomy, licensing, and editor relationships remain unresolved." }
field_dispositions: [{field: text_editors, disposition: no-evidence-found, checked_at: '2026-07-29'}, {field: programming_languages, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: gui_status, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: public-github-organization-audit, language: en, source: "https://github.com/PDP-6/TS-1.4", observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "PDP-6 Timesharing System 1.4", kind: catalog-title, language: en, script: Latn, evidence: [pdp6-ts-repo, pdp6-manual], assertion_status: documented }
  - { value: "TS-1.4", kind: repository-short-name, language: en, script: Latn, evidence: [pdp6-ts-repo], assertion_status: documented }
organizations:
  - { organization: "Digital Equipment Corporation", roles: [developer, vendor], evidence: [pdp6-manual], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: commercial-manufacturer-system-software, primary: true, evidence: [pdp6-manual], assertion_status: documented }
design_purposes:
  - { value: interactive-timesharing, primary: true, evidence: [pdp6-manual], assertion_status: documented }
  - { value: multiprogramming, primary: true, evidence: [pdp6-manual], assertion_status: documented }
development_status: { value: discontinued-original-with-partial-reconstruction, evidence: [pdp6-ts-repo], assertion_status: documented }
hardware_platforms:
  - { value: "DEC PDP-6", evidence: [pdp6-ts-repo, pdp6-manual], assertion_status: documented }
machine_classes: [mainframe]
source_preservation: { value: typed-and-proofread-executive-listing, evidence: [pdp6-ts-repo], assertion_status: documented }
documentation_preservation: { value: scanned-contemporary-manuals, evidence: [pdp6-ts-repo, pdp6-manual], assertion_status: documented }
preservation_gaps:
  - { value: "Common User Service Programs have not been found", evidence: [pdp6-ts-repo], assertion_status: documented }
repositories:
  - { resource: "https://github.com/PDP-6/TS-1.4", relationship: source-reconstruction, evidence: [pdp6-ts-repo], assertion_status: documented }
sources:
  - { id: pdp6-ts-repo, resource: "https://github.com/PDP-6/TS-1.4", title: "DEC PDP-6 timesharing system 1.4", source_kind: preservation-project }
  - { id: pdp6-manual, resource: "https://bitsavers.org/pdf/dec/pdp6/DEC-6-0-EX-SYS-UM-IP-PRE00_Multiprogramming_System_Manual_1965.pdf", title: "PDP-6 Multiprogramming System Manual", source_kind: contemporary-manual }
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

The organization repository preserves a typed and proofread executive derived
from scanned listings. It explicitly says the CUSPs have not been found, so the
record does not claim a complete runnable distribution.
