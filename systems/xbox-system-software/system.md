---
type: Operating System
title: Xbox system software
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
names: [{ value: "Xbox system software", kind: official, language: en, script: Latn, evidence: [wikipedia-list], assertion_status: provisional }]
sources: [{ id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }]
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Xbox_system_software
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Microsoft
    country_of_origin: United States
    purpose: null
    programming_languages: C , C++
    first_release: null
    latest_release: null
    last_updated: null
    development_status: Discontinued
    source_model: Closed source
    os_family: null
    gui: null
    platforms: Xbox
    kernel_type: null
    license: null
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
  source: https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/sdk-and-tools?view=gdk-2510
  source_kind: official-sdk-documentation
  assertion_status: documented
  scope:
    editions:
    - GDK-era Xbox development
  note: Microsoft requires/recommends Visual Studio with the GDK for games targeting
    Xbox consoles; this is an editor/IDE relationship on the development host, not
    a retail-console bundle claim.
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-002
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Xbox system software is a Microsoft console-software family spanning separate console
    generations and system versions, not one stable kernel release. Microsoft documents a current, separately
    versioned Game OS for Xbox titles, continuing console updates for Xbox One and Series X|S, and the
    GDK/Visual Studio development path. Historic kernel and implementation-language claims remain intentionally
    unresolved because Microsoft’s public generation-spanning sources do not establish them.
  sources:
  - id: ms-xbox-announcement-2000
    title: Microsoft Unveils Plans for Xbox
    url: https://news.microsoft.com/source/2000/03/10/microsoft-unveils-plans-for-xbox/
    archived_url: null
    source_kind: official-announcement
    language: en
    date: '2000-03-10'
    primary: true
    notes: Microsoft's first public Xbox announcement describes a dedicated video-game console and developer
      platform.
  - id: ms-xbox-launch-2001
    title: Microsoft Announces Launch Details for Xbox in North America
    url: https://news.microsoft.com/source/2001/05/16/microsoft-announces-launch-details-for-xbox-in-north-america/
    archived_url: null
    source_kind: official-release-announcement
    language: en
    date: '2001-05-16'
    primary: true
    notes: Microsoft announced North American retail availability beginning November 8, 2001.
  - id: ms-xbox-gdk-game-os
    title: What is the Microsoft Game Development Kit?
    url: https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/intro/introduction?view=gdk-2510
    archived_url: null
    source_kind: official-sdk-documentation
    language: en
    date: '2025-12-10'
    primary: true
    notes: Microsoft documents Game OS, its separate game-versioning model, GDK APIs, and Visual Studio
      support.
  - id: ms-xbox-update-2026-04
    title: 'April Xbox Update: Customize Your Console, Manually Add Your Favorite Games on PC, and More'
    url: https://news.xbox.com/en-us/2026/04/30/april-xbox-update-2026/
    archived_url: null
    source_kind: official-update-note
    language: en
    date: '2026-04-30'
    primary: true
    notes: Microsoft's Xbox Wire note documents April 2026 console features and current Series X|S/Xbox
      One update delivery.
  - id: ms-xbox-gdk-tools
    title: SDK and tools requirements - Microsoft Game Development Kit
    url: https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/sdk-and-tools?view=gdk-2510
    archived_url: null
    source_kind: official-sdk-documentation
    language: en
    date: '2026'
    primary: true
    notes: Microsoft's current GDK document specifies Visual Studio and SDK tooling for games targeting
      Xbox consoles.
  - id: ms-xbox-series-manual-license
    title: Xbox Series X|S Product and Regulatory Guide
    url: https://download.microsoft.com/download/c/5/1/c516c773-0650-4719-8b1e-fbee939075f5/XBOX%20SERIES%20X%20%20%20S%20MANUAL%20EN%20-%20AU%20NZ.pdf
    archived_url: null
    source_kind: official-product-manual
    language: en
    date: 2025-03
    primary: true
    notes: Microsoft product guide directs users to the Xbox Software License Agreement.
  claims:
  - field: organizations
    value:
      organization: Microsoft
      role: developer
    source_ids:
    - ms-xbox-announcement-2000
    - ms-xbox-gdk-game-os
    assertion_status: documented
    source_term: Microsoft; Microsoft Game Development Kit
    scope: {}
    locator: 2000 announcement; GDK overview
    evidence_note: Microsoft announced that it was developing the Xbox platform and publishes the GDK
      and Game OS documentation for current Xbox console development.
  - field: design_purposes
    value:
      purpose: gaming
      primary: true
      source_term: dedicated video game console; Game OS optimized for games
    source_ids:
    - ms-xbox-announcement-2000
    - ms-xbox-gdk-game-os
    assertion_status: documented
    source_term: dedicated video game console
    scope: {}
    locator: 2000 announcement, opening paragraphs; GDK overview, On Xbox
    evidence_note: Microsoft announced Xbox as a dedicated console for games and describes the current
      Game OS as optimized for running games with defined resource guarantees.
  - field: development_status
    value:
      state: active
      as_of: '2026-07-27'
      editions:
      - Xbox One
      - Xbox Series X|S
    source_ids:
    - ms-xbox-update-2026-04
    assertion_status: documented
    source_term: Console Updates
    scope:
      platforms:
      - Xbox One
      - Xbox Series X|S
    locator: April 2026 update, Console Updates and Help Shape the Future of Xbox
    evidence_note: Microsoft released console software features in April 2026 and explicitly addresses
      Xbox Series X|S and Xbox One update participation.
  - field: lifecycle_events
    value:
      event: announced
      date: '2000-03-10'
      subject: Xbox
    source_ids:
    - ms-xbox-announcement-2000
    assertion_status: documented
    source_term: Microsoft Unveils Plans for Xbox
    scope:
      platforms:
      - original Xbox
    locator: Dateline and opening paragraph
    evidence_note: Microsoft publicly unveiled the future dedicated Xbox console on March 10, 2000.
  - field: lifecycle_events
    value:
      event: commercial-availability
      date: '2001-11-08'
      subject: Xbox North American launch
    source_ids:
    - ms-xbox-launch-2001
    assertion_status: documented
    source_term: Starting Nov. 8, 2001
    scope:
      platforms:
      - original Xbox
      countries:
      - US
      - CA
    locator: Opening announcement paragraphs
    evidence_note: Microsoft announced that Xbox consoles would become available through North American
      retailers beginning November 8, 2001.
  - field: rights_regime
    value:
      regime: copyrighted
      scope: binary
      edition: Xbox Series X|S
    source_ids:
    - ms-xbox-series-manual-license
    assertion_status: documented
    source_term: Software License Agreement
    scope:
      platforms:
      - Xbox Series X|S
    locator: Product and Regulatory Guide, Software License Agreement reference
    evidence_note: Microsoft's Series X|S guide directs users to a software license agreement, establishing
      licensed proprietary treatment for that console software scope.
  - field: licenses
    value:
      name: Xbox Software License Agreement
      scope: binary
      licensor: Microsoft
    source_ids:
    - ms-xbox-series-manual-license
    assertion_status: documented
    source_term: Software License Agreement at xbox.com/slt
    scope:
      platforms:
      - Xbox Series X|S
    locator: Product and Regulatory Guide, Software License Agreement
    evidence_note: The Microsoft product guide names the Xbox Software License Agreement and provides
      its official location; this is scoped to the Series X|S product guide.
  - field: system_organization
    value:
      organization: other
      source_term: separate Game OS
    source_ids:
    - ms-xbox-gdk-game-os
    assertion_status: documented
    source_term: separate Game OS optimized for games
    scope:
      editions:
      - GDK-era Xbox Game OS
    locator: GDK overview, Testing games that use the Game OS and Gaming Runtime on Xbox
    evidence_note: Microsoft calls the relevant layer a separate Game OS and describes its game-specific
      versioning and resource model; the source does not assign a generic monolithic/microkernel label.
  - field: interfaces
    value:
      name: Xbox Home
      style: graphical
      provisioning: bundled-default
      access: local-console
    source_ids:
    - ms-xbox-update-2026-04
    assertion_status: documented
    source_term: Home; My games & apps
    scope:
      platforms:
      - Xbox One
      - Xbox Series X|S
    locator: April 2026 update, Console Updates
    evidence_note: Microsoft's current console-update note documents Home groups, color customization,
      My games & apps, and game cards as the first-party console interface.
  - field: platforms
    value:
      platform:
      - Xbox One
      - Xbox Series X
      - Xbox Series S
      support_origin: original-target
      execution_mode: native
    source_ids:
    - ms-xbox-update-2026-04
    - ms-xbox-gdk-game-os
    assertion_status: documented
    source_term: Xbox Series X|S; Xbox One; Xbox consoles
    scope:
      editions:
      - current console software
      - GDK-era Game OS
    locator: April 2026 update; GDK overview, On Xbox
    evidence_note: Microsoft's update note identifies the current Xbox One and Series X|S console platforms,
      while the GDK documentation establishes the Game OS scope on Xbox consoles.
  editor_associations:
  - name: Visual Studio
    relationship: development-host-tool
    interface_style: graphical
    source_ids:
    - ms-xbox-gdk-tools
    - ms-xbox-gdk-game-os
    assertion_status: documented
    scope:
      editions:
      - GDK-era Xbox development
    locator: SDK and tools requirements, Visual Studio; GDK overview, Support for Visual Studio
    evidence_note: Microsoft requires/recommends Visual Studio with the GDK for games targeting Xbox consoles;
      this is an editor/IDE relationship on the development host, not a retail-console bundle claim.
  unresolved:
  - field: countries_of_origin
    disposition: no-evidence-found
    reason: Microsoft's announcements establish company ownership and launch locations but do not document
      the physical location of original Xbox system-software development. A launch venue cannot establish
      a development origin.
    source_ids:
    - ms-xbox-announcement-2000
    - ms-xbox-launch-2001
  - field: programming_languages
    disposition: no-evidence-found
    reason: The GDK documents C and C++ API styles for game developers, not the implementation language(s)
      of Xbox system software across its generations; no implementation language is inferred from exposed
      APIs.
    source_ids:
    - ms-xbox-gdk-game-os
    - ms-xbox-gdk-tools
  - field: kernels
    disposition: unknown
    reason: The family title spans original Xbox, Xbox 360, Xbox One, and Series-era products. The consulted
      Microsoft GDK source documents a separate Game OS but provides no kernel architecture that can be
      applied across those generations.
    source_ids:
    - ms-xbox-gdk-game-os
    - ms-xbox-announcement-2000
# END GENERATED DEEP RESEARCH
---

# Xbox system software

Draft inventory record; core factual research is pending.
