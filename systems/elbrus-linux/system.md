---
type: Operating System
title: Elbrus Linux
description: MCST GNU/Linux operating-system lineage for Elbrus, SPARC, and selected x86 computers.
tags: [operating-system, linux, elbrus, russian-computing]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness:
  level: core
  note: Source-reviewed against current MCST product pages; unresolved core fields carry explicit dispositions.
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - field: first_release
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: The reviewed version table begins with the 3.0 stream and does not establish the lineage's first release.
    evidence: [mcst-product]
  - field: last_updated.value
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: MCST identifies a current version but does not date that release on the reviewed page.
    evidence: [mcst-product]
  - field: licenses
    disposition: no-evidence-found
    checked_at: 2026-07-26
    reason: The reviewed pages establish commercial licensing and mixed components but not one complete license expression for the distribution.
    evidence: [mcst-product, mcst-family]
  - field: programming_languages
    disposition: not-researched
    checked_at: 2026-07-26
  - field: kernels.architecture
    disposition: not-researched
    checked_at: 2026-07-26
  - field: interfaces.command-line
    disposition: not-researched
    checked_at: 2026-07-26
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences: []
discovery_provenance:
  - method: hardware-ecosystem
    language: ru
    native_label: ОС «Эльбрус Линукс»
    source: mcst-product
    observed_at: 2026-07-26
    disposition: included-system
same_as:
  - https://ru.wikipedia.org/wiki/ОС_Эльбрус
names:
  - value: Эльбрус Линукс
    kind: official
    language: ru
    script: Cyrl
    evidence: [mcst-product]
    assertion_status: documented
  - value: Elbrus Linux
    kind: translated
    language: en
    script: Latn
    evidence: [mcst-product]
    assertion_status: documented
  - value: ОС «Эльбрус»
    kind: alias
    language: ru
    script: Cyrl
    evidence: [mcst-product]
    assertion_status: documented
  - value: OSL
    kind: alias
    language: en
    script: Latn
    evidence: [mcst-product]
    assertion_status: documented
organizations:
  - organization: https://www.mcst.ru/
    roles: [creator, developer, maintainer, vendor, rights-holder]
    evidence: [mcst-product]
    assertion_status: documented
countries_of_origin: [RU]
development_origins:
  - country: RU
    place: Moscow
    organization: https://www.mcst.ru/
    role: origin
    evidence: [mcst-product]
    assertion_status: documented
development_contexts:
  - value: commercial-product
    primary: true
    evidence: [mcst-product]
    assertion_status: documented
design_purposes:
  - value: hardware-enablement
    primary: true
    source_term: эффективно использовать аппаратно-программную платформу Эльбрус
    evidence: [mcst-product]
    assertion_status: documented
  - value: software-development
    primary: false
    evidence: [mcst-product]
    assertion_status: documented
design_goals:
  - value: compatibility
    note: Supports development, porting, and building applications for the Elbrus platform.
    evidence: [mcst-product]
    assertion_status: documented
application_domains: []
target_audiences:
  - value: Elbrus computer operators and application developers
    evidence: [mcst-product]
    assertion_status: documented
documented_uses: []
deployment_roles:
  - { value: workstation, evidence: [mcst-product], assertion_status: documented }
  - { value: server, evidence: [mcst-product], assertion_status: documented }
system_traits:
  - { value: linux-distribution, evidence: [mcst-product], assertion_status: documented }
classification_labels:
  - { value: GNU/Linux, evidence: [mcst-product], assertion_status: documented }
standards: []
development_status:
  value: active
  evidence: [mcst-product, mcst-family]
  assertion_status: documented
support_status:
  value: active
  evidence: [mcst-family]
  assertion_status: documented
distribution_status:
  value: commercial
  evidence: [mcst-product]
  assertion_status: documented
lifecycle_events:
  - kind: first-public-release
    subject: 3.0 stream
    value: 2016-01
    precision: month
    qualifier: exact
    evidence: [mcst-product]
    assertion_status: documented
  - kind: first-public-release
    subject: 9.x stream
    value: 2025-07
    precision: month
    qualifier: exact
    evidence: [mcst-product]
    assertion_status: documented
release_streams:
  - name: 9.x
    status: stable
    kernel: Linux 6.1
    evidence: [mcst-family, mcst-product]
  - name: 8.x
    status: stable
    kernel: Linux 5.10
    evidence: [mcst-product]
first_release:
latest_releases:
  - stream: 9.x
    version: 9.4.7
    evidence: [mcst-product]
    assertion_status: documented
