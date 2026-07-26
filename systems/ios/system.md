---
type: Operating System
title: iOS
description: Apple's mobile operating system for iPhone, formerly iPhone OS.
tags: [operating-system, apple, ios, mobile]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: architectures, disposition: not-researched, checked_at: 2026-07-26 }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Apple], label: iOS (formerly iPhone OS), position: 40, target: https://en.wikipedia.org/wiki/IOS, depth: 2, parent_position: 39 }
    - { section: [Embedded, Mobile operating systems], label: iOS, position: 816, target: https://en.wikipedia.org/wiki/IOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: iOS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: iOS, kind: official, language: en, script: Latn, evidence: [apple], assertion_status: documented }
  - { value: iPhone OS, kind: former, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }
organizations: [{ organization: Apple Inc., roles: [developer, vendor], evidence: [apple], assertion_status: documented }]
countries_of_origin: []
design_purposes: [{ value: mobile-computing, primary: true, evidence: [apple], assertion_status: documented }]
development_status: { value: active, evidence: [apple], assertion_status: documented }
support_status: { value: active, evidence: [apple], assertion_status: documented }
distribution_status: { value: bundled, evidence: [apple], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: mixed, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
gui_status: { value: integrated, evidence: [apple], assertion_status: documented }
interfaces: [{ name: iOS touch interface, style: graphical, modalities: [touch], evidence: [apple], assertion_status: documented }]
hardware_platforms: [{ platform: iPhone, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [apple], assertion_status: documented }]
architectures: []
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/IOS, title: IOS, source_kind: article }
  - { id: apple, resource: https://developer.apple.com/ios, title: iOS, author: organization:apple, source_kind: documentation }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/IOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple
    country_of_origin: United States
    purpose: iPhone iPad (until 13.0 ) iPod Touch (until 16.0 )
    programming_languages: C , C++ , Objective-C , Swift , assembly language
    first_release: June 29, 2007 ; 19 years ago ( 2007-06-29 )
    latest_release: 26.5.2 (June 29, 2026 ; 27 days ago ( 2026-06-29 ) ) [ ± ]
    last_updated: 26.5.2 (June 29, 2026 ; 27 days ago ( 2026-06-29 ) ) [ ± ]
    development_status: Current
    source_model: Closed , with open-source components
    os_family: Unix-like , based on Darwin ( BSD ), macOS
    gui: Multi-touch GUI
    platforms: ARM architecture family ARM64 (since 7.0 ) ARM32 (until 11.0 )
    kernel_type: Hybrid ( XNU )
    license: Proprietary software except for open-source components
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q312
# END GENERATED ENWIKI INFOBOX
---

## Overview

Apple calls iOS its mobile operating system and documents its development
platform for iPhone applications.[^apple]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/IOS).
[^apple]: [Apple Developer iOS](https://developer.apple.com/ios).
