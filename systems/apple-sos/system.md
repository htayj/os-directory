---
type: Operating System
title: Apple SOS
description: Sophisticated Operating System (SOS), the Apple III operating system.
tags: [operating-system, apple-iii]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, Apple], label: "Apple SOS", position: 24, target: "https://en.wikipedia.org/wiki/Apple_SOS", depth: 2, parent_position: 23 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "SOS", kind: official, language: en, script: Latn, evidence: [sos-source], assertion_status: documented }]
organizations: [{ organization: Apple, roles: [developer, publisher], evidence: [sos-source], assertion_status: documented }]
design_purposes: [{ value: business-data-processing, primary: true, source_term: "Apple III computer's operating system", evidence: [sos-source], assertion_status: documented }]
development_status: { value: discontinued, evidence: [sos-source], assertion_status: provisional }
programming_languages: [{ value: "6502 assembly language", kind: assembly, extent: primary, evidence: [sos-source], assertion_status: documented }]
system_organization: [{ value: unknown, evidence: [sos-source], assertion_status: unknown }]
kernels: []
interfaces: [{ name: "SOS system interface", style: full-screen-text, modalities: [keyboard], provisioning: bundled, access: local-console, evidence: [sos-source], assertion_status: provisional }]
platforms: [{ value: "Apple III", evidence: [sos-source], assertion_status: documented }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: sos-source, resource: "https://apple3.org/Documents/SourceCode/apple3_SRC_SOS_DTC.pdf", title: "Apple III SOS source-code disk readme", source_kind: source-tree }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Apple_SOS
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Apple Computer
    country_of_origin: United States
    purpose: null
    programming_languages: null
    first_release: January 1980 ; 46 years ago ( 1980-01 )
    latest_release: 1.3 / January 1, 1980 ; 46 years ago ( 1980-01-01 )
    last_updated: 1.3 / January 1, 1980 ; 46 years ago ( 1980-01-01 )
    development_status: Discontinued
    source_model: Closed source
    os_family: SOS
    gui: Full screen text mode
    platforms: Apple III
    kernel_type: Monolithic kernel
    license: Apple Software License Agreement
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q312
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
---

# Apple SOS

SOS is the Apple III operating system; a preserved source-code disk identifies version 1.3 as its last released version.[^sos-source]

[^sos-source]: [Apple III SOS source-code disk readme](https://apple3.org/Documents/SourceCode/apple3_SRC_SOS_DTC.pdf)
