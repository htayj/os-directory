---
type: Catalog Schema
title: Operating-system field vocabulary
description: Normalized identity, purpose, chronology, licensing, implementation, interface, platform, technical, and preservation attributes.
tags: [schema, vocabulary, operating-system]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
vocabulary_version: "0.1"
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format specification, version 0.2
    author: organization:google-cloud-platform
---

# Representation Rules

This vocabulary extends OKF v0.2 with domain fields.[^okf-spec] Use a scalar
only for a fact stable across the full system lineage. Repeatable or changing
facts use claim mappings with evidence and release, platform, or date scope.

# Common Claim Envelope

Repeatable factual entries should use the applicable parts of this envelope:

```yaml
value:
source_term:
scope:
  releases: []
  editions: []
  platforms: []
  from:
  through:
evidence: [source-id]
assertion_status: documented
note:
```

`assertion_status` is `documented`, `inferred`, `disputed`, `provisional`, or
`unknown`. Conflicting claims coexist as separate entries. A temporal value
also uses:

```yaml
value: YYYY-MM-DD
precision: day
qualifier: exact
```

`precision` is `day`, `month`, or `year`; `qualifier` is `exact`, `circa`,
`before`, `after`, `range`, or `uncertain`. Granularity, uncertainty, and
disagreement are separate dimensions.

# Record Control

| Field | Shape | Meaning |
|---|---|---|
| `schema_version` | string | Version of this catalog vocabulary. |
| `as_of` | date | Observation cutoff for changeable claims. |
| `catalog_completeness` | mapping | Level (`inventory`, `core`, `deep`) and review notes. |
| `field_dispositions` | list of mappings | Field path, disposition, reason, date checked, and evidence. |
| `source_list` | mapping | Frozen list revision and all occurrence records. |
| `discovery_provenance` | list of mappings | Coverage set, method, language, source, native label, date, and candidate disposition. |
| `same_as` | list of URIs | External authority records for the same identity. |

Field dispositions are `not-researched`, `no-evidence-found`, `unknown`,
`disputed`, `not-applicable`, or `withheld`. This is more precise than treating
an empty list as proof that a feature did not exist.

Each `source_list.occurrences` item records `section`, `label`, `position`,
`target`, nesting context, and optional annotation. Repeated list appearances
therefore remain visible after identity deduplication.

Discovery methods include `english-list`, `wikidata-query`,
`multilingual-list`, `multilingual-article`, `hardware-ecosystem`,
`institutional-history`, `archive-catalog`, `bibliography`, `lineage-link`,
`category-traversal`, and `manual-search`. Candidate dispositions are
`included-system`, `included-release`, `included-environment`,
`included-artifact`, `alias`, `duplicate`, `not-an-operating-system`,
`insufficient-evidence`, and `needs-review`.

# Identity, Origin, and Stewardship

| Field | Shape | Meaning |
|---|---|---|
| `names` | list of claims | Official, short, former, development, translated, transliterated, or alias names, with BCP 47 language and ISO 15924 script. |
| `organizations` | list of claims | Organization path, roles, and time/release scope. |
| `countries_of_origin` | list of ISO 3166-1 alpha-2 codes | Filterable summary derived from origin-role entries. |
| `development_origins` | list of claims | Country, place, organization, development role, and scope. |
| `same_as` | list of URIs | Wikidata, authority-file, or other same-identity URIs. |

Organization roles are `creator`, `developer`, `maintainer`, `sponsor`,
`funder`, `commissioner`, `publisher`, `vendor`, `distributor`,
`support-provider`, `rights-holder`, `standards-body`, and
`preservation-custodian`.

Country of origin means where original development occurred, not the present
headquarters of a later owner. Development-origin roles are `origin`,
`major-development`, `port`, and `stewardship`. A genuinely multinational
origin has multiple country codes.

For names written in non-Latin scripts, retain the exact native form,
`language`, `script`, and any `transliteration_scheme`. An English rendering
does not replace the source-language name.

# Source-Language Metadata

Each `sources` entry may extend OKF with:

| Field | Meaning |
|---|---|
| `language` | BCP 47 language tag of the source. |
| `original_title` | Title exactly as published. |
| `translated_title` | Catalog-supplied English title, when useful. |
| `translation_by` | Human, named translation, or declared machine/tool actor. |
| `accessed` | Date the source was consulted. |
| `archived_resource` | Stable archived copy when the live resource is fragile. |
| `source_kind` | Manual, release note, source tree, article, catalog, oral history, or other kind. |

