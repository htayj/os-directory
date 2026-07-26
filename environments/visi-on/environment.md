---
type: Graphical Operating Environment
title: Visi On
description: VisiCorp graphical office-application environment for MS-DOS on IBM PC compatibles.
tags: [graphical-environment, desktop, ms-dos, historical-gui]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness:
  level: core
  note: Core identity and interface claims were checked against the contemporary user guide and discovery sources; unresolved fields carry dispositions.
field_dispositions:
  - field: latest_releases.date
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: Version 1.01 is reported, but the reviewed sources do not establish its date.
    evidence: [wikipedia]
  - field: licenses
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: Copyright and proprietary distribution are established, but exact customer license terms were not located.
    evidence: [user-guide, wikipedia]
  - field: programming_languages.core
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: VisiC is documented for applications; the implementation languages of the environment itself remain unresolved.
    evidence: [wikipedia, guided-tour]
  - field: source_preservation
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: The source was reportedly transferred to Control Data, but no surviving accessible source snapshot was verified.
    evidence: [wikipedia]
discovery_provenance:
  - method: manual-search
    language: en
    native_label: Visi On
    source: wikipedia
    observed_at: 2026-07-26
    disposition: included-environment
    note: Included as a graphical operating environment, not as an independent operating system.
same_as:
  - https://www.wikidata.org/wiki/Q1450007
names:
  - value: Visi On
    kind: official
    language: en
    script: Latn
    evidence: [user-guide, wikipedia]
    assertion_status: documented
  - value: VisiOn
    kind: alias
    language: en
    script: Latn
    evidence: [wikipedia]
    assertion_status: documented
  - value: Visi On Applications Manager
    kind: product
    language: en
    script: Latn
    evidence: [user-guide]
    assertion_status: documented
  - value: Quasar
    kind: development
    language: en
    script: Latn
    evidence: [wikipedia]
    assertion_status: provisional
organizations:
  - organization: https://en.wikipedia.org/wiki/VisiCorp
    roles: [creator, developer, publisher, vendor, rights-holder]
    scope: { through: 1984 }
    evidence: [user-guide, wikipedia]
    assertion_status: documented
  - organization: https://en.wikipedia.org/wiki/Control_Data_Corporation
    roles: [rights-holder]
    scope: { from: 1984 }
    evidence: [wikipedia]
    assertion_status: documented
countries_of_origin: [US]
development_origins:
  - country: US
    place: California
    organization: https://en.wikipedia.org/wiki/VisiCorp
    role: origin
    evidence: [wikipedia]
    assertion_status: documented
development_contexts:
  - value: commercial-product
    primary: true
    evidence: [user-guide, wikipedia]
    assertion_status: documented
design_purposes:
  - value: personal-computing
    primary: true
    source_term: integrated office applications environment
    evidence: [user-guide]
    assertion_status: documented
  - value: software-development
    primary: false
    note: Supplied a common environment and application model for a family of office products.
    evidence: [guided-tour, wikipedia]
    assertion_status: documented
design_goals:
  - value: usability
    source_term: fast, easy, and professional aid
    evidence: [user-guide]
    assertion_status: documented
  - value: consistency
    note: Common interaction techniques across Visi On applications.
    evidence: [user-guide, guided-tour]
    assertion_status: documented
  - value: portability
    note: VisiMachine and VisiHost separated applications from machine-specific support.
    evidence: [guided-tour, wikipedia]
    assertion_status: documented
target_audiences:
  - value: professional and business IBM PC users
    evidence: [user-guide, wikipedia]
    assertion_status: documented
documented_uses: []
development_status:
  value: discontinued
  evidence: [wikipedia]
  assertion_status: documented
support_status:
  value: ended
  evidence: [wikipedia]
  assertion_status: documented
distribution_status:
  value: ended
  evidence: [wikipedia]
  assertion_status: documented
lifecycle_events:
  - kind: development-started
    value: 1981
    precision: year
    qualifier: exact
    evidence: [wikipedia]
    assertion_status: provisional
  - kind: first-demonstrated
    value: 1982
    precision: year
    qualifier: exact
    note: Demonstrated at the fall COMDEX show.
    evidence: [wikipedia]
    assertion_status: documented
  - kind: first-public-release
    value: 1983-12-16
    precision: day
    qualifier: exact
    evidence: [wikipedia]
    assertion_status: documented
  - kind: distribution-ended
    value: 1985
    precision: year
    qualifier: circa
    evidence: [wikipedia]
    assertion_status: inferred
