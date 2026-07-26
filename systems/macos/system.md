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
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
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
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: Aquamacs
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q2859156
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Barry's Emacs
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q2885703
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: BBEdit
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q795617
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Bluefish
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q651027
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Codelobster
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q4036361
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: CotEditor
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q97186868
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: dte
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q88926112
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Eddie
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q5335795
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Edit
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q134540318
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Epsilon
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q5383949
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: GNU Emacs
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q1252773
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: GNU moe
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q3093311
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: GNU nano
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q306101
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: GNU Zile
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q3093309
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: iA Writer
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q5968467
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Kate
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q261933
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Kibi
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q104451372
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Kod
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q6425029
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Leo
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q6523506
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: MarkEdit
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q135840899
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: micro
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q62514269
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Notepadqq
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q50559933
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: novelWriter
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q104904049
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: StoryMill
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q7620368
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Sublime Text
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q267193
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: TeXShop
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q1417891
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Textadept
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q18388827
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: TextEdit
  relationship: bundled-default
  interface_style: graphical
  source: https://support.apple.com/guide/textedit/welcome/mac
  source_kind: vendor-documentation
  assertion_status: documented
- name: TextMate
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q2297533
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: The Hessling Editor
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q3521247
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Typora
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q48938027
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: UltraEdit
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q1305902
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Ulysses
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q3548159
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Xi
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q24817375
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Zed
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q112301707
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
# END GENERATED TEXT EDITORS
---

## Overview

Apple identifies macOS as the Mac operating system and documents its named
versions and installation compatibility.[^apple-support]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/MacOS).
[^apple-support]: [Apple macOS support](https://support.apple.com/en-us/109033).
