---
type: Operating System
title: Windows IoT
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
names: [{ value: "Windows IoT", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Windows_IoT
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Microsoft
    country_of_origin: United States
    purpose: null
    programming_languages: null
    first_release: null
    latest_release: null
    last_updated: null
    development_status: null
    source_model: Closed-source Source-available (through Shared Source Initiative
      )
    os_family: Microsoft Windows
    gui: null
    platforms: null
    kernel_type: Hybrid kernel
    license: Commercial proprietary software
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q2283
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: Visual Studio
  relationship: development-host-tool
  interface_style: graphical
  source: https://learn.microsoft.com/en-us/archive/msdn-magazine/2017/may/internet-of-things-working-with-raspberry-pi-and-windows-10
  source_kind: official-developer-article
  assertion_status: documented
  scope:
    editions:
    - Windows 10 IoT Core
    platforms:
    - Raspberry Pi
  note: Microsoft's IoT Core guide directs developers to install Visual Studio's Universal
    Windows App tools and create a UWP project; it is a development-host association,
    not a claim that Visual Studio is installed on the device.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-002
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Windows IoT is Microsoft’s family label, formerly Windows Embedded, rather than a
    single uniform kernel release. It includes discontinued Windows 10 IoT Core and currently supported
    Windows IoT Enterprise streams with different interfaces, licensing, and lifecycle. This result scopes
    claims to the documented edition and does not infer Windows internals or languages from the public
    platform APIs.
  sources:
  - id: ms-windows-iot-docs
    title: Windows for IoT Documentation
    url: https://learn.microsoft.com/en-us/windows/iot/
    archived_url: null
    source_kind: official-product-documentation
    language: en
    date: '2026'
    primary: true
    notes: Microsoft describes Windows for IoT as a family of operating systems formerly called Windows
      Embedded.
  - id: ms-iot-enterprise-overview
    title: What is Windows IoT Enterprise?
    url: https://learn.microsoft.com/en-us/windows/iot/iot-enterprise/overview
    archived_url: null
    source_kind: official-product-documentation
    language: en
    date: '2026-02-26'
    primary: true
    notes: Microsoft definition, intended fixed-purpose use, binary equivalence to Windows Enterprise,
      and servicing model.
  - id: ms-iot-enterprise-lifecycle
    title: Windows 11 IoT Enterprise - Microsoft Lifecycle
    url: https://learn.microsoft.com/en-us/lifecycle/products/windows-11-iot-enterprise
    archived_url: null
    source_kind: official-lifecycle-record
    language: en
    date: '2026'
    primary: true
    notes: Official current support table for the Windows 11 IoT Enterprise stream.
  - id: ms-iot-announcement-2015
    title: 'Windows 10 IoT: Powering the Internet of Things'
    url: https://blogs.windows.com/windowsexperience/2015/03/18/windows-10-iot-powering-the-internet-of-things/
    archived_url: null
    source_kind: official-announcement
    language: en
    date: '2015-03-18'
    primary: true
    notes: Microsoft announcement of the Windows 10 IoT offering and intended device categories.
  - id: ms-iot-enterprise-license
    title: 'Microsoft Software License Terms: Windows IoT Enterprise (All Editions)'
    url: https://learn.microsoft.com/en-us/windows/iot/iot-enterprise/eula/license_en-us_english_united_states.pdf
    archived_url: null
    source_kind: official-license
    language: en
    date: 2024-04
    primary: true
    notes: Microsoft's Windows IoT Enterprise EULA; it reserves rights not expressly granted and sets
      copy/transfer restrictions.
  - id: ms-iot-core-maker
    title: Microsoft brings Windows 10 to Makers
    url: https://blogs.windows.com/windowsdeveloper/2015/04/29/microsoft-brings-windows-10-to-makers/
    archived_url: null
    source_kind: official-announcement
    language: en
    date: '2015-04-29'
    primary: true
    notes: Windows 10 IoT Core preview announcement identifies Raspberry Pi 2 and Intel MinnowBoard Max
      support.
  - id: ms-iot-core-rpi
    title: Working with Raspberry Pi and Windows 10
    url: https://learn.microsoft.com/en-us/archive/msdn-magazine/2017/may/internet-of-things-working-with-raspberry-pi-and-windows-10
    archived_url: null
    source_kind: official-developer-article
    language: en
    date: 2017-05
    primary: true
    notes: Microsoft developer article documents the IoT Core Dashboard, Device Portal, remote control,
      and Visual Studio UWP development.
  claims:
  - field: organizations
    value:
      organization: Microsoft
      role: developer
    source_ids:
    - ms-windows-iot-docs
    - ms-iot-announcement-2015
    assertion_status: documented
    source_term: Windows for IoT; Microsoft
    scope: {}
    locator: Windows for IoT documentation landing page; 2015 announcement by Microsoft Operating Systems
      Group
    evidence_note: Microsoft's documentation identifies Windows for IoT as its operating-system family
      and its operating-systems group announced the Windows 10 IoT offering.
  - field: design_purposes
    value:
      purpose: embedded-control
      primary: true
      source_term: fixed purpose devices
      application_domains:
      - ATMs
      - point-of-sale
      - industrial automation
      - medical devices
      - kiosks
    source_ids:
    - ms-iot-enterprise-overview
    - ms-iot-announcement-2015
    assertion_status: documented
    source_term: fixed purpose devices; intelligent, connected IoT devices
    scope:
      editions:
      - Windows IoT Enterprise
      - Windows 10 IoT
    locator: Windows IoT Enterprise overview, Fixed Purpose Devices; 2015 announcement
    evidence_note: Microsoft says the Enterprise line is for fixed-purpose devices and announced Windows
      10 IoT for connected gateways, point of sale, robotics, and specialty medical devices.
  - field: development_status
    value:
      state: active
      as_of: '2026-07-27'
      edition: Windows 11 IoT Enterprise
    source_ids:
    - ms-iot-enterprise-lifecycle
    assertion_status: documented
    source_term: In Support
    scope:
      editions:
      - Windows 11 IoT Enterprise
    locator: Support Dates
    evidence_note: Microsoft's lifecycle record lists Windows 11 IoT Enterprise as in support; this does
      not project support to discontinued Windows IoT Core.
  - field: lifecycle_events
    value:
      event: announced
      date: '2015-03-18'
      release: Windows 10 IoT
    source_ids:
    - ms-iot-announcement-2015
    assertion_status: documented
    source_term: Windows 10 IoT
    scope:
      editions:
      - Windows 10 IoT
    locator: Announcement date and opening paragraphs
    evidence_note: Microsoft publicly described Windows 10 IoT and the intended summer 2015 availability
      on March 18, 2015.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: binary
      edition: Windows IoT Enterprise
    source_ids:
    - ms-iot-enterprise-license
    assertion_status: documented
    source_term: reserve all rights ... not expressly granted
    scope:
      editions:
      - Windows IoT Enterprise
    locator: License Terms, section 1(c), Restrictions
    evidence_note: Microsoft's EULA reserves intellectual-property rights not expressly granted, establishing
      a copyrighted proprietary regime for the cited Enterprise editions.
  - field: licenses
    value:
      name: 'Microsoft Software License Terms: Windows IoT Enterprise (All Editions)'
      scope: binary
      licensor: Microsoft
    source_ids:
    - ms-iot-enterprise-license
    assertion_status: documented
    source_term: MICROSOFT SOFTWARE LICENSE TERMS WINDOWS IOT ENTERPRISE (ALL EDITIONS)
    scope:
      editions:
      - Windows IoT Enterprise
    locator: Title and section 1(c)
    evidence_note: The official EULA covers Windows IoT Enterprise editions and restricts copying, transfer,
      separate feature use, and circumvention.
  - field: interfaces
    value:
      name: Windows IoT Core Device Portal and remote PowerShell
      style: command-line
      provisioning: bundled-default
      access: remote-session
    source_ids:
    - ms-iot-core-rpi
    assertion_status: documented
    source_term: Device Portal; remote PowerShell; headless mode
    scope:
      editions:
      - Windows 10 IoT Core
    locator: Working with Raspberry Pi and Windows 10, Device Portal and Developing for the Raspberry
      Pi
    evidence_note: Microsoft documents IoT Core's browser-accessible Device Portal, remote control, headless
      use, and remote PowerShell; this scoped claim avoids treating all Windows IoT editions as headless.
  - field: platforms
    value:
      platform:
      - Raspberry Pi 2
      - Intel MinnowBoard Max
      support_origin: official-port
      execution_mode: native
    source_ids:
    - ms-iot-core-maker
    assertion_status: documented
    source_term: Windows 10 IoT Core Insider Preview
    scope:
      editions:
      - Windows 10 IoT Core preview
    locator: Opening announcement paragraphs
    evidence_note: Microsoft announced IoT Core preview support for Raspberry Pi 2 and Intel MinnowBoard
      Max; the old board-specific scope is retained.
  editor_associations:
  - name: Visual Studio
    relationship: development-host-tool
    interface_style: graphical
    source_ids:
    - ms-iot-core-rpi
    assertion_status: documented
    scope:
      editions:
      - Windows 10 IoT Core
      platforms:
      - Raspberry Pi
    locator: Working with Raspberry Pi and Windows 10, Developing for the Raspberry Pi Using Visual Studio
    evidence_note: Microsoft's IoT Core guide directs developers to install Visual Studio's Universal
      Windows App tools and create a UWP project; it is a development-host association, not a claim that
      Visual Studio is installed on the device.
  unresolved:
  - field: countries_of_origin
    disposition: no-evidence-found
    reason: The consulted Microsoft material establishes the vendor and products but not the original
      Windows IoT development location. Microsoft headquarters or documentation location would not prove
      country of origin.
    source_ids:
    - ms-windows-iot-docs
    - ms-iot-announcement-2015
  - field: programming_languages
    disposition: no-evidence-found
    reason: The public documentation names UWP and Visual Studio development tooling but does not establish
      implementation languages for the family or its different editions; those languages are not inferred
      from API/toolchain support.
    source_ids:
    - ms-iot-core-rpi
    - ms-iot-enterprise-overview
  - field: system_organization
    disposition: unknown
    reason: Windows IoT is a family label covering distinct editions. Microsoft states that IoT Enterprise
      is binary equivalent to Windows Enterprise but the consulted sources do not give a normalized whole-family
      system-organization classification.
    source_ids:
    - ms-windows-iot-docs
    - ms-iot-enterprise-overview
  - field: kernels
    disposition: unknown
    reason: No consulted Microsoft source identifies a kernel architecture for every Windows IoT edition,
      and a Windows-family inference would erase the edition boundary documented by Microsoft.
    source_ids:
    - ms-windows-iot-docs
    - ms-iot-enterprise-overview
# END GENERATED DEEP RESEARCH
---

# Windows IoT

Draft inventory record; core factual research is pending.
