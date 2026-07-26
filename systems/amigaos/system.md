---
type: Operating System
title: AmigaOS
description: Operating-system lineage for Commodore Amiga computers, with later maintained branches.
tags: [operating-system, amiga, commodore]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, reason: Current rights arrangements are time-scoped and not fully researched. }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amiga Inc.], label: AmigaOS, position: 7, target: https://en.wikipedia.org/wiki/AmigaOS, depth: 1 }
    - { section: [Proprietary, Commodore International], label: AmigaOS, position: 90, target: https://en.wikipedia.org/wiki/AmigaOS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: AmigaOS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: AmigaOS, kind: official, language: en, script: Latn, evidence: [hyperion], assertion_status: documented }
organizations:
  - { organization: Commodore International, roles: [creator, developer, vendor], evidence: [hyperion], assertion_status: documented }
  - { organization: Hyperion Entertainment, roles: [developer, maintainer], scope: { releases: [AmigaOS 4.x] }, evidence: [hyperion], assertion_status: documented }
countries_of_origin: [US]
development_origins:
  - { country: US, organization: Commodore International, role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: personal-computing, primary: true, evidence: [hyperion], assertion_status: documented }
development_status: { value: active, evidence: [hyperion], assertion_status: documented }
distribution_status: { value: commercial, evidence: [hyperion], assertion_status: documented }
lifecycle_events:
  - { kind: first-public-release, value: "1985", precision: year, qualifier: exact, evidence: [wikipedia], assertion_status: provisional }
rights_regime: { value: copyrighted, evidence: [hyperion-settlement], assertion_status: documented }
software_freedom_status: { value: proprietary, evidence: [hyperion-settlement], assertion_status: documented }
programming_languages: []
system_organization: []
kernels: []
gui_status: { value: integrated, evidence: [wikipedia], assertion_status: provisional }
interfaces:
  - { name: Workbench, style: graphical, evidence: [wikipedia], assertion_status: provisional }
hardware_platforms:
  - { platform: Commodore Amiga computers, support_origin: original-target, support_status: historical, execution_mode: native, evidence: [hyperion], assertion_status: documented }
architectures:
  - { value: Motorola 68000 family, execution_mode: native, evidence: [wikipedia], assertion_status: provisional }
  - { value: PowerPC, execution_mode: native, scope: { releases: [AmigaOS 4.x] }, evidence: [hyperion], assertion_status: documented }
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/AmigaOS, title: AmigaOS, source_kind: article }
  - { id: hyperion, resource: https://shop.amigaos.net/index.php/corporate, title: About Hyperion Entertainment, author: organization:hyperion-entertainment, source_kind: project-site }
  - { id: hyperion-settlement, resource: https://www.hyperion-entertainment.com/index.php/news/38-corporate/134-hyperion-entertainment-cvba-and-amiga-inc-reach-settlement, title: Hyperion Entertainment CVBA and Amiga Inc. reach settlement, author: organization:hyperion-entertainment, source_kind: announcement }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/AmigaOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Commodore International (v1.0–3.1) Haage & Partner (v3.5–3.9) Hyperion
      Entertainment (v3.1.4–3.2, v4.0–4.1)
    country_of_origin: United States; Germany; Belgium; United Kingdom of the Netherlands;
      France; Austrian Netherlands; Spanish Netherlands; Habsburg Netherlands; Burgundian
      Netherlands; Duchy of Brabant
    purpose: null
    programming_languages: Assembly , C , BCPL (v1)
    first_release: July 23, 1985 ; 40 years ago ( 1985-07-23 )
    latest_release: 4.1 Final Edition Update 3 / October 18, 2025 ; 9 months ago (
      2025-10-18 )
    last_updated: 4.1 Final Edition Update 3 / October 18, 2025 ; 9 months ago ( 2025-10-18
      )
    development_status: Current
    source_model: Closed source
    os_family: Amiga
    gui: Graphical ( Workbench )
    platforms: m68k (v1–v3), PowerPC (v4)
    kernel_type: Microkernel
    license: Proprietary
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-headquarters
    source: https://www.wikidata.org/wiki/Q9005
# END GENERATED ENWIKI INFOBOX
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: has-associations
  note: One or more discovery relationships were found; provisional relationships
    still require primary-source confirmation.
text_editors:
- name: CygnusEd
  relationship: supported-platform
  interface_style: null
  source: https://www.wikidata.org/wiki/Q5199203
  source_kind: wikidata-P306-operating-system
  assertion_status: provisional
- name: Ed
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://wiki.amigaos.net/wiki/AmigaOS_Manual:_AmigaDOS_Command_Reference#Ed
  source_kind: official-system-manual
  assertion_status: documented
- name: MEmacs
  relationship: bundled-default
  interface_style: full-screen-text
  source: https://wiki.amigaos.net/wiki/AmigaOS_Manual:_AmigaDOS_Command_Reference#MEmacs
  source_kind: official-system-manual
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

## Overview

AmigaOS is retained as one operating-system lineage. Its two batch version
candidates are release concepts below; this avoids treating version ranges as
separate system identities. Hyperion describes AmigaOS 4.x as a modern rewrite
of the operating system originally developed by Commodore.[^hyperion]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/AmigaOS).
[^hyperion]: [Hyperion corporate history](https://shop.amigaos.net/index.php/corporate).
[^hyperion-settlement]: [Hyperion settlement announcement](https://www.hyperion-entertainment.com/index.php/news/38-corporate/134-hyperion-entertainment-cvba-and-amiga-inc-reach-settlement).