Translate for discovery and summary, but cite the original-language evidence.
Machine translation does not elevate a source's trust tier.

# Purpose, Context, and Classification

| Field | Shape | Meaning |
|---|---|---|
| `development_contexts` | list of claims | Institutional/social context in which development began or continued. |
| `design_purposes` | list of claims | Why the system was created, with `primary` and source terminology. |
| `design_goals` | list of claims | Stated technical or social design goals. |
| `application_domains` | list of claims | Intended problem or industry domains. |
| `target_audiences` | list of claims | Intended operators, developers, learners, institutions, or markets. |
| `documented_uses` | list of claims | Evidence of actual later use, distinct from original purpose. |
| `deployment_roles` | list of claims | Desktop, server, control, appliance, or other operational roles. |
| `system_traits` | list of claims | Cross-cutting traits such as distributed, real-time, fault-tolerant, or language-oriented. |
| `classification_labels` | list of claims | Source-attributed labels such as Unix-like; not inferred from one feature. |
| `standards` | list of claims | Standard, conformance, certification, release, platform, and date scope. |

Development contexts are `commercial-product`, `internal-production`,
`academic-research`, `classroom-teaching`, `government-research`,
`government-mission`, `community-project`, `individual-hobby`,
`standards-reference`, `vendor-demonstration`, `reimplementation`,
`preservation-reconstruction`, `unknown`, and `other`.

Design purposes are `general-purpose-computing`, `batch-processing`,
`interactive-computing`, `time-sharing`, `transaction-processing`,
`personal-computing`, `software-development`, `operating-systems-education`,
`research-experimentation`, `hardware-enablement`, `compatibility`,
`portability-research`, `embedded-control`, `real-time-control`,
`network-services`, `distributed-computing`, `scientific-engineering`,
`business-data-processing`, `high-performance-computing`,
`high-availability`, `security-assurance`, `safety-critical`,
`communications`, `multimedia`, `gaming`, `mobile-handheld`, `hobby`,
`demonstration`, `preservation`, `unknown`, and `other`.

Design goals include `portability`, `compatibility`, `simplicity`,
`small-footprint`, `performance`, `deterministic-timing`, `reliability`,
`availability`, `security`, `safety`, `usability`, `extensibility`,
`modularity`, `scalability`, `distribution`, `energy-efficiency`, `low-cost`,
and `other`. Purpose, capability, and documented use must not be conflated.

# Lifecycle and Chronology

| Field | Shape | Meaning |
|---|---|---|
| `development_status` | claim | Current development state at `as_of`. |
| `support_status` | claim | Current official/community support state. |
| `distribution_status` | claim | Current availability or distribution state. |
| `lifecycle_events` | list of claims | Event kind, date, subject/version, and evidence. |
| `release_streams` | list of mappings | Independently maintained channel, edition, or platform streams. |
| `first_release` | temporal claim | Derived convenience summary for earliest documented release. |
| `latest_releases` | list of release claims | Latest release per relevant stream at `as_of`. |
| `last_updated` | event claim | Derived latest material product/project event and observation method. |

Development states are `planned`, `active`, `maintenance`, `feature-frozen`,
`completed`, `dormant`, `revived`, `inactive`, `abandoned`, `cancelled`,
`discontinued`, `superseded`, `unreleased`, and `unknown`. Support and
distribution use their own states rather than inheriting development state.

Lifecycle event kinds are `development-started`, `announced`,
`first-demonstrated`, `first-operational-use`, `first-public-release`,
`commercial-availability`, `release`, `last-release`, `last-source-change`,
`renamed`, `forked`, `revived`, `development-ended`, `distribution-ended`, and
`support-ended`. A web-page edit is not a product update. Multiple active
branches may each have a latest release.

# Rights, Licensing, and Availability

| Field | Shape | Meaning |
|---|---|---|
| `rights_regime` | claim | Copyright/public-domain characterization and scope. |
| `software_freedom_status` | claim | Freedom/source-access characterization and scope. |
| `licenses` | list of claims | Name, SPDX expression, source term, scope, components, licensor, and time/release scope. |
| `source_preservation` | mapping | Survival, access, authorization, completeness, and evidence. |
| `binary_preservation` | mapping | Survival, access, authorization, completeness, and evidence. |
| `documentation_preservation` | mapping | Survival, access, authorization, completeness, and evidence. |
| `rights_notes` | list of claims | Evidence-based qualifications, never unsourced legal conclusions. |
| `official_sites` | list of claims | Current or archived official project/product sites. |
| `repositories` | list of claims | Repository URI, role, branch/tag scope, and archival status. |

