---
type: Operating System
title: z/VM
description: IBM virtual-machine operating-system lineage.
tags: [operating-system, ibm, mainframe, virtualization]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Linked identity accepted for draft inventory; core facts remain unverified." }
field_dispositions: [{field: text_editors, disposition: documented, checked_at: '2026-07-26'}, {field: organizations, disposition: not-researched, checked_at: 2026-07-26}, {field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26}, {field: design_purposes, disposition: not-researched, checked_at: 2026-07-26}, {field: development_status, disposition: unknown, checked_at: 2026-07-26}, {field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26}, {field: rights_regime, disposition: not-researched, checked_at: 2026-07-26}, {field: licenses, disposition: not-researched, checked_at: 2026-07-26}, {field: programming_languages, disposition: not-researched, checked_at: 2026-07-26}, {field: system_organization, disposition: not-researched, checked_at: 2026-07-26}, {field: kernels, disposition: not-researched, checked_at: 2026-07-26}, {field: interfaces, disposition: not-researched, checked_at: 2026-07-26}, {field: platforms, disposition: not-researched, checked_at: 2026-07-26}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "z/VM", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Z/VM
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: IBM
    country_of_origin: United States
    purpose: null
    programming_languages: null
    first_release: null
    latest_release: 7.4 / September 20, 2024 ; 22 months ago ( 2024-09-20 )
    last_updated: 7.4 / September 20, 2024 ; 22 months ago ( 2024-09-20 )
    development_status: Current
    source_model: Closed source
    os_family: VM family
    gui: null
    platforms: null
    kernel_type: null
    license: Proprietary
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
- name: XEDIT
  relationship: integral
  interface_style: full-screen-text
  source: https://www.ibm.com/support/pages/zvm/library/740pdfs.html
  source_kind: official-documentation-index
  assertion_status: documented
  scope:
    releases:
    - z/VM 7.4
    components:
    - CMS
  note: IBM's 7.4 library lists the XEDIT User's Guide, and its manual describes XEDIT
    as the IBM z/VM editor and both full-screen and line-mode text processing.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-002
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: IBM z/VM is the current IBM Z/LinuxONE virtual-machine operating-system and hypervisor
    product. Its documented base components include the Control Program (CP) and Conversational Monitor
    System (CMS); the current IBM library separately publishes the integral XEDIT editor. The consulted
    product material establishes current maintenance and platform scope, but not z/VM implementation languages
    or a development-location claim.
  sources:
  - id: ibm-zvm-general-74
    title: 'z/VM: 7.4 General Information, GC24-6286-74'
    url: https://www.ibm.com/support/pages/zvm/library/740pdfs/74628600.pdf
    archived_url: null
    source_kind: contemporary-system-manual
    language: en
    date: 2024-09
    primary: true
    notes: IBM product manual; product overview, CP/CMS component chapters, and server support appendix.
  - id: ibm-zvm-library-74
    title: IBM z/VM Library - 7.4 PDF files
    url: https://www.ibm.com/support/pages/zvm/library/740pdfs.html
    archived_url: null
    source_kind: official-documentation-index
    language: en
    date: '2026'
    primary: true
    notes: IBM's release-indexed library lists the 7.4 GA and subsequent component manuals, including
      XEDIT.
  - id: ibm-zvm-74-links
    title: IBM z/VM 7.4 links and more information
    url: https://www.ibm.com/support/pages/zvm/zvm740/links.html
    archived_url: null
    source_kind: official-release-information
    language: en
    date: '2024-09-20'
    primary: true
    notes: IBM release page gives the 7.4 ordering date and announcement resources.
  - id: ibm-zvm-74-changelog
    title: IBM z/VM 7.4 CMS Change Log
    url: https://www.ibm.com/support/pages/zvm/changelog/740/cms.html
    archived_url: null
    source_kind: official-change-log
    language: en
    date: '2026-07-07'
    primary: true
    notes: The current change log records 7.4 CMS feature-pack servicing in July 2026.
  - id: ibm-zvm-74-product
    title: z/VM 7.4.x release information
    url: https://www.ibm.com/support/pages/zvm74x
    archived_url: null
    source_kind: official-release-information
    language: en
    date: '2024-09-20'
    primary: true
    notes: IBM product release page identifies the IBM International Program License Agreement for this
      release.
  claims:
  - field: organizations
    value:
      organization: IBM
      role: developer
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: IBM z/VM licensed program
    scope:
      releases:
      - z/VM 7.4
    locator: About this document; page xi
    evidence_note: IBM identifies z/VM 7.4 as its licensed program and publishes the product manual.
  - field: design_purposes
    value:
      purpose: hardware-enablement
      primary: true
      source_term: premier hypervisor
      traits:
      - virtualization
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: premier hypervisor
    scope:
      releases:
      - z/VM 7.4
    locator: Chapter 1, z/VM overview, page 1
    evidence_note: IBM says z/VM hosts enterprise virtual servers and is designed to run hundreds to thousands
      of guests on IBM Z or LinuxONE.
  - field: development_status
    value:
      state: maintenance
      as_of: '2026-07-27'
    source_ids:
    - ibm-zvm-74-changelog
    assertion_status: documented
    source_term: service and feature packs
    scope:
      releases:
      - z/VM 7.4
    locator: 7.4 CMS change log, feature pack 07 fix 00, 2026-07-07
    evidence_note: IBM recorded a z/VM 7.4 CMS feature pack on July 7, 2026, establishing active product
      servicing at the catalog cutoff.
  - field: lifecycle_events
    value:
      event: release
      date: '2024-09-20'
      release: z/VM 7.4
    source_ids:
    - ibm-zvm-74-links
    assertion_status: documented
    source_term: z/VM 7.4 ordering begins
    scope:
      releases:
      - z/VM 7.4
    locator: Ordering and Availability
    evidence_note: IBM's 7.4 resource page dates ordering to September 17 and was last updated September
      20, 2024; its linked 7.4 GA manual is dated September 2024.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: binary
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: licensed program
    scope:
      releases:
      - z/VM 7.4
    locator: About this document; product identification
    evidence_note: IBM describes z/VM as a licensed program rather than a public-domain or source-distributed
      system.
  - field: licenses
    value:
      name: IBM International Program License Agreement
      scope: binary
      licensor: IBM
    source_ids:
    - ibm-zvm-74-product
    assertion_status: documented
    source_term: International Program License Agreement
    scope:
      releases:
      - z/VM 7.4
    locator: Release-information page, licensing link
    evidence_note: IBM's z/VM 7.4 release-information page links this product to the IBM International
      Program License Agreement.
  - field: system_organization
    value:
      organization: other
      source_term: Control Program (CP) and Conversational Monitor System (CMS)
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: Control Program (CP)
    scope:
      releases:
      - z/VM 7.4
    locator: Chapter 5, z/VM base product, pages 45 and 57
    evidence_note: IBM organizes the base product around CP and CMS; retaining those product terms is
      more precise than labeling the whole lineage a conventional monolithic kernel.
  - field: kernels
    value:
      name: Control Program (CP)
      architecture: other
      source_term: hypervisor
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: Control Program (CP); hypervisor
    scope:
      releases:
      - z/VM 7.4
    locator: Chapter 1, z/VM overview; Chapter 5, Control Program
    evidence_note: The manual calls z/VM a hypervisor and identifies CP as a base component; it does not
      classify CP using a modern monolithic/microkernel label.
  - field: interfaces
    value:
      name: CP/CMS
      style: command-line
      provisioning: built-in
      access: local-session
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: CP environment; CMS environment
    scope:
      releases:
      - z/VM 7.4
    locator: Chapter 5, CP and CMS component sections
    evidence_note: IBM documents CP and CMS as base z/VM components and provides their command documentation.
  - field: platforms
    value:
      platform: IBM Z and IBM LinuxONE servers
      support_origin: original-target
      execution_mode: native
    source_ids:
    - ibm-zvm-general-74
    assertion_status: documented
    source_term: IBM Z; IBM LinuxONE
    scope:
      releases:
      - z/VM 7.4
    locator: Chapter 1, z/VM overview; Appendix A
    evidence_note: IBM says z/VM runs guests on IBM Z and LinuxONE and supplies model-specific supported-server
      tables.
  editor_associations:
  - name: XEDIT
    relationship: integral
    interface_style: full-screen-text
    source_ids:
    - ibm-zvm-library-74
    - ibm-zvm-general-74
    assertion_status: documented
    scope:
      releases:
      - z/VM 7.4
      components:
      - CMS
    locator: z/VM 7.4 library, XEDIT User's Guide SC24-6338-74; General Information Chapter 5
    evidence_note: IBM's 7.4 library lists the XEDIT User's Guide, and its manual describes XEDIT as the
      IBM z/VM editor and both full-screen and line-mode text processing.
  unresolved:
  - field: countries_of_origin
    disposition: no-evidence-found
    reason: The IBM product and component manuals identify the vendor and current platform but do not
      establish the geographical location of original z/VM development; IBM's present corporate location
      is not a valid substitute.
    source_ids:
    - ibm-zvm-general-74
    - ibm-zvm-74-product
  - field: programming_languages
    disposition: no-evidence-found
    reason: The consulted manuals list a High Level Assembler prerequisite and application interfaces,
      not the implementation language(s) of CP, CMS, or the whole z/VM product; no language is inferred
      from those toolchain references.
    source_ids:
    - ibm-zvm-general-74
    - ibm-zvm-library-74
# END GENERATED DEEP RESEARCH
---

# z/VM

Draft inventory record; core factual research is pending.
