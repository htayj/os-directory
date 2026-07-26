---
type: Operating System
title: Fire OS
description: Amazon operating system for Fire TV and Fire tablet devices.
tags: [operating-system, amazon, android, embedded]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: Draft coverage record; no verified claim is asserted. }
field_dispositions:
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: kernels, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26, reason: Amazon documentation identifies supported OSes and devices, not a full system license. }
source_list:
  title: List of operating systems
  revision: 1365063001
  occurrences:
    - { section: [Proprietary, Amazon], label: Fire OS, position: 6, target: https://en.wikipedia.org/wiki/Fire_OS, depth: 1 }
discovery_provenance:
  - { method: english-list, language: en, native_label: Fire OS, source: wikipedia, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: Fire OS, kind: official, language: en, script: Latn, evidence: [amazon-fire], assertion_status: documented }
organizations:
  - { organization: Amazon.com, Inc., roles: [developer, vendor], evidence: [amazon-fire], assertion_status: documented }
countries_of_origin: [US]
development_origins:
  - { country: US, organization: Amazon.com, Inc., role: origin, evidence: [wikipedia], assertion_status: provisional }
design_purposes:
  - { value: consumer-media-device, primary: true, evidence: [amazon-fire], assertion_status: documented }
development_status: { value: active, evidence: [amazon-fire], assertion_status: documented }
support_status: { value: active, evidence: [amazon-fire], assertion_status: documented }
distribution_status: { value: bundled, evidence: [amazon-fire], assertion_status: documented }
rights_regime: { value: copyrighted, evidence: [wikipedia], assertion_status: provisional }
software_freedom_status: { value: mixed, evidence: [wikipedia], assertion_status: provisional }
programming_languages: []
system_organization: []
kernels: []
gui_status: { value: integrated, evidence: [amazon-fire], assertion_status: documented }
interfaces:
  - { name: Fire TV interface, style: graphical, evidence: [amazon-fire], assertion_status: documented }
hardware_platforms:
  - { platform: Amazon Fire TV, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [amazon-fire], assertion_status: documented }
  - { platform: Amazon Fire tablets, support_origin: original-target, support_status: supported, execution_mode: native, evidence: [amazon-fire], assertion_status: documented }
architectures: []
sources:
  - { id: wikipedia, resource: https://en.wikipedia.org/wiki/Fire_OS, title: Fire OS, source_kind: article }
  - { id: amazon-fire, resource: https://developer.amazon.com/docs/fire-tv/fire-os-overview.html, title: Fire OS Overview, author: organization:amazon, source_kind: documentation }
---

## Overview

Amazon documents Fire OS as the operating system running Fire TV and tablet
devices, with Android-compatible application development for many devices.[^amazon-fire]

[^wikipedia]: [Wikipedia discovery page](https://en.wikipedia.org/wiki/Fire_OS).
[^amazon-fire]: [Amazon Fire OS overview](https://developer.amazon.com/docs/fire-tv/fire-os-overview.html).
