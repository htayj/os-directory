---
type: Operating System
title: macOS
description: Apple's operating system for Mac computers, formerly Mac OS X and OS X.
tags: [operating-system, apple, mac]
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
    - { section: [Proprietary, Apple], label: macOS (formerly Mac OS X and OS X), position: 33, target: https://en.wikipedia.org/wiki/MacOS, depth: 2, parent_position: 26 }
discovery_provenance:
  - { method: english-list, language: en, native_label: macOS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: macOS, kind: official, language: en, script: Latn, evidence: [apple-support], assertion_status: documented }
  - { value: Mac OS X, kind: former, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }
  - { value: OS X, kind: former, language: en, script: Latn, evidence: [wikipedia], assertion_status: provisional }
organizations: [{ organization: Apple Inc., roles: [developer, vendor], evidence: [apple-support], assertion_status: documented }]
countries_of_origin: []
design_purposes: [{ value: personal-computing, primary: true, evidence: [apple-support], assertion_status: documented }]
development_status: { value: active, evidence: [apple-support], assertion_status: documented }
distribution_status: { value: active, evidence: [apple-support], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: mixed, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
gui_status: { value: integrated, evidence: [apple-support], assertion_status: documented }
interfaces: [{ name: macOS graphical interface, style: graphical, evidence: [apple-support], assertion_status: documented }]
hardware_platforms: [{ platform: Apple Mac computers, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [apple-support], assertion_status: documented }]
architectures: []
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/MacOS, title: MacOS, source_kind: article }
  - { id: apple-support, resource: https://support.apple.com/en-us/109033, title: Find out which macOS your Mac is using, author: organization:apple, source_kind: documentation }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/MacOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple
    country_of_origin: United States
    purpose: null
    programming_languages: C C++ Objective-C Swift assembly language
    first_release: March 24, 2001 ; 25 years ago ( 2001-03-24 )
    latest_release: 26.5.2 (June 29, 2026 ; 27 days ago ( 2026-06-29 ) ) [ ± ]
    last_updated: 26.5.2 (June 29, 2026 ; 27 days ago ( 2026-06-29 ) ) [ ± ]
    development_status: null
    source_model: Proprietary with open source components
    os_family: Mac Darwin BSD Unix-like Unix
    gui: Aqua ( graphical )
    platforms: 'Apple silicon ( ARM64 ) ARMv9-A ( 15.0 –present) ARMv8-A ( 11.0 –present)
      Intel (64-bit) x86-64 ( 10.4.7 – 26.x ) Previously supported: Intel (32-bit)
      IA-32 ( 10.4.4 – 10.6.8 ) PowerPC 64-bit ppc970 ( 10.4 – 10.5.8 ) 32-bit ppc7400
      ( 10.0 – 10.5.8 ) 32-bit ppc ( 10.0 – 10.4.11 )'
    kernel_type: Hybrid ( XNU )
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q312
# END GENERATED ENWIKI INFOBOX
---

## Overview

Apple identifies macOS as the Mac operating system and documents its named
versions and installation compatibility.[^apple-support]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/MacOS).
[^apple-support]: [Apple macOS support](https://support.apple.com/en-us/109033).