Rights regimes are `copyrighted`, `public-domain-dedication`,
`public-domain-status-claimed`, `mixed`, and `unknown`. Software-freedom states
are `free-open-source`, `source-available-nonfree`, `proprietary`,
`no-known-license`, `mixed`, `disputed`, and `unknown`. “No license found” does
not mean proprietary.

License scopes are `source`, `binary`, `documentation`, `sdk`, `tools`,
`kernel`, `userland`, `driver`, `component`, and `distribution`. Preservation
survival is `complete`, `substantial`, `partial`, `fragmentary`, `none-known`,
or `unknown`; access is `public`, `commercial`, `restricted`, `private`,
`inaccessible`, or `unknown`; authorization is `authorized`,
`permission-unclear`, `unauthorized`, or `unknown`. Survival, access, and
redistribution authority are independent.

# Implementation Languages and System Organization

| Field | Shape | Meaning |
|---|---|---|
| `programming_languages` | list of claims | Language, dialect/version, kind, extent, roles, components, ISA where relevant, and scope. |
| `system_organization` | list of claims | Overall organization, preserving historical terminology. |
| `kernels` | list of claims | Kernel name, architecture, modules, service/driver placement, protection and address-space models, lineage, and scope. |
| `userlands` | list of claims | Userland family, origin, components, and scope. |
| `apis_abis` | list of claims | Native and compatibility APIs/ABIs. |
| `binary_formats` | list of claims | Executable, object, library, or load-module formats. |
| `execution_environments` | list of claims | Runtimes, language environments, subsystems, personality layers, and hosted environments. |
| `build_toolchains` | list of claims | Compilers, assemblers, build systems, and source-generation tools. |

Language kinds are `high-level`, `assembly`, `machine-code`, `microcode`,
`domain-specific`, `generated`, and `unknown`. Extent is `primary`,
`substantial`, `component`, `tooling-only`, `generated-only`, or `unknown`.
Roles include `kernel`, `executive`, `bootloader`, `drivers`, `userland`,
`shell`, `gui`, `network-stack`, `filesystem`, `runtime`,
`compiler-toolchain`, `installer`, `build-tools`, `utilities`, and
`applications`. Assembly claims identify the ISA or dialect.

Overall system organization is `distinct-kernel`, `executive`,
`resident-monitor`, `supervisor-control-program`, `distributed-services`,
`no-distinct-kernel`, `unknown`, or `other`. This avoids forcing early systems
into later kernel terminology.

Kernel architectures are `monolithic`, `modular-monolithic`, `microkernel`,
`hybrid`, `exokernel`, `separation-kernel`, `nanokernel`, `multikernel`,
`layered`, `executive`, `monitor`, `other`, `unknown`, and `disputed`.
`library-os`, `unikernel`, `single-address-space`, and
`virtual-machine-based` are system traits unless a source explicitly calls them
kernel types. Preserve `source_term`; scope every kernel claim by release and
platform.

# Human and Programmatic Interfaces

| Field | Shape | Meaning |
|---|---|---|
| `gui_status` | list of claims | Derived scoped status of first-party graphical interaction. |
| `interfaces` | list of claims | Name, style, modalities, provisioning, access, and scope. |
| `shells` | list of claims | Command shell or command language. |
| `window_systems` | list of claims | Window server/system and scope. |
| `desktop_environments` | list of claims | Desktop environment and scope. |
| `accessibility` | list of claims | Accessibility interfaces or facilities. |
| `localization` | list of claims | Languages, locales, character sets, and internationalization facilities. |

Interface styles are `batch`, `command-line`, `full-screen-text`,
`menu-forms`, `graphical`, `conversational`, and `programmatic`. Modalities are
`punched-card`, `paper-tape`, `keyboard`, `pointer`, `touch`, `pen`, `voice`,
`front-panel`, `serial-terminal`, `video-terminal`, and `network-client`.
Provisioning is `built-in`, `bundled-default`, `bundled-optional`,
`separate-first-party`, or `third-party`. Access is `local-console`,
`local-session`, `remote-session`, `administrative`, or
`application-facing`.

