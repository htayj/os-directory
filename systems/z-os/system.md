---
type: Operating System
title: z/OS
description: Draft operating-system identity pending core research.
tags: [operating-system, ibm, mainframe]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Linked identity accepted for draft inventory; core facts remain unverified." }
field_dispositions: [{field: text_editors, disposition: documented, checked_at: '2026-07-26'}, {field: organizations, disposition: not-researched, checked_at: 2026-07-26}, {field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26}, {field: design_purposes, disposition: not-researched, checked_at: 2026-07-26}, {field: development_status, disposition: unknown, checked_at: 2026-07-26}, {field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26}, {field: rights_regime, disposition: not-researched, checked_at: 2026-07-26}, {field: licenses, disposition: not-researched, checked_at: 2026-07-26}, {field: programming_languages, disposition: not-researched, checked_at: 2026-07-26}, {field: system_organization, disposition: not-researched, checked_at: 2026-07-26}, {field: kernels, disposition: not-researched, checked_at: 2026-07-26}, {field: interfaces, disposition: not-researched, checked_at: 2026-07-26}, {field: platforms, disposition: not-researched, checked_at: 2026-07-26}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "z/OS", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Z/OS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: IBM
    country_of_origin: United States
    purpose: Enterprise / Mainframes
    programming_languages: primarily PL/X , HLASM , and C / C++
    first_release: March 30, 2001 ; 25 years ago ( 2001-03-30 ) (V1R1, announced October,
      2000)
    latest_release: Version 3.2 (V3R2) / September 30, 2025 ; 9 months ago ( 2025-09-30
      )
    last_updated: Version 3.2 (V3R2) / September 30, 2025 ; 9 months ago ( 2025-09-30
      )
    development_status: Current
    source_model: Closed source with open source components
    os_family: MVS Unix
    gui: ISPF , z/OS Management Facility
    platforms: z/Architecture
    kernel_type: Monolithic (uniquely hardware-assisted)
    license: Proprietary monthly license charge (MLC); pricing available based on
      actual use (VWLC, EWLC, AWLC, EAWLC, IWP); reduced pricing options (zELC, zNALC,
      "Solution Edition") for many applications
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q37156
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: ISPF editor
  relationship: bundled-optional
  interface_style: full-screen-text
  source: https://www.ibm.com/docs/en/zos/3.2.0?topic=edit-using-editor
  source_kind: vendor-documentation
  assertion_status: documented
- name: oedit
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://www.ibm.com/docs/en/zos/3.2.0?topic=descriptions-oedit-edit-text
  source_kind: vendor-documentation
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# z/OS

Draft inventory record; core factual research is pending.
