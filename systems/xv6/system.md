---
type: Operating System
title: Xv6
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
names: [{ value: "Xv6", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Xv6
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: MIT
    country_of_origin: United States
    purpose: null
    programming_languages: C and assembly
    first_release: null
    latest_release: 'RISC-V: rev5 / September 2, 2025 ; 10 months ago ( 2025-09-02
      ) x86-32 ( EOL ): rev11 / September 2, 2018 ; 7 years ago ( 2018-09-02 ) x86-64:
      rev1 / September 1, 2025 ; 10 months ago ( 2025-09-01 )'
    last_updated: 'RISC-V: rev5 / September 2, 2025 ; 10 months ago ( 2025-09-02 )
      x86-32 ( EOL ): rev11 / September 2, 2018 ; 7 years ago ( 2018-09-02 ) x86-64:
      rev1 / September 1, 2025 ; 10 months ago ( 2025-09-01 )'
    development_status: null
    source_model: Open source
    os_family: Unix-like
    gui: Command-line interface
    platforms: multiprocessor Intel x86 and RISC-V
    kernel_type: Monolithic
    license: MIT license
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q49108
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
  research_summary: Xv6 is MIT PDOS's Unix Version 6-inspired teaching OS. The official RISC-V book and
    repository document an ANSI C monolithic kernel, console shell, multi-core RISC-V target, MIT license,
    and a source change two days before this batch cutoff. No official bundled text editor was found.
  sources:
  - id: xv6-book
    title: 'xv6: a simple, Unix-like teaching operating system, revision 5'
    url: https://pdos.csail.mit.edu/6.1810/2025/xv6/book-riscv-rev5.pdf
    archived_url: null
    source_kind: official-system-manual
    language: en
    date: '2025-09-02'
    primary: true
    notes: MIT PDOS course text for xv6-riscv revision 5.
  - id: xv6-source
    title: mit-pdos/xv6-riscv source tree
    url: https://github.com/mit-pdos/xv6-riscv
    archived_url: null
    source_kind: official-source-tree
    language: en
    date: '2026-07-25'
    primary: true
    notes: Observed HEAD 59db7e2ea922cb1cf18e328b5b80f5264b0f755b, dated 2026-07-25.
  claims:
  - field: organizations
    value:
      organization: Massachusetts Institute of Technology
      role: developer
    source_ids:
    - xv6-book
    - xv6-source
    assertion_status: documented
    source_term: MIT's 6.828 and 6.1810; Massachusetts Institute of Technology
    scope: {}
    locator: Book Foreword p. 7; source LICENSE header
    evidence_note: The book identifies MIT courses using xv6 and the license names MIT as copyright holder.
  - field: countries_of_origin
    value:
      country: US
      place: Massachusetts Institute of Technology
    source_ids:
    - xv6-book
    - xv6-source
    assertion_status: inferred
    source_term: MIT
    scope: {}
    locator: Book Foreword p. 7; source LICENSE header
    evidence_note: US origin is inferred from MIT's documented development role.
  - field: design_purposes
    value:
      purpose: operating-systems-education
      primary: true
      source_term: teaching operating system
    source_ids:
    - xv6-book
    - xv6-source
    assertion_status: documented
    source_term: draft text intended for a class on operating systems
    scope: {}
    locator: Book Foreword p. 7; source README
    evidence_note: Both official sources define xv6's educational use.
  - field: development_status
    value:
      state: active
      basis: official source change on 2026-07-25
    source_ids:
    - xv6-source
    assertion_status: inferred
    source_term: commit 59db7e2
    scope:
      as_of: '2026-07-27'
      branch: riscv
    locator: Repository HEAD commit 59db7e2ea922cb1cf18e328b5b80f5264b0f755b
    evidence_note: Active status is inferred from a source change two days before the cutoff.
  - field: lifecycle_events
    value:
      event: last-source-change
      date: '2026-07-25'
      precision: day
      qualifier: exact
    source_ids:
    - xv6-source
    assertion_status: documented
    source_term: add CLINT to memlayout.h
    scope:
      branch: riscv
    locator: Repository commit 59db7e2ea922cb1cf18e328b5b80f5264b0f755b
    evidence_note: The observed HEAD provides the exact source-change date.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: software and associated documentation
    source_ids:
    - xv6-source
    assertion_status: documented
    source_term: Copyright (c) 2006-2024
    scope: {}
    locator: xv6-riscv LICENSE lines 1-3
    evidence_note: The official LICENSE identifies rights holders and covered material.
  - field: licenses
    value:
      name: MIT License
      spdx_expression: MIT
      scope: software and associated documentation
    source_ids:
    - xv6-source
    assertion_status: documented
    source_term: Permission is hereby granted, free of charge
    scope: {}
    locator: xv6-riscv LICENSE lines 5-21
    evidence_note: The standard MIT permission and warranty terms are present.
  - field: programming_languages
    value:
      language: ANSI C
      kind: high-level
      extent: primary
      roles:
      - kernel
    source_ids:
    - xv6-book
    assertion_status: documented
    source_term: implemented in ANSI C ... for a multi-core RISC-V
    scope:
      platforms:
      - RISC-V
    locator: Book Foreword p. 7
    evidence_note: The official book explicitly states the implementation language.
  - field: system_organization
    value:
      organization: distinct-kernel
      source_term: xv6 kernel
    source_ids:
    - xv6-book
    assertion_status: documented
    source_term: kernel implements the complete operating system
    scope: {}
    locator: Book section 2.3 p. 25
    evidence_note: The source distinguishes the kernel and OS interface.
  - field: kernels
    value:
      name: xv6 kernel
      architecture: monolithic
      source_term: monolithic kernel
    source_ids:
    - xv6-book
    assertion_status: documented
    source_term: Xv6 is implemented as a monolithic kernel
    scope:
      platforms:
      - RISC-V
    locator: Book section 2.3 p. 25
    evidence_note: The book directly gives the monolithic classification.
  - field: interfaces
    value:
      name: xv6 console shell
      style: command-line
      modalities:
      - keyboard
      - screen
      provisioning: bundled-default
      access: local-console
    source_ids:
    - xv6-book
    assertion_status: documented
    source_term: Then it starts a shell on the console
    scope: {}
    locator: Book section 2.6 p. 28
    evidence_note: Init opens the console and starts a shell.
  - field: platforms
    value:
      platform: multi-core RISC-V
      role: native target
    source_ids:
    - xv6-book
    - xv6-source
    assertion_status: documented
    source_term: multi-core RISC-V; Xv6 for RISC-V
    scope:
      branch: riscv
    locator: Book Foreword p. 7; source README
    evidence_note: Both official sources identify the maintained target.
  editor_associations: []
  unresolved:
  - field: text_editors
    disposition: no-evidence-found
    reason: The official user-program directory at the observed HEAD contains shell, file, test, and utility
      programs but no named text editor; the book documents a shell but no editor.
    source_ids:
    - xv6-book
    - xv6-source
# END GENERATED DEEP RESEARCH
---

# Xv6

Draft inventory record; core factual research is pending.
