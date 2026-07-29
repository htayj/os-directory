---
type: Operating System
title: Interlisp-D / Medley
description: Xerox's integrated graphical Interlisp workstation environment, later renamed Medley and ported from D-machines to a virtual machine.
tags: [operating-system, integrated-environment, xerox, interlisp, medley]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "Machine lineage, graphical environment, Medley rename, virtual-machine port, and TEdit are documented. The record preserves the Xerox 1100 Alto Executive boot layer." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: documented, checked_at: 2026-07-29 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29 }
  - { field: latest_releases, disposition: not-researched, checked_at: 2026-07-29 }
  - { field: kernels, disposition: no-evidence-found, checked_at: 2026-07-29 }
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: lisp-machine-hardware-audit, language: en, source: parc-archive, observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: Interlisp-D, kind: official, language: en, script: Latn, evidence: [xerox-1100-manual, parc-archive], assertion_status: documented }
  - { value: Medley, kind: later-name, language: en, script: Latn, evidence: [parc-archive], assertion_status: documented }
organizations:
  - { organization: "Xerox PARC", roles: [developer], evidence: [parc-archive], assertion_status: documented }
  - { organization: Venue, roles: [later-vendor], evidence: [parc-archive], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: research-and-commercial-product, primary: true, evidence: [parc-archive], assertion_status: documented }
design_purposes:
  - { value: interactive-lisp-development, primary: true, evidence: [xerox-1100-manual], assertion_status: documented }
  - { value: personal-graphical-workstation, primary: true, evidence: [parc-archive], assertion_status: documented }
development_status: { value: maintained-preservation-lineage, evidence: [interlisp-project], assertion_status: documented, scope: { as_of: 2026-07-29 } }
rights_regime: { value: mixed-historical-and-current, evidence: [parc-archive, interlisp-project], assertion_status: provisional }
licenses:
  - { identifier: MIT, name: "MIT License", scope: { component: "most software in the current Medley Interlisp Project" }, evidence: [interlisp-project], assertion_status: documented }
programming_languages:
  - { language: Interlisp, extent: primary, evidence: [parc-archive], assertion_status: documented }
  - { language: BCPL, extent: component, evidence: [xerox-1100-manual], assertion_status: documented }
system_organization:
  - { value: integrated-graphical-lisp-environment, evidence: [parc-archive], assertion_status: documented }
gui_status:
  - { value: graphical, evidence: [parc-archive], assertion_status: documented }
interfaces:
  - { name: "Interlisp-D graphical environment", style: graphical, modalities: [keyboard, pointing-device], evidence: [parc-archive], assertion_status: documented }
hardware_platforms:
  - { value: "Xerox Dorado", evidence: [parc-archive], assertion_status: documented }
  - { value: "Xerox Dolphin / 1100", evidence: [parc-archive, xerox-1100-manual], assertion_status: documented }
  - { value: "Xerox Dandelion / 1108", evidence: [parc-archive, xerox-1100-manual], assertion_status: documented }
  - { value: "Xerox Daybreak / 1186", evidence: [parc-archive], assertion_status: documented }
virtual_platforms:
  - { value: "C virtual machine on Unix and Linux hosts", evidence: [parc-archive], assertion_status: documented }
host_environments:
  - { value: "Alto Executive on Xerox 1100 boot path", evidence: [xerox-1100-manual], assertion_status: documented }
machine_classes: [lisp-machine, workstation, virtual-machine]
lineage:
  - { relationship: renamed-to, target: Medley, evidence: [parc-archive], assertion_status: documented }
known_gaps:
  - { value: "The current project's MIT licensing statement does not establish the license terms of every historical Xerox or Venue release.", evidence: [interlisp-project], assertion_status: documented }
sources:
  - { id: xerox-1100-manual, resource: "https://xeroxparcarchive.computerhistory.org/eris/lispmanual/.CHAPX1100.PRESS%211.pdf", title: "Using Interlisp-D on the Xerox 1100", author: Xerox, source_kind: contemporary-system-manual }
  - { id: parc-archive, resource: "https://xeroxparcarchive.computerhistory.org/Xerox_PARC_source_code.html", title: "Xerox PARC source code archive: Lisp and Interlisp", author: "Computer History Museum", source_kind: institutional-source-archive }
  - { id: interlisp-project, resource: "https://interlisp.org/", title: "Medley Interlisp Project", source_kind: official-preservation-project }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: TEdit
  relationship: native
  interface_style: graphical
  source: https://xeroxparcarchive.computerhistory.org/Xerox_PARC_source_code.html
  source_kind: institutional-source-archive
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Overview

Interlisp-D was Xerox's integrated graphical Lisp environment for the Dorado,
Dolphin, Dandelion, and Daybreak D-machine families. Xerox's final Interlisp-D
release was renamed Medley, and a later C virtual-machine implementation brought
the environment to Unix and Linux hosts.[^parc-archive]

# Layering boundary

On a Xerox 1100, the machine boots the Alto Executive and starts Interlisp-D
from that command environment. This record therefore treats Interlisp-D/Medley
as the dominant integrated graphical operating environment without erasing the
separate boot executive documented by Xerox.[^xerox-1100-manual]

# Text editor

The preserved PARC source collection identifies TEdit as the Interlisp-D text
editing tool and retains its 1986 source snapshot.[^parc-archive]

[^parc-archive]: [Xerox PARC source code archive: Lisp and Interlisp](https://xeroxparcarchive.computerhistory.org/Xerox_PARC_source_code.html).
[^xerox-1100-manual]: [Using Interlisp-D on the Xerox 1100](https://xeroxparcarchive.computerhistory.org/eris/lispmanual/.CHAPX1100.PRESS%211.pdf), sections 22.3–22.11.
