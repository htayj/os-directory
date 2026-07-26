---
type: Operating System
title: watchOS
description: Apple operating system for Apple Watch.
tags: [operating-system, apple, wearable]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, Apple], label: watchOS, position: 44, target: "https://en.wikipedia.org/wiki/WatchOS", depth: 4, parent_position: 43 }, { section: [Embedded, "Mobile operating systems"], label: watchOS, position: 817, target: "https://en.wikipedia.org/wiki/WatchOS", depth: 2, parent_position: 816 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: watchOS, kind: official, language: en, script: Latn, evidence: [apple-watchos], assertion_status: documented }]
organizations: [{ organization: Apple, roles: [developer, publisher], evidence: [apple-watchos], assertion_status: documented }]
countries_of_origin: [US]
design_purposes: [{ value: mobile-handheld, primary: true, evidence: [apple-watchos], assertion_status: documented }]
development_status: { value: active, evidence: [apple-watchos], assertion_status: documented }
distribution_status: { value: public, evidence: [apple-watchos], assertion_status: documented }
gui_status: [{ value: first-party, evidence: [apple-watchos], assertion_status: provisional }]
interfaces: [{ name: "watchOS interface", style: graphical, modalities: [touch, rotary-control], provisioning: bundled, access: local-session, evidence: [apple-watchos], assertion_status: provisional }]
platforms: [{ value: "Apple Watch", evidence: [apple-watchos], assertion_status: documented }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: apple-watchos, resource: "https://developer.apple.com/watchos/", title: "watchOS", author: organization:Apple, source_kind: project-site }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/WatchOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple
    country_of_origin: United States
    purpose: Smartwatch
    programming_languages: C C++ Objective-C Swift assembly language
    first_release: April 24, 2015 ; 11 years ago ( 2015-04-24 )
    latest_release: 26.5 (May 11, 2026 ; 2 months ago ( 2026-05-11 ) ) [ ± ]
    last_updated: 26.5 (May 11, 2026 ; 2 months ago ( 2026-05-11 ) ) [ ± ]
    development_status: Current
    source_model: Closed , with open-source components
    os_family: Unix-like , iOS based on Darwin
    gui: Cocoa Touch ( GUI )
    platforms: ARMv8-A (5.0–present) ARMv7-A (1.0–8.8.2)
    kernel_type: Hybrid ( XNU )
    license: Proprietary software except for open-source components
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q312
# END GENERATED ENWIKI INFOBOX
---

# watchOS

Apple's watchOS developer page identifies watchOS as the Apple Watch platform.[^apple-watchos]

[^apple-watchos]: [watchOS](https://developer.apple.com/watchos/)
