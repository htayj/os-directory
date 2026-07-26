---
type: Operating System
title: GNO/ME
description: Unix-like multitasking operating-system environment for the Apple IIGS.
tags: [operating-system, unix-like, apple-iigs]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "First-pass record; no claim is marked verified." }
field_dispositions:
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: development_origins, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: gui_status, disposition: not-applicable, checked_at: 2026-07-26 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [{ section: [Proprietary, Apple], label: "GNO/ME", position: 21, target: "https://en.wikipedia.org/wiki/GNO/ME", depth: 2, parent_position: 16 }] }
discovery_provenance: [{ method: english-list, language: en, source: wikipedia-list, observed_at: 2026-07-26, disposition: included-system }]
names: [{ value: "GNO/ME", kind: official, language: en, script: Latn, evidence: [gno-site], assertion_status: documented }]
organizations: [{ organization: "Procyon Enterprises", roles: [developer], evidence: [gno-site], assertion_status: provisional }]
design_purposes: [{ value: time-sharing, primary: true, source_term: "UNIX-like environment", evidence: [gno-site], assertion_status: documented }]
development_status: { value: maintenance, evidence: [gno-site], assertion_status: provisional }
distribution_status: { value: public, evidence: [gno-site], assertion_status: documented }
system_organization: [{ value: distinct-kernel, source_term: "GNO kernel", evidence: [gno-kernel], assertion_status: documented }]
kernels: [{ name: "GNO kernel", architecture: unknown, note: "Provides communication between programs and GS/OS.", evidence: [gno-kernel], assertion_status: documented }]
interfaces: [{ name: "GNO shell", style: command-line, modalities: [keyboard], provisioning: bundled, access: local-console, evidence: [gno-kernel], assertion_status: provisional }]
platforms: [{ value: "Apple IIGS", evidence: [gno-site], assertion_status: documented }]
sources:
  - { id: wikipedia-list, resource: "https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001", title: "List of operating systems", source_kind: list }
  - { id: gno-site, resource: "https://www.gno.org/gno/", title: "GNO/ME home", author: organization:GNO, source_kind: project-site }
  - { id: gno-kernel, resource: "https://mirrors.apple2.org.za/ftp.gno.org/gs.specific/gno/doc/refs/aug96/kernel.html", title: "GNO Kernel Reference Manual", source_kind: manual }
# BEGIN GENERATED ENWIKI INFOBOX
first_pass_attributes:
  source: https://en.wikipedia.org/wiki/GNO/ME
  retrieved_at: '2026-07-26'
  assertion_status: provisional
  note: Raw discovery metadata from the linked English Wikipedia infobox; normalize
    and verify against stronger sources before marking verified.
  fields:
    developer: Procyon Enterprises, Devin Reade
    country_of_origin: null
    purpose: Personal computing
    programming_languages: null
    first_release: 1991 ; 35 years ago ( 1991 )
    latest_release: 2.0.6 / February 15, 1999 ; 27 years ago ( 1999-02-15 )
    last_updated: 2.0.6 / February 15, 1999 ; 27 years ago ( 1999-02-15 )
    development_status: null
    source_model: Open source
    os_family: Unix-like
    gui: null
    platforms: Apple IIGS
    kernel_type: null
    license: Freeware
# END GENERATED ENWIKI INFOBOX
---

# GNO/ME

GNO/ME is documented by its maintained project site as a UNIX-like Apple IIGS environment running on GS/OS.[^gno-site]

[^gno-site]: [GNO/ME home](https://www.gno.org/gno/)
