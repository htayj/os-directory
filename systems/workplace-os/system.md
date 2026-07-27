---
type: Operating System
title: Workplace OS
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
names: [{ value: "Workplace OS", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Workplace_OS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: IBM
    country_of_origin: United States
    purpose: Global
    programming_languages: C , C++
    first_release: null
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: Closed source , Mach open source
    os_family: Universal
    gui: Workplace Shell
    platforms: PowerPC
    kernel_type: Microkernel
    license: null
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
- name: E
  relationship: bundled-optional
  interface_style: full-screen-text
  source: https://www.ibmfiles.com/ibmfiles/powerpc/os2ppc_first_look.pdf
  source_kind: contemporary-system-manual
  assertion_status: documented
  scope:
    editions:
    - OS/2 Warp Connect (PowerPC Edition) 1.0
    components:
    - MVM DOS environment
  note: IBM's table marks DOS E as added in the PowerPC Edition's DOS utility set
    and calls it a full-screen text editor; it is not generalized to the unshipped
    Workplace OS personalities.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-002
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Workplace OS names IBM's early-1990s microkernel/personality architecture and its
    limited PowerPC expression, not a normally released universal OS family. IBM's contemporaneous OS/2
    Warp Connect (PowerPC Edition) Redbook documents the IBM Microkernel, personality-neutral services,
    OS/2 dominant personality, command-line and Workplace Shell interface, PowerPC target, and a bundled
    DOS E editor. The broader promised personalities should not be treated as shipped editions.
  sources:
  - id: ibm-os2ppc-redbook
    title: 'OS/2 Warp (PowerPC Edition): A First Look, SG24-4630-00'
    url: https://www.ibmfiles.com/ibmfiles/powerpc/os2ppc_first_look.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 1995-12
    primary: true
    notes: Archived copy of an IBM International Technical Support Organization Redbook; it applies to
      OS/2 Warp Connect (PowerPC Edition) 1.0 and documents the IBM Microkernel architecture.
  - id: fleisch-workplace-case-study
    title: 'Workplace microkernel and OS: a case study'
    url: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-024X%28199805%2928%3A6%3C569%3A%3AAID-SPE158%3E3.0.CO%3B2-U
    archived_url: null
    source_kind: scholarly-case-study
    language: en
    date: '1998'
    primary: false
    notes: Peer-reviewed retrospective by former project participants; its abstract identifies the Workplace
      OS microkernel as the core component and describes its multiple-personality premise.
  - id: jhu-microkernel-paper
    title: Experience with the Development of a Microkernel-Based, Multiserver Operating System
    url: https://srl.cs.jhu.edu/courses/600.439/ExperienceMicrokernelBasedOS.pdf
    archived_url: null
    source_kind: technical-paper
    language: en
    date: '1997'
    primary: false
    notes: Technical paper describing the IBM Microkernel and the Workplace OS multiserver structure.
  claims:
  - field: organizations
    value:
      organization: IBM
      role: developer
    source_ids:
    - ibm-os2ppc-redbook
    - fleisch-workplace-case-study
    assertion_status: documented
    source_term: IBM Microkernel; IBM's Microkernel
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Redbook, chapters 1-2; case-study abstract
    evidence_note: IBM's contemporary architecture book names the IBM Microkernel, while the case study
      describes it as Workplace OS's core component.
  - field: countries_of_origin
    value:
      country: US
      place:
      - Boca Raton, Florida
      - Austin, Texas
      development_role: origin
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: IBM ... development, Boca Raton; IBM Microkernel development, Austin
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Acknowledgments, pages xviii-xix
    evidence_note: The IBM Redbook credits OS/2 PowerPC development in Boca Raton and IBM Microkernel
      development in Austin, both in the United States; the claim is scoped to the documented released
      expression.
  - field: design_purposes
    value:
      purpose: portability-research
      primary: true
      source_term: highly portable systems
      traits:
      - compatibility
      - extensibility
    source_ids:
    - ibm-os2ppc-redbook
    - fleisch-workplace-case-study
    assertion_status: documented
    source_term: multiple operating system personalities
    scope: {}
    locator: Redbook, Chapter 1 and Chapter 2, page 5; case-study abstract
    evidence_note: IBM says the microkernel structures system software for flexibility and portability
      and supports multiple personalities; the case study describes the intended concurrent personality
      platform.
  - field: development_status
    value:
      state: discontinued
      as_of: '2026-07-27'
    source_ids:
    - fleisch-workplace-case-study
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: case study; Version 1.0
    scope: {}
    locator: Case study, abstract and May 1998 publication; Redbook first edition, December 1995
    evidence_note: The post-project scholarly case study treats Workplace OS as a historical project,
      while the last identified IBM expression is the 1995 PowerPC Edition 1.0 documentation; no current
      product stream was found.
  - field: lifecycle_events
    value:
      event: first-public-release
      date: 1995-12
      release: OS/2 Warp Connect (PowerPC Edition) Version 1.0
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: First Edition (December 1995); applies to ... Version 1.0
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Title verso, pages i-ii
    evidence_note: IBM's contemporaneous Redbook states it applies to the Version 1.0 PowerPC Edition
      and is first published in December 1995; it is a limited expression of Workplace OS rather than
      evidence that all promised personalities shipped.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: documentation
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: Copyright International Business Machines Corporation 1995. All rights reserved.
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Title verso, copyright notice
    evidence_note: The IBM Redbook directly establishes copyright and restricted-rights status for the
      documented release material; it does not supply a complete software EULA.
  - field: system_organization
    value:
      organization: distinct-kernel
      source_term: microkernel services and dominant personality
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: IBM microkernel; personality-neutral services; dominant personality
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Chapter 2, pages 5-6; Chapter 3, microkernel services
    evidence_note: IBM documents a pure kernel plus user-level servers and a dominant OS/2 personality,
      rather than a single undifferentiated OS/2 kernel.
  - field: kernels
    value:
      name: IBM Microkernel
      architecture: microkernel
      source_term: pure kernel
    source_ids:
    - ibm-os2ppc-redbook
    - fleisch-workplace-case-study
    assertion_status: documented
    source_term: IBM Microkernel
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Redbook, Chapter 2, pages 5-6; case-study abstract
    evidence_note: IBM says its microkernel is implemented as a pure kernel with user-level servers; the
      later case study identifies that named microkernel as Workplace OS's core component.
  - field: interfaces
    value:
      name: Workplace Shell and OS/2 command line
      style:
      - graphical
      - command-line
      provisioning: built-in
      access: local-session
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: Workplace Shell; command line interface
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
      components:
      - OS/2 dominant personality
    locator: Chapter 4, sections 4.2.10 and 4.4 Graphics Subsystem Summary
    evidence_note: IBM says the PowerPC Edition continues to offer a command-line interface and that users
      see the OS/2 Workplace Shell desktop; this does not assert that every unshipped Workplace personality
      had that UI.
  - field: platforms
    value:
      platform: PowerPC-based machines
      support_origin: original-target
      execution_mode: native
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    source_term: PowerPC architecture
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
    locator: Chapter 1, Introduction, page 3
    evidence_note: The IBM document says OS/2 Warp Connect (PowerPC Edition) runs on PowerPC architecture
      systems and must be installed on a PowerPC-based machine.
  editor_associations:
  - name: E
    relationship: bundled-optional
    interface_style: full-screen-text
    source_ids:
    - ibm-os2ppc-redbook
    assertion_status: documented
    scope:
      editions:
      - OS/2 Warp Connect (PowerPC Edition) 1.0
      components:
      - MVM DOS environment
    locator: Chapter 4, Table 2, Changes to DOS Utilities, page 84
    evidence_note: IBM's table marks DOS E as added in the PowerPC Edition's DOS utility set and calls
      it a full-screen text editor; it is not generalized to the unshipped Workplace OS personalities.
  unresolved:
  - field: licenses
    disposition: no-evidence-found
    reason: The contemporary IBM material has a copyright and documentation restricted-rights notice but
      does not contain the applicable software license text for Workplace OS/OS/2 Warp Connect PowerPC
      Edition.
    source_ids:
    - ibm-os2ppc-redbook
  - field: programming_languages
    disposition: no-evidence-found
    reason: The Redbook documents standard C/C++ headers in a toolkit, which is application-development
      material rather than evidence of Workplace OS implementation languages; no OS implementation language
      is inferred.
    source_ids:
    - ibm-os2ppc-redbook
# END GENERATED DEEP RESEARCH
---

# Workplace OS

Draft inventory record; core factual research is pending.
