---
type: Operating System
title: V
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
names: [{ value: "V", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/V_(operating_system)
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: David Cheriton
    country_of_origin: null
    purpose: Research
    programming_languages: C
    first_release: 1981 ; 45 years ago ( 1981 )
    latest_release: Final / 1988 ; 38 years ago ( 1988 )
    last_updated: Final / 1988 ; 38 years ago ( 1988 )
    development_status: Discontinued
    source_model: null
    os_family: Distributed operating system
    gui: VGTS
    platforms: 'Workstations : SUN , MicroVAX , DEC Firefly'
    kernel_type: Microkernel
    license: Stanford University
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: ved
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://www.bitsavers.org/pdf/stanford/v-system/V_6.0refMan_Jun86.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  scope:
    releases:
    - '6.0'
    interfaces:
    - VGTS
  note: The command summary calls ved a text editor that runs under VGTS.
- name: vemacs
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://www.bitsavers.org/pdf/stanford/v-system/V_6.0refMan_Jun86.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  scope:
    releases:
    - '6.0'
    interfaces:
    - VGTS
  note: The command summary identifies vemacs as Emacs using VGTS window features.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-001
  researcher: deep_academic_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: This is Stanford's V-System/V distributed OS, not UNIX System V. Contemporary documentation
    describes a distributed kernel and external servers, C facilities, command executive, VGTS graphical
    terminal service, 1986 version 6.0, copyrighted software requiring a Stanford license, and ved/vemacs
    editors.
  sources:
  - id: v-cacm
    title: The V Distributed System
    url: https://graphics.stanford.edu/~tpurcell/quals/os/cher88.pdf
    archived_url: null
    source_kind: contemporary-scholarly-article
    language: en
    date: 1988-03
    primary: true
    notes: David R. Cheriton, Communications of the ACM 31(3), pp. 314-333.
  - id: v-manual
    title: V-System 6.0 Reference Manual
    url: https://www.bitsavers.org/pdf/stanford/v-system/V_6.0refMan_Jun86.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: '1986-06-17'
    primary: true
    notes: Contemporary manual preserved by Bitsavers.
  claims:
  - field: organizations
    value:
      organization: Stanford University
      role: developer
    source_ids:
    - v-cacm
    - v-manual
    assertion_status: documented
    source_term: developed at Stanford University
    scope: {}
    locator: Cheriton article p. 314; Manual Preface
    evidence_note: The article identifies Stanford as development site and the manual identifies the Stanford
      V-System trademark.
  - field: organizations
    value:
      organization: Defense Advanced Research Projects Agency
      role: funder
    source_ids:
    - v-cacm
    assertion_status: documented
    source_term: on-going support of the Defense Advanced Research Projects Agency
    scope: {}
    locator: Cheriton article p. 332 Acknowledgements
    evidence_note: Cheriton calls DARPA support central to the project.
  - field: countries_of_origin
    value:
      country: US
      place: Stanford/Palo Alto, California
    source_ids:
    - v-cacm
    - v-manual
    assertion_status: inferred
    source_term: Stanford University; Palo Alto, CA
    scope: {}
    locator: Cheriton article p. 314; Manual Installation Notes
    evidence_note: US origin follows from the named development institution and Palo Alto support address.
  - field: design_purposes
    value:
      purpose: distributed-computing
      primary: true
      source_term: research project to explore issues in distributed systems
    source_ids:
    - v-cacm
    assertion_status: documented
    source_term: research project to explore issues in distributed systems
    scope: {}
    locator: Cheriton article p. 314
    evidence_note: The article abstract directly states V's research purpose.
  - field: lifecycle_events
    value:
      event: release
      date: '1986-06-17'
      precision: day
      qualifier: exact
      subject: V-System 6.0
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: Version 6.0; 17 June 1986
    scope:
      releases:
      - '6.0'
    locator: Manual Preface and page footer
    evidence_note: The reference manual identifies the version and date.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: V software
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: All the software is under copyright protection
    scope:
      releases:
      - '6.0'
    locator: Manual Installation Notes
    evidence_note: The manual explicitly characterizes V software as copyrighted.
  - field: programming_languages
    value:
      language: C
      kind: high-level
      extent: substantial
      roles:
      - kernel
      - runtime
      - applications
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: C program development environment; Distributed V Kernel Kernel Ethernet driver
    scope:
      releases:
      - '6.0'
    locator: Manual Preface; Appendix B
    evidence_note: The manual documents C facilities and includes a C-style kernel driver excerpt, without
      claiming that every component was C.
  - field: system_organization
    value:
      organization: distributed-services
      source_term: distributed kernel and a distributed set of server processes
    source_ids:
    - v-manual
    - v-cacm
    assertion_status: documented
    source_term: distributed kernel
    scope: {}
    locator: Manual sections 1.3-1.3.2; Cheriton article p. 314
    evidence_note: Both sources describe per-node kernel copies plus external service processes.
  - field: kernels
    value:
      name: V distributed kernel
      architecture: microkernel
      source_term: distributed kernel
      services:
      - process management
      - IPC
      - low-level device management
      service_placement: other OS services outside kernel
    source_ids:
    - v-manual
    - v-cacm
    assertion_status: inferred
    source_term: All other operating system services are implemented as ... processes outside the kernel
    scope:
      releases:
      - '6.0'
    locator: Manual section 1.3.1; Cheriton article pp. 314-316
    evidence_note: Microkernel is an explicit classification inference from the documented minimal-kernel/external-server
      division; the sources use 'distributed kernel'.
  - field: interfaces
    value:
      name: V executive
      style: command-line
      modalities:
      - keyboard
      provisioning: built-in
      access: local-session
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: accepts user commands from the keyboard
    scope: {}
    locator: Manual section 3.1
    evidence_note: The executive is V's documented command interpreter.
  - field: interfaces
    value:
      name: Virtual Graphics Terminal Service (VGTS)
      style: graphical
      modalities:
      - keyboard
      - pointer
      provisioning: built-in
      access: local-session
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: window system; three-button mouse
    scope:
      releases:
      - '6.0'
    locator: Manual sections 1.2, 2.3, and 46
    evidence_note: VGTS provides graphical views/windows with keyboard and mouse input.
  - field: platforms
    value:
      platform: Sun workstations
      role: native host
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: runs on Sun ... workstations
    scope:
      releases:
      - '6.0'
    locator: Manual section 1.1
    evidence_note: The hardware-environment section identifies Sun support.
  - field: platforms
    value:
      platform: DEC VAXstation
      role: native host
    source_ids:
    - v-manual
    assertion_status: documented
    source_term: runs on ... VaxStation workstations
    scope:
      releases:
      - '6.0'
    locator: Manual section 1.1
    evidence_note: The hardware-environment section identifies VAXstation support.
  editor_associations:
  - name: ved
    relationship: bundled-default
    interface_style: full-screen-text
    scope:
      releases:
      - '6.0'
      interfaces:
      - VGTS
    source_ids:
    - v-manual
    assertion_status: documented
    locator: Manual Command Summary and chapter 14
    evidence_note: The command summary calls ved a text editor that runs under VGTS.
  - name: vemacs
    relationship: bundled-default
    interface_style: full-screen-text
    scope:
      releases:
      - '6.0'
      interfaces:
      - VGTS
    source_ids:
    - v-manual
    assertion_status: documented
    locator: Manual Command Summary
    evidence_note: The command summary identifies vemacs as Emacs using VGTS window features.
  unresolved:
  - field: development_status
    disposition: unknown
    reason: The 1986-88 sources show active work in their own periods but no authoritative current status
      or terminal development event was located.
    source_ids:
    - v-manual
    - v-cacm
  - field: licenses
    disposition: unknown
    reason: The manual says a Stanford license is required but does not reproduce operative terms or name
      a license.
    source_ids:
    - v-manual
# END GENERATED DEEP RESEARCH
---

# V

Draft inventory record; core factual research is pending.
