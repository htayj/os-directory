---
type: Operating System
title: Unix
description: Bell Laboratories operating-system lineage and progenitor of the Unix family.
tags: [operating-system, unix, bell-labs]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass lineage record; no claim is marked verified." }
field_dispositions:
  - { field: rights_regime, disposition: disputed, checked_at: 2026-07-26 }
  - { field: licenses, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26, reason: "The reviewed early system is command-oriented." }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, "Bell Labs"], label: Unix, position: 65, target: "https://en.wikipedia.org/wiki/Unix", depth: 1 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: Unix, kind: official, language: en, script: Latn, evidence: [unix-paper], assertion_status: documented }]
organizations: [{ organization: "Bell Laboratories", roles: [creator, developer], evidence: [unix-paper], assertion_status: documented }]
countries_of_origin: [US]
development_origins: [{ country: US, place: "Murray Hill, New Jersey", organization: "Bell Laboratories", role: origin, evidence: [unix-paper], assertion_status: documented }]
development_contexts: [{ value: academic-research, primary: true, evidence: [unix-paper], assertion_status: provisional }]
design_purposes: [{ value: time-sharing, primary: true, source_term: "general-purpose, multi-user, interactive operating system", evidence: [unix-paper], assertion_status: documented }]
development_status: { value: superseded, evidence: [unix-paper], assertion_status: provisional }
programming_languages: [{ value: C, kind: high-level, extent: substantial, evidence: [unix-paper], assertion_status: documented }]
system_organization: [{ value: distinct-kernel, evidence: [unix-paper], assertion_status: provisional }]
kernels: [{ name: Unix, architecture: unknown, evidence: [unix-paper], assertion_status: provisional }]
interfaces: [{ name: "Unix command language", style: command-line, modalities: [keyboard], provisioning: bundled, access: terminal, evidence: [unix-paper], assertion_status: documented }]
platforms: [{ value: "PDP-11/40 and PDP-11/45", evidence: [unix-paper], assertion_status: documented }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: unix-paper, resource: "https://web.eecs.umich.edu/~prabal/teaching/eecs582-w13/readings/ritchie74unix.pdf", title: "The UNIX Time-Sharing System", author: "Dennis M. Ritchie and Ken Thompson", source_kind: paper }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/Unix
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Ken Thompson , Dennis Ritchie , Brian Kernighan , Douglas McIlroy ,
      and Joe Ossanna at Bell Labs
    country_of_origin: United States
    purpose: null
    programming_languages: C and assembly language
    first_release: Development started in 1969 First manual published internally in
      November 1971 ( 1971-11 ) Announced outside Bell Labs in October 1973 ( 1973-10
      )
    latest_release: null
    last_updated: null
    development_status: null
    source_model: Historically proprietary software , while some Unix projects (including
      BSD family and Illumos ) are open-source and historical Unix source code is
      archived.
    os_family: Unix
    gui: Command-line interface and Graphical ( Wayland and X Window System ; Android
      SurfaceFlinger ; macOS Quartz )
    platforms: null
    kernel_type: Varies; monolithic , microkernel , hybrid
    license: Varies; some versions are proprietary , others are free/libre or open-source
      software
  country_evidence:
    assertion_status: inferred
    method: inferred-from-developer-country
    source: https://www.wikidata.org/wiki/Q217365
# END GENERATED ENWIKI INFOBOX
---

# Unix

The 1974 Bell Laboratories paper describes Unix as a general-purpose,
multi-user interactive system for PDP-11 computers.[^unix-paper]

[^unix-paper]: [The UNIX Time-Sharing System](https://web.eecs.umich.edu/~prabal/teaching/eecs582-w13/readings/ritchie74unix.pdf)