last_updated:
  kind: release
  subject: 9.4.7
  evidence: [mcst-product]
  assertion_status: documented
rights_regime:
  value: copyrighted
  scope: { distribution: Elbrus Linux }
  evidence: [mcst-product]
  assertion_status: documented
software_freedom_status:
  value: mixed
  note: MCST describes a commercially licensed distribution containing the Linux kernel, GNU utilities, and other open-source applications.
  evidence: [mcst-product]
  assertion_status: documented
licenses: []
source_preservation:
  survival: substantial
  access: restricted
  authorization: authorized
  note: MCST states that source for distribution packages is available through its platform development kit on request.
  evidence: [mcst-family, mcst-product]
binary_preservation:
  survival: substantial
  access: commercial
  authorization: authorized
  evidence: [mcst-product]
documentation_preservation:
  survival: substantial
  access: public
  authorization: authorized
  evidence: [mcst-product]
rights_notes:
  - value: MCST states that it holds exclusive rights to the product and sells perpetual use licenses.
    evidence: [mcst-product]
    assertion_status: documented
official_sites:
  - { value: https://www.mcst.ru/elbrus_linux, evidence: [mcst-product], assertion_status: documented }
repositories: []
programming_languages: []
system_organization:
  - value: distinct-kernel
    source_term: ядро Linux
    evidence: [mcst-product]
    assertion_status: documented
kernels:
  - name: Linux
    architecture: unknown
    scope:
      releases: [9.x]
    version: "6.1"
    evidence: [mcst-product, mcst-family]
    assertion_status: documented
  - name: Linux
    architecture: unknown
    scope:
      releases: [8.x]
    version: "5.10"
    evidence: [mcst-product]
    assertion_status: documented
userlands:
  - value: GNU plus MCST and other application packages
    evidence: [mcst-product]
    assertion_status: documented
apis_abis: []
binary_formats: []
execution_environments:
  - value: x86 binary translation
    scope: { platforms: [Elbrus architecture] }
    evidence: [mcst-product]
    assertion_status: documented
build_toolchains:
  - value: PDK
    note: MCST platform development kit and package build system.
    evidence: [mcst-product]
    assertion_status: documented
gui_status:
  - value: optional-first-party
    scope: { releases: [9.x] }
    evidence: [mcst-product]
    assertion_status: documented
interfaces:
  - name: Xfce
    style: graphical
    modalities: [keyboard, pointer]
    provisioning: bundled-optional
    access: local-session
    scope: { releases: [9.x] }
    version: 4.20.0
    evidence: [mcst-product]
    assertion_status: documented
shells: []
window_systems: []
desktop_environments:
  - name: Xfce
    scope: { releases: [9.x] }
    version: 4.20.0
    evidence: [mcst-product]
    assertion_status: documented
accessibility: []
localization: []
hardware_platforms:
  - platform: Elbrus computer family
    support_origin: original-target
    support_status: supported
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
  - platform: MCST-R SPARC systems
    support_origin: official-port
    support_status: supported
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
  - platform: x86 personal computers
    support_origin: official-port
    support_status: supported
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
architectures:
  - value: Elbrus e2k
    variants: [e2k-v1, e2k-v2, e2k-v3, e2k-v4, e2k-v5, e2k-v6, e2k-v7]
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
  - value: SPARC
    variants: [V8, V9]
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
  - value: x86
    variants: [x86-32, x86-64]
    execution_mode: native
    evidence: [mcst-product]
    assertion_status: documented
machine_classes:
  - { value: workstation, evidence: [mcst-product], assertion_status: documented }
  - { value: server, evidence: [mcst-product], assertion_status: documented }
host_environments: []
virtual_platforms: []
minimum_requirements: []
boot_requirements: []
required_peripherals: []
boot_and_initialization: []
process_task_thread_model: []
scheduling: []
concurrency: []
user_model: []
memory_management: []
protection_domains: []
filesystems: []
storage_model: []
io_model: []
networking: []
distributed_system_model: []
security: []
accounting_and_auditing: []
ipc: []
drivers: []
configuration_model: []
installation_model:
  - value: Bootable installation-disc set
    evidence: [mcst-product]
    assertion_status: documented
package_management:
  - { value: dpkg, evidence: [mcst-product], assertion_status: documented }
  - { value: apt, evidence: [mcst-product], assertion_status: documented }
package_formats:
  - { value: deb, evidence: [mcst-product], assertion_status: documented }
virtualization: []
reliability: []
real_time:
  - value: soft-real-time-capable-kernel-variant
    source_term: rt Real Time
    note: MCST lists an RT kernel variant; hard or firm real-time guarantees were not established.
    evidence: [mcst-product]
    assertion_status: documented
power_management: []
graphics_multimedia: []
certifications: []
documented_limits: []
lineage: []
compatibility: []
influences: []
historical_significance: []
limitations: []
distribution_media:
  - { value: optical-disc-image, evidence: [mcst-product], assertion_status: documented }
  - { value: network-download, evidence: [mcst-family], assertion_status: documented }
update_mechanisms:
  - { value: package-repository, evidence: [mcst-product], assertion_status: documented }
surviving_artifacts: []
emulation: []
archives: []
known_gaps:
  - { value: Exact first release of the full lineage, assertion_status: unknown }
  - { value: Complete distribution-wide license expression, assertion_status: unknown }
  - { value: Implementation-language breakdown by component and release, assertion_status: unknown }
sources:
  - id: mcst-product
    resource: https://www.mcst.ru/elbrus_linux
    original_title: Операционная система «Эльбрус Линукс» (ТВГИ.00333-01)
    translated_title: Elbrus Linux operating system
    language: ru
    author: organization:mcst
    source_kind: vendor-product-documentation
    accessed: 2026-07-26
  - id: mcst-family
    resource: https://www.mcst.ru/elbrus_os
    original_title: Операционные системы «Эльбрус»
    translated_title: Elbrus operating systems
    language: ru
    author: organization:mcst
    source_kind: vendor-product-matrix
    accessed: 2026-07-26
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

# Overview

Elbrus Linux is MCST's GNU/Linux operating-system lineage for computers using
Elbrus, MCST-R SPARC, and selected x86 architectures.[^mcst-product] MCST also
uses the names ОС «Эльбрус» and OSL for the product, but currently lists
Эльбрус-Д separately; those identity boundaries need release-level review.

# Purpose and Design Goals

MCST describes the system as a software platform for operating, testing, and
supporting Elbrus hardware and for developing, porting, and building
applications for it.[^mcst-product]

# History and Releases

The reviewed MCST matrix identifies stable 8.x and 9.x streams. The 9.x stream
first appeared in July 2025 and is shown at version 9.4.7 with Linux 6.1 as of
the catalog cutoff.[^mcst-product] The table does not establish the first
release of the overall lineage.

# Licensing and Availability

MCST sells perpetual licenses and identifies itself as the exclusive
rights-holder, while the distribution incorporates the Linux kernel, GNU
utilities, and other open-source software.[^mcst-product] The aggregate
software-freedom status is therefore recorded as mixed pending a component- and
release-level license audit.

# Implementation and Kernel

The system uses Linux kernels, MCST system programs, GNU utilities, `deb`
packages, `dpkg`, `apt`, and MCST's PDK build environment.[^mcst-product]
Kernel architecture and implementation-language proportions remain open
research fields rather than being inferred from the upstream Linux project.

# Interfaces

MCST's current component table includes Xfce 4.20 in the 9.x graphical
environment.[^mcst-product] The reviewed source does not establish whether it
is the mandatory default or document command-line interaction in enough detail
for a normalized claim.

# Platforms

The lineage has supported Elbrus e2k generations, MCST-R SPARC V8/V9 systems,
and x86 variants; platform coverage changes substantially by release
stream.[^mcst-product]

# System Facilities

MCST distributes general-purpose, real-time, non-NUMA, and combined kernel
variants. The existence of an `rt` variant is not treated as proof of hard
real-time guarantees.[^mcst-product]

# Lineage and Compatibility

MCST describes Elbrus Linux as its own distribution while acknowledging Debian
technical solutions and identifying Linux and GNU as major components.[^mcst-product]
Those statements support component relationships, not a claim that every
release is simply a Debian derivative.

# Preservation

MCST currently exposes package information and documentation, distributes
installation images to customers or eligible hardware users, and provides
package source through its PDK request process.[^mcst-family][^mcst-product]
No exact image or source snapshot has yet been recorded as a
[software artifact](/schema/scope-and-identity.md).

# Open Questions

* What was the first release and original product name of this lineage?
* Which versions called ОС «Эльбрус», OSL, or ОПО «Эльбрус» belong to this
  lineage, and which require separate concepts?
* What complete license expression applies to each shipped distribution?
* Which languages implement MCST-specific kernel, toolchain, installer, GUI,
  and userland components?
* What sourced kernel-architecture classification applies to each kernel line?

[^mcst-product]: MCST, Операционная система «Эльбрус Линукс» (ТВГИ.00333-01).
[^mcst-family]: MCST, Операционные системы «Эльбрус».