first_release:
  value: 1983-12-16
  precision: day
  qualifier: exact
  evidence: [wikipedia]
  assertion_status: documented
latest_releases:
  - version: "1.01"
    evidence: [wikipedia]
    assertion_status: provisional
last_updated:
  kind: release
  subject: "1.01"
  evidence: [wikipedia]
  assertion_status: provisional
rights_regime:
  value: copyrighted
  evidence: [user-guide]
  assertion_status: documented
software_freedom_status:
  value: proprietary
  evidence: [wikipedia]
  assertion_status: documented
licenses: []
programming_languages:
  - language: VisiC
    source_term: subset of C
    kind: high-level
    extent: component
    roles: [applications]
    evidence: [wikipedia, guided-tour]
    assertion_status: documented
environment_kind: graphical-operating-environment
host_systems:
  - system: https://en.wikipedia.org/wiki/MS-DOS
    version: "2.0"
    relationship: required-host
    provisioning: separately-required
    evidence: [wikipedia]
    assertion_status: documented
host_relationship: layered
display_architecture:
  - value: bitmap graphical display
    resolution: 640x200 monochrome
    adapter: CGA-compatible
    evidence: [wikipedia]
    assertion_status: documented
  - value: VisiHost and VisiMachine portability layer
    evidence: [guided-tour, wikipedia]
    assertion_status: documented
ui_paradigms:
  - { value: desktop-metaphor, evidence: [user-guide], assertion_status: documented }
  - { value: direct-manipulation, evidence: [user-guide], assertion_status: documented }
  - { value: application-centric, evidence: [user-guide], assertion_status: documented }
  - { value: menu-based, evidence: [user-guide], assertion_status: documented }
window_model:
  - value: multiple resizable application windows
    capabilities: [open, resize, reposition, full-screen, set-aside, restore]
    evidence: [user-guide, wikipedia]
    assertion_status: documented
input_model:
  - modalities: [keyboard, pointer]
    required_pointer: Mouse Systems-compatible two-button mouse
    evidence: [user-guide, wikipedia]
    assertion_status: documented
desktop_components:
  - { value: Services options, evidence: [user-guide], assertion_status: documented }
  - { value: online help, evidence: [user-guide, wikipedia], assertion_status: documented }
  - { value: closed-window list, evidence: [user-guide], assertion_status: documented }
file_managers:
  - value: none
    note: The environment did not include a graphical file manager.
    evidence: [wikipedia]
    assertion_status: documented
session_management: []
application_model:
  - value: native Visi On windowed applications
    capabilities: [multiple-open-applications, common-ui, cross-window-data-transfer]
    evidence: [user-guide, guided-tour]
    assertion_status: documented
  - value: VisiMachine virtual application target
    evidence: [guided-tour, wikipedia]
    assertion_status: documented
toolkits:
  - value: Basic Interaction Techniques
    note: Common interaction operations supplied to applications.
    evidence: [guided-tour]
    assertion_status: documented
environment_apis:
  - value: VisiMachine application interface
    evidence: [guided-tour, wikipedia]
    assertion_status: documented
bundled_applications:
  - { value: Visi On Calc, provisioning: separate-first-party, evidence: [user-guide, wikipedia], assertion_status: documented }
  - { value: Visi On Word, provisioning: separate-first-party, evidence: [user-guide, wikipedia], assertion_status: documented }
  - { value: Visi On Graph, provisioning: separate-first-party, evidence: [user-guide, wikipedia], assertion_status: documented }
  - { value: Visi On Query, provisioning: separate-first-party, evidence: [user-guide], assertion_status: documented }
visual_design:
  - value: monochrome bitmapped desktop with windows and menus
    evidence: [user-guide, wikipedia]
    assertion_status: documented
  - value: hourglass busy cursor
    evidence: [wikipedia]
    assertion_status: documented
hardware_platforms:
  - platform: IBM PC and compatible computers
    support_origin: original-target
    support_status: supported
    execution_mode: native
    evidence: [wikipedia]
    assertion_status: documented
architectures:
  - value: Intel 8086
    execution_mode: native
    evidence: [wikipedia]
    assertion_status: documented
minimum_requirements:
  - memory: 512 KiB
    storage: 5 MB hard disk
    removable_media: one DS/DD floppy drive
    graphics: CGA-compatible 640x200 monochrome
    peripherals: [RS-232 serial port, Mouse Systems-compatible mouse]
    host_system: MS-DOS 2.0
    evidence: [wikipedia]
    assertion_status: documented
