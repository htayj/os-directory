---
type: Operating System
title: VxWorks
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
names: [{ value: "VxWorks", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/VxWorks
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Wind River (a wholly owned subsidiary of Aptiv )
    country_of_origin: United States
    purpose: Embedded systems
    programming_languages: null
    first_release: 1987 ; 39 years ago ( 1987 )
    latest_release: VxWorks 7 25.09 / August 22, 2025 ; 11 months ago ( 2025-08-22
      )
    last_updated: VxWorks 7 25.09 / August 22, 2025 ; 11 months ago ( 2025-08-22 )
    development_status: Current
    source_model: null
    os_family: Real-time operating systems
    gui: null
    platforms: x86 , x86-64 , MIPS , PowerPC , SH-4 , ARM , RISC-V
    kernel_type: Monolithic
    license: null
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q1746945
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: Visual Studio Code
  relationship: development-host-tool
  interface_style: graphical
  source: https://labs.windriver.com/downloads/wrsdk-vxworks7-docs/VxWorksSDK-ApplicationDeveloperGuide.html
  source_kind: official-sdk-manual
  assertion_status: documented
  scope:
    releases:
    - VxWorks 7 SDK
  note: The official VxWorks 7 SDK guide has a VS Code project-creation path; this
    is a host-side development relationship, not a claim that the editor runs or is
    bundled on every VxWorks target.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-002
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: VxWorks is Wind River's continuing commercial real-time operating-system lineage,
    introduced in 1987 in California. Current vendor material defines it around deterministic mission-critical
    embedded deployment, a kernel separated from protected user space, and a broad embedded processor/board
    range. It documents C/C++ as supported development languages but does not establish VxWorks' own implementation
    languages or publish a complete VxWorks license text in the consulted material.
  sources:
  - id: wind-vx-product
    title: 'VxWorks: The World''s #1 Real-Time Operating System'
    url: https://www.windriver.com/products/embedded/vxworks
    archived_url: null
    source_kind: official-product-page
    language: en
    date: '2026'
    primary: true
    notes: Current Wind River product page for the RTOS.
  - id: wind-vx-history
    title: Wind River Celebrates 30 Years of Embedded Innovation
    url: https://www.windriver.com/news/press/news-8961
    archived_url: null
    source_kind: vendor-history-press-release
    language: en
    date: '2011'
    primary: true
    notes: Wind River's own chronology says it was created in Berkeley, California and VxWorks was introduced
      in 1987.
  - id: wind-vx-datasheet
    title: 'VxWorks 7: The Safe, Secure, and Reliable RTOS'
    url: https://www.windriver.com/themes/Windriver/pdf/vxworks-7-datasheet.pdf
    archived_url: null
    source_kind: official-product-datasheet
    language: en
    date: '2019'
    primary: true
    notes: Vendor datasheet documents kernel/user-space separation, processor families, compiler/tool
      support, and the Eclipse development environment.
  - id: wind-vx-sdk-guide
    title: VxWorks SDK Application Developer Guide
    url: https://labs.windriver.com/downloads/wrsdk-vxworks7-docs/VxWorksSDK-ApplicationDeveloperGuide.html
    archived_url: null
    source_kind: official-sdk-manual
    language: en
    date: '2020'
    primary: true
    notes: Vendor SDK guide covers VxWorks application types and creating a project with VS Code or the
      command line.
  - id: wind-vx-public-source-notices
    title: Public Source Code - Downloads by Product
    url: https://www.windriver.com/source
    archived_url: null
    source_kind: official-source-notice-index
    language: en
    date: '2026'
    primary: true
    notes: Wind River's public source-download page is component-specific and does not publish a general
      VxWorks product license.
  claims:
  - field: organizations
    value:
      organization: Wind River
      role: developer
    source_ids:
    - wind-vx-product
    - wind-vx-history
    assertion_status: documented
    source_term: VxWorks
    scope: {}
    locator: Current product page; 30-year chronology
    evidence_note: Wind River presents VxWorks as its RTOS product and its own chronology dates the product's
      introduction to 1987.
  - field: countries_of_origin
    value:
      country: US
      place: Berkeley, California
      development_role: origin
    source_ids:
    - wind-vx-history
    assertion_status: documented
    source_term: created in a garage in Berkeley, Calif.
    scope:
      from: '1981'
      through: '1987'
    locator: Select company milestones
    evidence_note: Wind River says it was created in Berkeley, California in 1981 and introduced VxWorks
      in 1987, supporting the United States origin for the original product lineage.
  - field: design_purposes
    value:
      purpose: real-time-control
      primary: true
      source_term: mission-critical embedded systems
      traits:
      - deterministic-timing
      - safety-critical
    source_ids:
    - wind-vx-product
    assertion_status: documented
    source_term: Real-Time OS for Mission-Critical Systems
    scope: {}
    locator: Product-page heading and key capabilities
    evidence_note: Wind River says VxWorks targets mission-critical embedded systems and is designed for
      hard real time and deterministic performance.
  - field: development_status
    value:
      state: active
      as_of: '2026-07-27'
    source_ids:
    - wind-vx-product
    assertion_status: documented
    source_term: current product
    scope: {}
    locator: Current VxWorks product page
    evidence_note: Wind River actively markets and documents VxWorks as its current RTOS product.
  - field: lifecycle_events
    value:
      event: first-public-release
      date: '1987'
      release: VxWorks
    source_ids:
    - wind-vx-history
    assertion_status: documented
    source_term: VxWorks ... is introduced
    scope: {}
    locator: Select company milestones
    evidence_note: Wind River's vendor chronology dates VxWorks' introduction to 1987.
  - field: system_organization
    value:
      organization: distinct-kernel
      source_term: separation between kernel and memory-protected user space environments
    source_ids:
    - wind-vx-datasheet
    assertion_status: documented
    source_term: kernel and memory-protected user space
    scope:
      releases:
      - VxWorks 7
    locator: Key Features
    evidence_note: The VxWorks 7 datasheet explicitly distinguishes the kernel from memory-protected user-space
      environments.
  - field: interfaces
    value:
      name: VxWorks kernel shell
      style: command-line
      provisioning: bundled-optional
      access: administrative
    source_ids:
    - wind-vx-datasheet
    - wind-vx-sdk-guide
    assertion_status: documented
    source_term: VxWorks kernel shell; wrdbg shell
    scope:
      releases:
      - VxWorks 7
    locator: VxWorks 7 and Workbench Essentials course description; SDK guide, Connecting to a VxWorks
      Target
    evidence_note: Wind River describes a VxWorks kernel shell and its SDK documents command-line debugging
      through wrdbg and a target console.
  - field: platforms
    value:
      platform:
      - Arm
      - Power Architecture
      - Intel
      - RISC-V
      support_origin: vendor-port
      execution_mode: native
    source_ids:
    - wind-vx-datasheet
    assertion_status: documented
    source_term: broad spectrum of silicon architectures
    scope:
      releases:
      - VxWorks 7
    locator: Key Features, extensive processor and board support
    evidence_note: The vendor datasheet lists 32/64-bit support and Arm, Power Architecture, Intel, and
      RISC-V among supported architecture families.
  editor_associations:
  - name: Visual Studio Code
    relationship: development-host-tool
    interface_style: graphical
    source_ids:
    - wind-vx-sdk-guide
    assertion_status: documented
    scope:
      releases:
      - VxWorks 7 SDK
    locator: Application Developer Guide, Creating a Project with VSCode
    evidence_note: The official VxWorks 7 SDK guide has a VS Code project-creation path; this is a host-side
      development relationship, not a claim that the editor runs or is bundled on every VxWorks target.
  unresolved:
  - field: rights_regime
    disposition: unknown
    reason: The consulted vendor pages establish a commercial current product and list selected public
      source-component notices, but they do not state the copyright/public-domain characterization for
      the complete VxWorks product.
    source_ids:
    - wind-vx-product
    - wind-vx-public-source-notices
  - field: licenses
    disposition: no-evidence-found
    reason: No complete VxWorks end-user or source license was located in the consulted public Wind River
      documentation; the source-download page concerns individual included components, not a whole-product
      license.
    source_ids:
    - wind-vx-public-source-notices
    - wind-vx-product
  - field: programming_languages
    disposition: no-evidence-found
    reason: The datasheet documents C11, C++17, Rust, and Python as supported development languages and
      compilers, but that is not evidence of VxWorks implementation languages; no implementation language
      is inferred from the toolchain.
    source_ids:
    - wind-vx-datasheet
    - wind-vx-sdk-guide
  - field: kernels
    disposition: unknown
    reason: Wind River calls the component a kernel and documents its user-space separation, but the consulted
      current sources do not classify it as monolithic, microkernel, hybrid, or another normalized architecture
      for the cited release.
    source_ids:
    - wind-vx-datasheet
    - wind-vx-product
# END GENERATED DEEP RESEARCH
---

# VxWorks

Draft inventory record; core factual research is pending.