`gui_status` is `integral`, `bundled-default`, `optional-first-party`,
`third-party-only`, `none-documented`, `unknown`, or `disputed`. “Headless” is
a deployment condition, not an interface style; touch and voice are modalities,
not proof of a GUI.

# Graphical-Environment Concepts

Graphical environments use the common identity, origin, purpose, lifecycle,
rights, implementation, platform, and preservation fields plus:

| Field | Shape | Meaning |
|---|---|---|
| `environment_kind` | value | `desktop-environment`, `graphical-operating-environment`, `window-system`, `display-server`, `workspace-manager`, `user-interface-shell`, or `integrated-gui`. |
| `host_systems` | list of claims | Required or supported host OS, version, relationship, and scope. |
| `host_relationship` | value | `layered`, `bundled-component`, `native-subsystem`, `replacement-shell`, `hosted-application`, or `standalone`. |
| `display_architecture` | list of claims | Display server, graphics layer, rendering, fonts, and client/server boundary. |
| `ui_paradigms` | list of claims | Desktop, document, application, workspace, menu, icon, direct-manipulation, or other interaction model. |
| `window_model` | list of claims | Overlap, tiling, stacking, resizing, minimization/set-aside, focus, and multiple-window behavior. |
| `input_model` | list of claims | Keyboard, pointer, touch, pen, voice, command, and accessibility interaction. |
| `desktop_components` | list of claims | Panel, launcher, dock, workspace switcher, notifications, settings, and related components. |
| `file_managers` | list of claims | Integrated, bundled, optional, or absent file-management interface. |
| `session_management` | list of claims | Login, session, startup, shutdown, persistence, and multi-user behavior. |
| `application_model` | list of claims | Native application lifecycle, multitasking, data exchange, document model, and compatibility. |
| `toolkits` | list of claims | Widget, UI, graphics, or application frameworks. |
| `environment_apis` | list of claims | Native API/ABI, extension, automation, and interoperability interfaces. |
| `bundled_applications` | list of claims | First-party applications and provisioning. |
| `visual_design` | list of claims | Sourced visual conventions, themes, icons, typography, and distinctive interaction features. |

Do not collapse these concepts into one “desktop environment” type. A display
server may support many desktops; a shell may replace one component; and a
graphical operating environment may provide its own application model while
still requiring a host OS.

# Platforms and Hardware Coupling

| Field | Shape | Meaning |
|---|---|---|
| `hardware_platforms` | list of claims | Platform path, support origin/status, execution mode, and scope. |
| `architectures` | list of claims | ISA family/variant, register width, address width, endianness, and scope. |
| `machine_classes` | list of claims | Hardware/device class and scope. |
| `host_environments` | list of claims | Required host OS, monitor, VM, firmware, or hypervisor. |
| `virtual_platforms` | list of claims | Virtual machines, abstract machines, hypervisors, or emulators treated as targets. |
| `minimum_requirements` | list of claims | Release-scoped CPU, memory, storage, display, and peripheral requirements. |
| `boot_requirements` | list of claims | Firmware, loader, media, console, and boot-device requirements. |
| `required_peripherals` | list of claims | Required or defining peripherals. |

Platform support origin is `original-target`, `official-port`, `vendor-port`,
`community-port`, `experimental-port`, or `unknown`; status is `announced`,
`supported`, `experimental`, `partial`, `cancelled`, or `unverified`;
execution mode is `native`, `hosted`, `virtualized`, `paravirtualized`,
`emulated`, or `translated`.

Endianness is `little`, `big`, `bi`, `mixed`, `not-applicable`, or `unknown`.
Machine classes include `supercomputer`, `mainframe`, `minicomputer`,
`workstation`, `server`, `personal-computer`, `microcomputer`,
`home-computer`, `mobile-phone`, `tablet`, `handheld-pda`, `wearable`,
`embedded-controller`, `industrial-control`, `automotive`,
`avionics-spacecraft`, `medical-device`, `telecom-system`, `router-switch`,
`storage-system`, `appliance`, `set-top-tv`, `game-console`, `calculator`,
`smart-card`, and `sensor-node`.

# Operating-System Facilities