distribution_media:
  - { value: floppy-disk, evidence: [wikipedia], assertion_status: documented }
source_preservation:
documentation_preservation:
  survival: substantial
  access: public
  authorization: permission-unclear
  evidence: [user-guide]
binary_preservation:
  survival: substantial
  access: restricted
  authorization: permission-unclear
  note: Preserved media images are reported, but no exact artifact was verified for this record.
  evidence: [wikipedia]
surviving_artifacts: []
emulation: []
known_gaps:
  - { value: Exact date and contents of version 1.01, assertion_status: unknown }
  - { value: Complete implementation-language breakdown, assertion_status: unknown }
  - { value: Exact customer license terms, assertion_status: unknown }
  - { value: Provenance and checksums for surviving installation media, assertion_status: unknown }
sources:
  - id: user-guide
    resource: https://toastytech.com/manuals/Visi%20On%20AM%20Users%20Guide.pdf
    title: Visi On Applications Manager User's Guide
    language: en
    author: organization:visicorp
    source_kind: contemporary-user-manual
    accessed: 2026-07-26
  - id: guided-tour
    resource: https://guidebookgallery.org/articles/aguidedtourofvision
    title: A Guided Tour of Visi On
    language: en
    author: human:phil-lemmons
    source_kind: contemporary-trade-press-interview
    accessed: 2026-07-26
  - id: wikipedia
    resource: https://en.wikipedia.org/w/index.php?title=Visi_On&oldid=1321248446
    title: Visi On
    language: en
    author: community:wikipedia-editors
    source_kind: discovery-secondary-reference
    last_modified: 2025-11-09
    accessed: 2026-07-26
---

# Overview

Visi On was VisiCorp's separately sold graphical operating environment for
MS-DOS 2.0 on IBM PC-compatible hardware.[^user-guide][^wikipedia] It receives
its own environment concept because it supplied a distinct application model,
windowing interface, release history, and development toolchain; it is not
treated as an independent operating system.

# Purpose and Design

VisiCorp designed Visi On as an integrated office-application environment with
a common interface and data exchange among applications.[^user-guide] Its
VisiMachine/VisiHost split was intended to isolate applications from
machine-specific support and make the system portable.[^guided-tour]

# History and Releases

Visi On was demonstrated at COMDEX in 1982 and commercially shipped in December
1983.[^wikipedia] The source code was sold to Control Data in 1984, and the
product disappeared during VisiCorp's decline. Version 1.01 is reported as the
latest release, but its release date remains unresolved.

# Host Systems and Platforms

The released IBM PC version required MS-DOS 2.0, 512 KiB of memory, a hard
disk, floppy drive, CGA-compatible monochrome graphics, and a
Mouse Systems-compatible mouse.[^wikipedia]

# Interface and Visual Model

The environment presented a bitmapped desktop with menus, online help, and
multiple application windows that could be resized, moved, expanded, set
aside, and restored.[^user-guide] Visi On used keyboard and mouse input but did
not include a graphical file manager.[^wikipedia]

# Application Architecture

Native applications targeted the VisiMachine abstraction and shared common
interaction techniques. The environment supported several open applications
and transfer of information between their windows.[^user-guide][^guided-tour]
VisiC, a restricted C subset, was used for application development; this does
not establish the implementation language of every environment component.

# Licensing and Distribution

The contemporary guide carries a 1983 VisiCorp copyright notice.[^user-guide]
The product was commercially and proprietarily distributed, but the exact
customer license terms have not yet been recovered.

# Preservation

Scanned manuals survive publicly, and preserved floppy images are reported,
but the catalog has not yet verified exact image provenance, completeness, or
checksums. Those objects will become separate software-artifact concepts.

# Open Questions

* What changed in release 1.01, and when did it ship?
* Which languages implemented VisiHost, VisiMachine, window management, and
  device support?
* Does the Control Data source transfer survive in an accessible archive?
* Which preserved disk sets are complete, authentic, and legally distributable?

[^user-guide]: VisiCorp, Visi On Applications Manager User's Guide, 1983.
[^guided-tour]: Phil Lemmons, A Guided Tour of Visi On, BYTE, June 1983.
[^wikipedia]: Wikipedia, Visi On, revision 1321248446, used as a discovery and secondary source.
