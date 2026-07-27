---
type: Operating System
title: WAITS
description: Draft operating-system identity pending core research.
tags: [operating-system]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Wikipedia-linked identity accepted for draft inventory; all core facts remain unverified." }
field_dispositions: [{field: text_editors, disposition: documented, checked_at: '2026-07-26'}, {field: organizations, disposition: not-researched, checked_at: 2026-07-26}, {field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26}, {field: design_purposes, disposition: not-researched, checked_at: 2026-07-26}, {field: development_status, disposition: unknown, checked_at: 2026-07-26}, {field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26}, {field: rights_regime, disposition: not-researched, checked_at: 2026-07-26}, {field: licenses, disposition: not-researched, checked_at: 2026-07-26}, {field: programming_languages, disposition: not-researched, checked_at: 2026-07-26}, {field: system_organization, disposition: not-researched, checked_at: 2026-07-26}, {field: kernels, disposition: not-researched, checked_at: 2026-07-26}, {field: interfaces, disposition: not-researched, checked_at: 2026-07-26}, {field: platforms, disposition: not-researched, checked_at: 2026-07-26}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "WAITS", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/WAITS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Stanford Artificial Intelligence Laboratory
    country_of_origin: United States
    purpose: Mainframe computer
    programming_languages: null
    first_release: 1967 ; 59 years ago ( 1967 )
    latest_release: null
    last_updated: null
    development_status: Historic
    source_model: null
    os_family: DEC OS family
    gui: null
    platforms: PDP-6 , PDP-10
    kernel_type: null
    license: null
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q22704990
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: E
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://www.saildart.org/MONCOM.BH%5BS%2CDOC%5D26
  source_kind: contemporary-system-manual
  assertion_status: documented
  scope:
    releases:
    - WAITS 9.13/M
  note: The manual says several editors are available and identifies E as the current
    favorite.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-001
  researcher: deep_academic_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: WAITS was the Stanford AI Lab PDP-10 time-sharing monitor. The 1982 Monitor Command
    Manual documents a resource-managing monitor, command and display-terminal interfaces, the E editor,
    user-visible languages, and WAITS 9.13/M. It does not establish WAITS's implementation language or
    license.
  sources:
  - id: waits-manual
    title: Monitor Command Manual, Stanford Artificial Intelligence Laboratory Operating Note 54.7
    url: https://www.saildart.org/MONCOM.BH%5BS%2CDOC%5D26
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 1982-03
    primary: true
    notes: SAIL archive transcription of the WAITS monitor command manual.
  - id: waits-history
    title: Stanford WAITS
    url: https://timereshared.com/stanford-waits/
    archived_url: null
    source_kind: preservation-history
    language: en
    date: '2025'
    primary: false
    notes: Used only for the broad operation interval.
  - id: stanford-sail
    title: 'Stanford Artificial Intelligence Lab: About'
    url: https://ai.stanford.edu/about/
    archived_url: null
    source_kind: institutional-history
    language: en
    date: current
    primary: false
    notes: Institutional identity context for SAIL.
  claims:
  - field: organizations
    value:
      organization: Stanford Artificial Intelligence Laboratory
      role: developer
    source_ids:
    - waits-manual
    - stanford-sail
    assertion_status: documented
    source_term: WAITS timesharing system at the Stanford Artificial Intelligence Laboratory
    scope: {}
    locator: Manual abstract; Stanford SAIL About page
    evidence_note: The primary manual names WAITS as the Stanford AI Lab system.
  - field: countries_of_origin
    value:
      country: US
      place: Stanford, California
    source_ids:
    - waits-manual
    - stanford-sail
    assertion_status: inferred
    source_term: Stanford Artificial Intelligence Laboratory
    scope: {}
    locator: Manual abstract; Stanford SAIL About page
    evidence_note: US origin is inferred from the sources' named Stanford developing institution.
  - field: design_purposes
    value:
      purpose: time-sharing
      primary: true
      source_term: operated exclusively as a timesharing system
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: operated exclusively as a timesharing system
    scope: {}
    locator: Manual Section 1 pp. 3-4
    evidence_note: The system is explicitly described as exclusively time-sharing.
  - field: development_status
    value:
      state: discontinued
      as_of: '1991'
    source_ids:
    - waits-history
    assertion_status: documented
    source_term: running continuously from 1966 to 1991
    scope:
      through: '1991'
    locator: Stanford WAITS opening summary
    evidence_note: The preservation history supplies the ending operation year.
  - field: lifecycle_events
    value:
      event: release
      date: '1982-03-21'
      precision: day
      qualifier: exact
      subject: WAITS 9.13/M
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: SU-AI WAITS 9.13/M Assembled 03/21/82
    scope: {}
    locator: Manual Section 1.4 p. 7
    evidence_note: The manual reproduces the logged-in monitor version and assembly date.
  - field: system_organization
    value:
      organization: resident-monitor
      source_term: timesharing monitor
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: monitor
    scope: {}
    locator: Manual Section 1 pp. 3-4
    evidence_note: The manual defines WAITS in monitor terms.
  - field: kernels
    value:
      name: WAITS monitor
      architecture: monitor
      source_term: monitor
      services:
      - resource allocation
      - I/O arbitration
      - UUOs
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: monitor
    scope: {}
    locator: Manual Section 1 pp. 3-4
    evidence_note: The monitor allocates core and I/O resources and provides services through UUOs.
  - field: interfaces
    value:
      name: WAITS monitor command interface
      style: command-line
      modalities:
      - keyboard
      - video-terminal
      provisioning: built-in
      access: local-session
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: typing commands to the monitor
    scope: {}
    locator: Manual Sections 1.3-1.4
    evidence_note: The manual describes keyboard/display terminals and monitor command decoding.
  - field: platforms
    value:
      platform: DEC PDP-10 KL-10
      role: native host
    source_ids:
    - waits-manual
    assertion_status: documented
    source_term: PDP-10 ... KL-10
    scope:
      releases:
      - WAITS 9.13/M
    locator: Manual Section 1.2
    evidence_note: The manual identifies the SAIL host as a DEC PDP-10 KL-10.
  editor_associations:
  - name: E
    relationship: bundled-default
    interface_style: full-screen-text
    scope:
      releases:
      - WAITS 9.13/M
    source_ids:
    - waits-manual
    assertion_status: documented
    locator: Manual Section 1 p. 4
    evidence_note: The manual says several editors are available and identifies E as the current favorite.
  unresolved:
  - field: rights_regime
    disposition: no-evidence-found
    reason: The manual and preservation history establish provenance but contain no WAITS software rights
      statement.
    source_ids:
    - waits-manual
    - waits-history
  - field: licenses
    disposition: no-evidence-found
    reason: No WAITS software license terms were found in the consulted sources.
    source_ids:
    - waits-manual
    - waits-history
  - field: programming_languages
    disposition: unknown
    reason: SAIL, LISP, FAIL, and MICRO-PLANNER are listed as user languages, not as the WAITS monitor
      implementation language.
    source_ids:
    - waits-manual
# END GENERATED DEEP RESEARCH
---

# WAITS

Draft inventory record; core factual research is pending.