| Field | Shape | Meaning |
|---|---|---|
| `boot_and_initialization` | list of claims | Boot stages, service initialization, and recovery startup. |
| `process_task_thread_model` | list of claims | Program, process, task, job, thread, and scheduling entities. |
| `scheduling` | list of claims | Algorithms, preemption, priorities, dispatch, and timing guarantees. |
| `concurrency` | list of claims | Multitasking, threading, multiprocessing, SMP, and NUMA. |
| `user_model` | list of claims | Single/multi-user, accounts, sessions, roles, and privilege. |
| `memory_management` | list of claims | Address spaces, protection, paging, segmentation, virtual memory, and swapping. |
| `protection_domains` | list of claims | Isolation boundaries and transitions. |
| `filesystems` | list of claims | Filesystem name, role, features, and scope. |
| `storage_model` | list of claims | Volumes, catalogs, records, removable media, and persistence. |
| `io_model` | list of claims | Device, channel, interrupt, asynchronous, and stream I/O models. |
| `networking` | list of claims | Stacks, protocols, distributed facilities, and network role. |
| `distributed_system_model` | list of claims | Naming, location, consistency, replication, and distribution model. |
| `security` | list of claims | Authentication, authorization, isolation, capabilities, and policy. |
| `accounting_and_auditing` | list of claims | Usage accounting, logs, audit trails, and certification evidence. |
| `ipc` | list of claims | Interprocess and inter-machine communication. |
| `drivers` | list of claims | Driver placement, interfaces, loading, and extension model. |
| `configuration_model` | list of claims | Configuration storage, discovery, policy, and administration. |
| `installation_model` | list of claims | Installation, system generation, imaging, or source-build process. |
| `package_management` | list of claims | Package managers and repositories. |
| `package_formats` | list of claims | Package, archive, patch, and update formats. |
| `virtualization` | list of claims | Hosted, guest, container, partition, or hypervisor facilities. |
| `reliability` | list of claims | Fault tolerance, recovery, clustering, and high availability. |
| `real_time` | list of claims | Hard, firm, or soft real-time behavior and bounded-latency evidence. |
| `power_management` | list of claims | Power states, energy policy, and battery support. |
| `graphics_multimedia` | list of claims | Display, graphics, audio, video, and input subsystems. |
| `certifications` | list of claims | Certification, evaluator, level, platform, release, and date. |
| `documented_limits` | list of claims | Users, tasks, memory, processors, storage, or other system limits. |

# Lineage, Compatibility, and Significance

| Field | Shape | Meaning |
|---|---|---|
| `lineage` | list of claims | Predecessor, successor, derivation, fork, port, merge, or rename relationship. |
| `compatibility` | list of claims | Source, binary, API, filesystem, data, or behavioral compatibility. |
| `influences` | list of claims | Documented design influence weaker than derivation. |
| `historical_significance` | list of claims | Source-attributed impact, innovation, adoption, or “first” claim. |
| `limitations` | list of claims | Documented constraints, omissions, or failure modes. |

Lineage relationships are `predecessor`, `successor`, `derived-from`,
`fork-of`, `port-of`, `based-on`, `merged-into`, and `renamed-to`. Standards,
Unix/POSIX labels, compatibility, trademark certification, and code lineage are
separate claims.

# Distribution and Preservation

| Field | Shape | Meaning |
|---|---|---|
| `distribution_media` | list of claims | Cards, paper tape, disk, tape, ROM, optical, network, download, or listing. |
| `update_mechanisms` | list of claims | Patch, package, image, over-the-air, source rebuild, or other update path. |
| `surviving_artifacts` | list of paths | Exact artifact concepts rather than release titles. |
| `emulation` | list of claims | Emulator, simulator, reconstruction, or compatibility environment and status. |
| `archives` | list of claims | Collection URI, custodian, scope, access, authorization, and fixity. |
| `known_gaps` | list of claims | Missing versions, components, documentation, source, provenance, or checksums. |

# Body Sections

Use structured frontmatter for comparison and prose for qualification:

* **Overview**
* **Purpose and Design Goals**
* **History and Releases**
* **Licensing and Availability**
* **Implementation and Kernel**
* **Interfaces**
* **Platforms**
* **System Facilities**
* **Lineage and Compatibility**
* **Preservation**
* **Open Questions**

[^okf-spec]: OKF permits producer-defined keys and requires consumers to preserve and tolerate unknown fields.
