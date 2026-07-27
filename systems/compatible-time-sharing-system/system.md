---
type: Operating System
title: Compatible Time-Sharing System
description: Draft operating-system identity pending core research.
tags: [operating-system]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Linked identity accepted for draft inventory; core facts remain unverified." }
field_dispositions: [{field: text_editors, disposition: documented, checked_at: '2026-07-26'}, {field: organizations, disposition: not-researched, checked_at: 2026-07-26}, {field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26}, {field: design_purposes, disposition: not-researched, checked_at: 2026-07-26}, {field: development_status, disposition: unknown, checked_at: 2026-07-26}, {field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26}, {field: rights_regime, disposition: not-researched, checked_at: 2026-07-26}, {field: licenses, disposition: not-researched, checked_at: 2026-07-26}, {field: programming_languages, disposition: not-researched, checked_at: 2026-07-26}, {field: system_organization, disposition: not-researched, checked_at: 2026-07-26}, {field: kernels, disposition: not-researched, checked_at: 2026-07-26}, {field: interfaces, disposition: not-researched, checked_at: 2026-07-26}, {field: platforms, disposition: not-researched, checked_at: 2026-07-26}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "Compatible Time-Sharing System", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: MIT Computation Center , Project MAC
    country_of_origin: United States
    purpose: Colleges and universities
    programming_languages: FAP assembly , MAD
    first_release: 1961 ; 65 years ago ( 1961 )
    latest_release: null
    last_updated: null
    development_status: Discontinued, simulator available
    source_model: Open source
    os_family: null
    gui: Command-line interface
    platforms: IBM 7090 , IBM 7094
    kernel_type: Monolithic , protected
    license: '[ data missing ]'
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q49108
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: ED
  relationship: bundled-default
  interface_style: line
  source: https://people.csail.mit.edu/saltzer/CTSS/CTSS-Documents/CTSS_ProgrammersGuide_1966.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  note: Listed as a context editor for card-image files.
- name: EDL
  relationship: bundled-default
  interface_style: line
  source: https://people.csail.mit.edu/saltzer/CTSS/CTSS-Documents/CTSS_ProgrammersGuide_1966.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  note: Listed as a context editor for line-marked files.
- name: QED
  relationship: bundled-default
  interface_style: line
  source: https://people.csail.mit.edu/saltzer/CTSS/CTSS-Documents/CTSS_ProgrammersGuide_1966.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  note: Listed as a programmable editor.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-001
  researcher: deep_academic_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: MIT's CTSS was a compatible time-sharing system developed at the Computation Center
    and Project MAC. Its 1965-69 guide documents a permanently resident supervisor on IBM 7094 hardware,
    and the 2011 participant overview dates the first demonstration to November 1961 and the Project MAC
    shutdown to May 1973.
  sources:
  - id: ctss-guide
    title: 'The Compatible Time-Sharing System: A Programmer''s Guide'
    url: https://people.csail.mit.edu/saltzer/CTSS/CTSS-Documents/CTSS_ProgrammersGuide_1966.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 1965-1969
    primary: true
    notes: MIT Computation Center guide, including sections revised through December 1969.
  - id: ctss-history
    title: 'The Compatible Time Sharing System (1961-1973): Fiftieth Anniversary Commemorative Overview'
    url: https://people.csail.mit.edu/saltzer/CTSS/CTSS-Documents/CTSS_50th_anniversary_web_03.pdf
    archived_url: null
    source_kind: participant-retrospective
    language: en
    date: '2011'
    primary: false
    notes: IEEE Computer Society History Committee overview, including accounts by CTSS participants.
  claims:
  - field: organizations
    value:
      organization: Massachusetts Institute of Technology Computation Center
      role: developer
    source_ids:
    - ctss-guide
    - ctss-history
    assertion_status: documented
    source_term: M.I.T. Computation Center
    scope:
      from: '1961'
    locator: Guide title leaf; History pp. 1-3
    evidence_note: The manual identifies the MIT Computation Center and the history says its staff began
      CTSS design in 1961.
  - field: organizations
    value:
      organization: MIT Project MAC
      role: developer
    source_ids:
    - ctss-guide
    - ctss-history
    assertion_status: documented
    source_term: Project MAC
    scope:
      from: '1963'
      through: '1973'
    locator: Guide Preface to Second Edition p. 1; History pp. 3, 12
    evidence_note: The guide identifies the Project MAC installation and the history dates its CTSS machine
      and shutdown.
  - field: countries_of_origin
    value:
      country: US
      place: Cambridge, Massachusetts
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: Massachusetts Institute of Technology, Cambridge, Massachusetts
    scope: {}
    locator: Guide title leaf
    evidence_note: The contemporary publisher and developer location is given directly.
  - field: design_purposes
    value:
      purpose: time-sharing
      primary: true
      source_term: concurrent, effective utilization of a single computer by several users
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: primary goal is concurrent, effective utilization of a single computer by several users
    scope: {}
    locator: Guide Section AA.0 pp. 1-2
    evidence_note: The guide contrasts CTSS's multi-user interactive purpose with batch processing.
  - field: development_status
    value:
      state: discontinued
      as_of: '1973'
    source_ids:
    - ctss-history
    assertion_status: documented
    source_term: it was time to retire the 7094s and CTSS
    scope:
      through: '1973'
    locator: History p. 3
    evidence_note: The Project MAC CTSS system was shut off in May 1973.
  - field: lifecycle_events
    value:
      event: first-demonstrated
      date: 1961-11
      precision: month
      qualifier: exact
    source_ids:
    - ctss-history
    assertion_status: documented
    source_term: first demonstrated in November of 1961
    scope: {}
    locator: History Preface p. ix
    evidence_note: The overview dates the original CTSS demonstration.
  - field: lifecycle_events
    value:
      event: development-ended
      date: 1973-05
      precision: month
      qualifier: exact
      subject: Project MAC CTSS
    source_ids:
    - ctss-history
    assertion_status: documented
    source_term: shut off in May 1973
    scope: {}
    locator: History p. 3
    evidence_note: This is the documented Project MAC terminal event.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: documentation
      rights_holder: Massachusetts Institute of Technology
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: Copyright 1965 by The Massachusetts Institute of Technology
    scope:
      components:
      - Programmer's Guide
    locator: Guide copyright page
    evidence_note: This establishes manual copyright only, not software license terms.
  - field: programming_languages
    value:
      language: FAP
      kind: assembly
      extent: supported-toolchain
      roles:
      - compiler-toolchain
      isa: IBM 7094
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: FAP, IBM 7094 Assembler
    scope: {}
    locator: Guide Section Table AH.2 entry .07
    evidence_note: FAP is listed as a CTSS language subsystem.
  - field: programming_languages
    value:
      language: MAD
      kind: high-level
      extent: supported-toolchain
      roles:
      - compiler-toolchain
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: MAD, Michigan Algorithm Decoder
    scope: {}
    locator: Guide Section Table AH.2 entry .10
    evidence_note: MAD is listed as a CTSS language subsystem, not assumed to implement all CTSS.
  - field: system_organization
    value:
      organization: supervisor-control-program
      source_term: supervisor program
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: entire operation ... under the control of a supervisor program
    scope: {}
    locator: Guide Section AA.0 p. 2
    evidence_note: The supervisor stays resident while controlling foreground and background work.
  - field: kernels
    value:
      name: CTSS supervisor program
      architecture: monitor
      source_term: supervisor program
      services:
      - traps
      - I/O
      - scheduling
      - swapping
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: supervisor program
    scope: {}
    locator: Guide Sections AA.0-AA.1
    evidence_note: The guide documents resident supervisory control of those operating-system services.
  - field: interfaces
    value:
      name: CTSS console command interface
      style: command-line
      modalities:
      - typewriter-terminal
      provisioning: built-in
      access: remote-session
    source_ids:
    - ctss-guide
    assertion_status: documented
    source_term: electric typewriters; standard commands
    scope: {}
    locator: Guide Section AA.0 p. 2
    evidence_note: Users issue standard commands from console typewriters.
  - field: platforms
    value:
      platform: IBM 7094
      role: native host
    source_ids:
    - ctss-guide
    - ctss-history
    assertion_status: documented
    source_term: CTSS IBM 7094
    scope: {}
    locator: Guide Sections AA.1 and AH.2; History pp. 5-8
    evidence_note: Both the manual and retrospective document the 7094 deployment.
  editor_associations:
  - name: ED
    relationship: bundled-default
    interface_style: line
    scope: {}
    source_ids:
    - ctss-guide
    assertion_status: documented
    locator: Guide Section Table AH.3 entry .02
    evidence_note: Listed as a context editor for card-image files.
  - name: QED
    relationship: bundled-default
    interface_style: line
    scope: {}
    source_ids:
    - ctss-guide
    assertion_status: documented
    locator: Guide Section Table AH.3 entry .09
    evidence_note: Listed as a programmable editor.
  - name: EDL
    relationship: bundled-default
    interface_style: line
    scope: {}
    source_ids:
    - ctss-guide
    assertion_status: documented
    locator: Guide Section Table AH.3 entry .07
    evidence_note: Listed as a context editor for line-marked files.
  unresolved:
  - field: licenses
    disposition: no-evidence-found
    reason: The manual supplies a documentation copyright notice and the historical overview has its own
      copyright, but neither gives CTSS software license terms.
    source_ids:
    - ctss-guide
    - ctss-history
# END GENERATED DEEP RESEARCH
---

# Compatible Time-Sharing System

Draft inventory record; core factual research is pending.
