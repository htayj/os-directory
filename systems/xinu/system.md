---
type: Operating System
title: Xinu
description: Draft operating-system identity pending core research.
tags: [operating-system]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Linked identity accepted for draft inventory; core facts remain unverified." }
field_dispositions: [{field: text_editors, disposition: no-evidence-found, checked_at: '2026-07-26'}, {field: organizations, disposition: not-researched, checked_at: 2026-07-26}, {field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26}, {field: design_purposes, disposition: not-researched, checked_at: 2026-07-26}, {field: development_status, disposition: unknown, checked_at: 2026-07-26}, {field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26}, {field: rights_regime, disposition: not-researched, checked_at: 2026-07-26}, {field: licenses, disposition: not-researched, checked_at: 2026-07-26}, {field: programming_languages, disposition: not-researched, checked_at: 2026-07-26}, {field: system_organization, disposition: not-researched, checked_at: 2026-07-26}, {field: kernels, disposition: not-researched, checked_at: 2026-07-26}, {field: interfaces, disposition: not-researched, checked_at: 2026-07-26}, {field: platforms, disposition: not-researched, checked_at: 2026-07-26}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "Xinu", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Xinu
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Douglas Comer
    country_of_origin: null
    purpose: Higher education , embedded systems
    programming_languages: C
    first_release: 1981 ; 45 years ago ( 1981 )
    latest_release: 3rd ed. / 2025 ; 1 year ago ( 2025 )
    last_updated: 3rd ed. / 2025 ; 1 year ago ( 2025 )
    development_status: Current
    source_model: Open source
    os_family: null
    gui: Command-line interface
    platforms: null
    kernel_type: null
    license: null
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: no-evidence-found
  note: No editor relationship was found in the linked Wikipedia page or direct Wikidata
    text-editor platform statements; primary manuals and distribution manifests still
    require research.
text_editors: []
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-001
  researcher: deep_academic_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Xinu is Douglas Comer's small operating-system lineage hosted at Purdue for teaching,
    research, and embedded work. Official material provides x86, ARM, and VirtualBox variants, a shell
    and serial-console workflow, source examples, and a custom copyright/permission notice; it does not
    establish a named editor or a kernel architecture.
  sources:
  - id: xinu-page
    title: The Xinu Page
    url: https://xinu.cs.purdue.edu/
    archived_url: null
    source_kind: official-project-documentation
    language: en
    date: current
    primary: true
    notes: Purdue-hosted description, timeline, lab, and platform documentation.
  - id: xinu-source
    title: Source files for Operating System Design — The Xinu Approach
    url: https://www.cs.purdue.edu/homes/comer/downloads/Xinu_Book_And_Code/view_source_code/
    archived_url: null
    source_kind: official-source-tree
    language: en
    date: current
    primary: true
    notes: Purdue source browser maintained through the textbook-author contact.
  - id: xinu-license
    title: License information for Xinu software
    url: https://www.cs.purdue.edu/homes/dec/xlicense.html
    archived_url: null
    source_kind: official-license-notice
    language: en
    date: '2015'
    primary: true
    notes: Copyright and permission terms for covered portions of Xinu.
  claims:
  - field: organizations
    value:
      organization: Purdue University Computer Science Department
      role: maintainer
    source_ids:
    - xinu-page
    - xinu-source
    assertion_status: documented
    source_term: Xinu Lab at Purdue
    scope: {}
    locator: Xinu Page, Xinu Lab at Purdue; source-browser footer
    evidence_note: Purdue hosts the Xinu lab and source browser.
  - field: organizations
    value:
      organization: CRC Press, Inc.
      role: rights-holder
    source_ids:
    - xinu-license
    assertion_status: documented
    source_term: Copyright (c) 2012, 2015 Douglas E. Comer and CRC Press, Inc.
    scope:
      components:
      - covered portions
    locator: License notice paragraph 1
    evidence_note: CRC Press is a stated joint copyright holder for covered portions.
  - field: countries_of_origin
    value:
      country: US
      place: Purdue University
    source_ids:
    - xinu-page
    assertion_status: inferred
    source_term: Xinu Lab at Purdue University
    scope:
      from: '1979'
    locator: Xinu Page Development Timeline and Xinu Lab section
    evidence_note: US origin is inferred from the Purdue project origin.
  - field: design_purposes
    value:
      purpose: operating-systems-education
      primary: true
      source_term: used for both teaching and research
    source_ids:
    - xinu-page
    assertion_status: documented
    source_term: used for both teaching and research
    scope: {}
    locator: Xinu Page, Xinu Lab at Purdue
    evidence_note: The official lab is explicitly for teaching and research.
  - field: design_purposes
    value:
      purpose: embedded-control
      primary: false
      source_term: suitable for embedded environments
    source_ids:
    - xinu-page
    assertion_status: documented
    source_term: The small size makes Xinu suitable for embedded environments
    scope: {}
    locator: Xinu Page, Description
    evidence_note: The official description gives embedded suitability.
  - field: development_status
    value:
      state: active
      basis: current official source distribution and 2025 edition
    source_ids:
    - xinu-page
    - xinu-source
    assertion_status: inferred
    source_term: Third Edition 2025; several recent versions
    scope:
      as_of: '2026-07-27'
    locator: Xinu Page Textbook and Experimenting sections; source-browser overview
    evidence_note: Active status is inferred from current official source availability and 2025 edition
      evidence, not a stated status label.
  - field: lifecycle_events
    value:
      event: development-started
      date: '1979'
      precision: year
      qualifier: range
    source_ids:
    - xinu-page
    assertion_status: documented
    source_term: 1979-80 ... project starts
    scope: {}
    locator: Xinu Page Development Timeline 1979-80
    evidence_note: The timeline says the project began to explore integrating network protocol software
      into an OS.
  - field: lifecycle_events
    value:
      event: release
      date: '2025'
      precision: year
      qualifier: exact
      subject: third edition
    source_ids:
    - xinu-page
    assertion_status: documented
    source_term: Third Edition ... 2025
    scope: {}
    locator: Xinu Page Textbook
    evidence_note: The official page says the revised third edition is in print.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: covered software portions
      rights_holders:
      - Douglas E. Comer
      - CRC Press, Inc.
    source_ids:
    - xinu-license
    assertion_status: documented
    source_term: Copyright (c) 2012, 2015 Douglas E. Comer and CRC Press, Inc.
    scope: {}
    locator: License notice paragraph 1
    evidence_note: The notice expressly limits coverage to portions of the Xinu software.
  - field: licenses
    value:
      name: Xinu software permission notice
      spdx_expression: null
      scope: covered software portions
      software_freedom_status: source-available-nonfree
    source_ids:
    - xinu-license
    assertion_status: documented
    source_term: Redistribution and use in source and binary forms ... are permitted
    scope: {}
    locator: License notice paragraphs 1-2
    evidence_note: The custom permission includes textbook-publication and charging restrictions, so it
      is not assigned an SPDX or OSI label.
  - field: programming_languages
    value:
      language: C
      kind: high-level
      extent: substantial
      roles:
      - kernel
      - utilities
    source_ids:
    - xinu-source
    assertion_status: inferred
    source_term: source files ... common_files/freebuf.c
    scope: {}
    locator: Purdue Xinu Source Browser all-version view
    evidence_note: C is inferred from official .c implementation files; no precise language proportion
      is claimed.
  - field: interfaces
    value:
      name: Xinu shell and serial console
      style: command-line
      modalities:
      - serial-terminal
      provisioning: built-in
      access: local-console
    source_ids:
    - xinu-page
    assertion_status: documented
    source_term: a shell; console serial connection
    scope: {}
    locator: Xinu Page Description and Experimenting sections
    evidence_note: The page lists a shell and gives serial-console startup procedures.
  - field: platforms
    value:
      platform: Intel x86 / Galileo board
      role: teaching target
    source_ids:
    - xinu-page
    - xinu-source
    assertion_status: documented
    source_term: X86 version (the Galileo board)
    scope: {}
    locator: Xinu Page Experimenting section; source-browser overview
    evidence_note: Both official sources name this target.
  - field: platforms
    value:
      platform: ARM / BeagleBone Black
      role: teaching target
    source_ids:
    - xinu-page
    - xinu-source
    assertion_status: documented
    source_term: ARM version (the BeagleBone Black board)
    scope: {}
    locator: Xinu Page Experimenting section; source-browser overview
    evidence_note: Both official sources name this target.
  - field: platforms
    value:
      platform: Oracle VirtualBox
      role: hosted virtual target
    source_ids:
    - xinu-page
    - xinu-source
    assertion_status: documented
    source_term: VirtualBox hypervisor
    scope: {}
    locator: Xinu Page Experimenting section; source-browser overview
    evidence_note: The project page describes a VM version and the source browser provides its view.
  editor_associations: []
  unresolved:
  - field: system_organization
    disposition: no-evidence-found
    reason: The official page calls Xinu an OS and refers to a kernel version but does not document a
      controlled-vocabulary organization.
    source_ids:
    - xinu-page
    - xinu-source
  - field: kernels
    disposition: no-evidence-found
    reason: No named architecture, module placement, or protection model is documented by the consulted
      official sources.
    source_ids:
    - xinu-page
    - xinu-source
  - field: text_editors
    disposition: no-evidence-found
    reason: The official material describes an edit-compile-download-test workflow but names no bundled,
      native, or supported text editor.
    source_ids:
    - xinu-page
    - xinu-source
# END GENERATED DEEP RESEARCH
---

# Xinu

Draft inventory record; core factual research is pending.
