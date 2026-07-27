---
type: Operating System
title: Z80-RIO
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
names: [{ value: "Z80-RIO", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Z80-RIO
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Zilog
    country_of_origin: null
    purpose: null
    programming_languages: null
    first_release: null
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: Closed source
    os_family: null
    gui: Command-line interface
    platforms: Zilog Z80
    kernel_type: null
    license: Proprietary
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: RIO Text Editor
  relationship: bundled-default
  interface_style: command-line
  source: https://www.bitsavers.org/pdf/zilog/mcz-1/03-0072-01A_Z80_RIO_Operating_System_Users_Manual_Sep78.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  scope:
    releases:
    - RIO Revision A
    components:
    - enhanced environment
  note: The enhanced environment's disk-resident software includes a text editor.
    Its dedicated manual calls it a line-oriented editor with string handling and
    automatic disk interface.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-003
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Z80-RIO (the Z80 Operating System with Relocatable Modules and I/O Management) is
    Zilog's general-purpose development and production system for the MCZ and ZDS families. Its 1978 manual
    distinguishes a small PROM-resident environment from an enhanced environment centred on the RIO Executive,
    disk file systems, command processing, and disk-resident development tools. The manual copyright establishes
    a copyrighted documentation/product context, but the consulted material does not establish a product
    license, development location, implementation language, or an end-of-life announcement.
  sources:
  - id: zilog-rio-os-manual-1978
    title: Z80-RIO Operating System User's Manual, Revision A
    url: https://www.bitsavers.org/pdf/zilog/mcz-1/03-0072-01A_Z80_RIO_Operating_System_Users_Manual_Sep78.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 1978-09
    primary: true
    notes: Zilog's original RIO operating-system manual; it defines the name expansion, target systems,
      Executive, console, command, and file-system components.
  - id: zilog-rio-editor-manual-1980
    title: Z80-RIO Text Editor User's Manual
    url: https://www.bitsavers.org/pdf/zilog/mcz-1/03-0074-00B_Z80-RIO_Text_Editor_Users_Manual_Sep80.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 1980-09
    primary: true
    notes: Zilog editor manual for the RIO text editor.
  - id: zilog-mcs-brochure-de-1978
    title: Mikrocomputer Applikationssammlung 77/78
    url: https://bitsavers.org/components/zilog/1977_1978_Zilog_Mikrocomputer_Applikationssammlung--GERMAN.pdf
    archived_url: null
    source_kind: contemporary-vendor-brochure
    language: de
    date: 1977-1978
    primary: true
    notes: German-language Zilog brochure describing Z80-RIO for the MCS as modular, transparent operating
      software and listing development-language products that run under RIO.
  - id: computerwoche-rio-1978
    title: 'Zilog GmbH: IBM-like mit RIO-Unterstützung'
    url: https://www.computerwoche.de/article/2872702/zilog-gmbh-ibm-like-mit-rio-unterstuetzung.html
    archived_url: null
    source_kind: contemporary-trade-press
    language: de
    date: '1978'
    primary: false
    notes: German contemporary report referring to RIO as Relocatable Input Output support for the MCZ-1
      expansion family.
  claims:
  - field: organizations
    value:
      organization: Zilog, Inc.
      role: developer and publisher
    source_ids:
    - zilog-rio-os-manual-1978
    - zilog-rio-editor-manual-1980
    assertion_status: documented
    source_term: Zilog
    scope:
      releases:
      - RIO Revision A
    locator: Operating System User's Manual, title page and copyright page
    evidence_note: Both contemporary manuals identify Zilog as publisher; the operating-system manual
      describes the Zilog product and its supplied software.
  - field: design_purposes
    value:
      purpose: software-development and production integration
      primary: true
      source_term: development and integration of user's programs into a production environment
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: general-purpose computing system
    scope:
      releases:
      - RIO Revision A
    locator: Chapter 1.1, Introduction, page 1
    evidence_note: Zilog describes RIO as a general-purpose system designed to facilitate development
      and integration of user programs into production.
  - field: lifecycle_events
    value:
      event: release
      date: 1978-09
      release: Z80-RIO Revision A
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: Revision A, September 1978
    scope:
      releases:
      - RIO Revision A
    locator: Manual cover and publication page
    evidence_note: The original manual is dated September 1978 and labelled Revision A; this establishes
      a documented release-era artifact, not necessarily the first public release.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: documentation
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: Copyright 1978 by Zilog, Inc. All rights reserved.
    scope:
      releases:
      - RIO Revision A
    locator: Copyright page
    evidence_note: The RIO manual explicitly reserves rights in the manual. This does not establish a
      binary or source-code license.
  - field: system_organization
    value:
      organization: executive
      source_term: RIO Executive
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: RIO Executive (OS)
    scope:
      releases:
      - RIO Revision A
      components:
      - enhanced environment
    locator: Chapter 1.1, pages 1-2; Chapter 2, page 9
    evidence_note: The enhanced environment includes the RIO Executive, which initializes the console
      and primary file system and manages memory and standardized I/O.
  - field: kernels
    value:
      name: RIO Executive
      architecture: executive
      source_term: RIO Executive (OS)
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: Executive (OS)
    scope:
      releases:
      - RIO Revision A
      components:
      - enhanced environment
    locator: Chapter 2.1, System Initialization, page 9
    evidence_note: Zilog calls the OS core the RIO Executive and documents its initialization, memory-manager,
      command-interpreter, and I/O-management responsibilities.
  - field: interfaces
    value:
      name: RIO command input
      style: command-line
      provisioning: built-in
      access: local-console
    source_ids:
    - zilog-rio-os-manual-1978
    assertion_status: documented
    source_term: command prompt character %; command string interpreter
    scope:
      releases:
      - RIO Revision A
    locator: Chapter 2.1 and 2.4, pages 9 and 13
    evidence_note: After initialization RIO prints a prompt and waits for command input; the following
      section specifies command-string interpretation.
  - field: platforms
    value:
      platform: Zilog MCZ Micro Computer System and ZDS Development System
      support_origin: original-target
      execution_mode: native
    source_ids:
    - zilog-rio-os-manual-1978
    - zilog-mcs-brochure-de-1978
    assertion_status: documented
    source_term: MCZ-1 series; ZDS; MCS
    scope:
      releases:
      - RIO Revision A
    locator: Operating System User's Manual, Chapter 1.1-1.2, pages 1-3; German brochure, Z80-RIO section
    evidence_note: The English manual names MCZ and ZDS hardware configurations; the German brochure independently
      identifies RIO for the MCS.
  editor_associations:
  - name: RIO Text Editor
    relationship: bundled-default
    interface_style: command-line
    source_ids:
    - zilog-rio-os-manual-1978
    - zilog-rio-editor-manual-1980
    assertion_status: documented
    scope:
      releases:
      - RIO Revision A
      components:
      - enhanced environment
    locator: Operating System User's Manual, Chapter 1.1, page 1; Text Editor User's Manual, Introduction,
      page 1
    evidence_note: The enhanced environment's disk-resident software includes a text editor. Its dedicated
      manual calls it a line-oriented editor with string handling and automatic disk interface.
  unresolved:
  - field: countries_of_origin
    disposition: no-evidence-found
    reason: The manuals identify Zilog and target hardware, while the German material identifies a German
      sales context, but none establishes the geographical location where RIO was originally developed.
    source_ids:
    - zilog-rio-os-manual-1978
    - computerwoche-rio-1978
  - field: development_status
    disposition: no-evidence-found
    reason: The consulted contemporary manuals establish dated releases but contain no maintenance, termination,
      or support-status statement that can safely establish the current historical lifecycle state.
    source_ids:
    - zilog-rio-os-manual-1978
    - zilog-rio-editor-manual-1980
  - field: licenses
    disposition: no-evidence-found
    reason: The manual copyright notice is not a software license or redistribution grant for RIO binaries
      or source code.
    source_ids:
    - zilog-rio-os-manual-1978
  - field: programming_languages
    disposition: no-evidence-found
    reason: The German brochure lists BASIC, COBOL, FORTRAN, and PL/Z products that run under RIO; those
      are user toolchains and do not establish RIO's implementation language.
    source_ids:
    - zilog-mcs-brochure-de-1978
    - zilog-rio-os-manual-1978
# END GENERATED DEEP RESEARCH
---

# Z80-RIO

Draft inventory record; core factual research is pending.
