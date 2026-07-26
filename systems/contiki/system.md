---
type: Operating System
title: Contiki
description: Open-source operating system lineage for networked, resource-constrained and IoT devices.
tags: [operating-system, embedded, internet-of-things]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified. Contiki-NG is a separately maintained successor project and is not merged here." }
field_dispositions:
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: no-evidence-found, checked_at: 2026-07-26, evidence: [contiki-repository] }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amstrad], label: Contiki, position: 12, target: https://en.wikipedia.org/wiki/Contiki, depth: 1 }
    - { section: [Proprietary, Apple], label: Contiki, position: 22, target: https://en.wikipedia.org/wiki/Contiki, depth: 2, parent_position: 16 }
    - { section: [Proprietary, Atari], label: "Contiki (for 8-bit, ST, Portfolio)", position: 59, target: https://en.wikipedia.org/wiki/Contiki, depth: 1 }
    - { section: ["Generic, commodity, and other"], label: "Contiki for various, mostly 8-bit systems", position: 712, target: https://en.wikipedia.org/wiki/Contiki, depth: 1 }
    - { section: [Embedded, "Other embedded"], label: Contiki, position: 858, target: https://en.wikipedia.org/wiki/Contiki, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: Contiki, kind: official, language: en, script: Latn, evidence: [contiki-repository], assertion_status: documented }
organizations:
  - { organization: "https://www.sics.se/", roles: [creator], note: "Repository source header attributes Contiki to Adam Dunkels at SICS.", evidence: [contiki-source], assertion_status: documented }
development_contexts:
  - { value: academic-research, primary: true, evidence: [contiki-source], assertion_status: documented }
design_purposes:
  - { value: network-services, primary: true, source_term: "Internet of Things", evidence: [contiki-repository], assertion_status: documented }
  - { value: embedded-control, primary: false, evidence: [contiki-repository], assertion_status: documented }
development_status: { value: inactive, note: "The official historical repository directs current development to Contiki-NG.", evidence: [contiki-repository], assertion_status: documented }
support_status: { value: community, evidence: [contiki-repository], assertion_status: provisional }
distribution_status: { value: public, evidence: [contiki-repository], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [contiki-source], assertion_status: documented }
software_freedom_status: { value: free-open-source, evidence: [contiki-source], assertion_status: documented }
licenses:
  - { value: "BSD 3-Clause", spdx: BSD-3-Clause, scope: source, evidence: [contiki-source], assertion_status: documented }
source_preservation: { survival: complete, access: public, authorization: authorized, evidence: [contiki-repository] }
programming_languages:
  - { value: C, kind: high-level, extent: primary, evidence: [contiki-repository], assertion_status: documented }
interfaces:
  - { name: "application programming interfaces", style: programming, modalities: [programmatic], provisioning: source, access: local-build, evidence: [contiki-repository], assertion_status: documented }
platforms:
  - { value: "networked Internet of Things devices", evidence: [contiki-repository], assertion_status: documented }
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: contiki-repository, resource: "https://github.com/contiki-os/contiki", title: "contiki-os/contiki", author: organization:contiki-os, source_kind: source-tree }
  - { id: contiki-source, resource: "https://docs.contiki-ng.org/en/master/_api/contiki_8h_source.html", title: "Contiki header source", author: person:Adam-Dunkels, source_kind: source-tree }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Contiki
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Adam Dunkels
    country_of_origin: null
    purpose: null
    programming_languages: null
    first_release: 10 March 2003 ; 23 years ago ( 2003-03-10 )
    latest_release: null
    last_updated: null
    development_status: null
    source_model: Open source
    os_family: null
    gui: null
    platforms: null
    kernel_type: null
    license: BSD-3-Clause
# END GENERATED ENWIKI INFOBOX
---

# Contiki

## Overview

Contiki is an open-source operating-system lineage for the Internet of Things;
the project repository identifies the historic Contiki tree and links to its
successor, Contiki-NG.[^contiki-repository]

[^contiki-repository]: [contiki-os/contiki](https://github.com/contiki-os/contiki)
