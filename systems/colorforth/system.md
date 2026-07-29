---
type: Operating System
title: colorForth
description: Chuck Moore's compact color-tokenized Forth language, operating system, and integrated development environment for standalone PC-compatible hardware.
tags: [operating-system, forth, integrated-environment, colorforth, preservation]
status: draft
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
schema_version: "0.1"
as_of: 2026-07-29
catalog_completeness: { level: core, note: "The preserved official site establishes the integrated language/OS identity, standalone operation, platform class, interface design, implementation approach, and integral editor. Exact first release, last original update, formal license, and conventional kernel taxonomy remain unresolved." }
field_dispositions: [{field: text_editors, disposition: documented, checked_at: '2026-07-29'}, {field: rights_regime, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: licenses, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: kernels, disposition: not-applicable, checked_at: 2026-07-29, reason: The source describes an integrated standalone language and operating environment rather than a separable conventional kernel.}, {field: first_release, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: latest_releases, disposition: no-evidence-found, checked_at: 2026-07-29}, {field: last_updated, disposition: no-evidence-found, checked_at: 2026-07-29}]
source_list: { title: "List of operating systems", revision: 1365063001, occurrences: [] }
discovery_provenance:
  - { method: public-github-organization-audit, language: en, source: "https://github.com/colorforth/colorforth.github.io", observed_at: 2026-07-29, disposition: included-system }
names:
  - { value: "colorForth", kind: official, language: en, script: Latn, evidence: [colorforth-site, colorforth-repo], assertion_status: documented }
organizations:
  - { organization: "Chuck Moore", roles: [designer, developer], evidence: [colorforth-site], assertion_status: documented }
countries_of_origin: [US]
development_contexts:
  - { value: personal-minimal-computing-system, primary: true, evidence: [colorforth-site], assertion_status: documented }
design_purposes:
  - { value: minimal-standalone-programming-environment, primary: true, evidence: [colorforth-site], assertion_status: documented }
  - { value: vlsi-design-tool-host, primary: true, evidence: [colorforth-site], assertion_status: documented }
target_audiences:
  - { value: "Forth programmers and VLSI designers", evidence: [colorforth-site], assertion_status: provisional }
development_status: { value: inactive-original-with-web-archive, evidence: [colorforth-repo], assertion_status: documented }
programming_languages:
  - { value: "colorForth", roles: [implementation, primary-application-language], evidence: [colorforth-site], assertion_status: documented }
system_organization:
  - { value: integrated-language-operating-environment, evidence: [colorforth-site], assertion_status: documented }
gui_status:
  - { value: graphical-color-coded-integrated-environment, evidence: [colorforth-site], assertion_status: documented }
interfaces:
  - { name: "colorForth editor and interpreter", style: graphical-semantic-text, modalities: [keyboard, display], evidence: [colorforth-site], assertion_status: documented }
hardware_platforms:
  - { value: "Pentium-class IBM PC compatibles", evidence: [colorforth-site], assertion_status: documented }
machine_classes: [personal-computer]
source_preservation: { value: official-site-and-download-archive, evidence: [colorforth-repo], assertion_status: documented }
repositories:
  - { resource: "https://github.com/colorforth/colorforth.github.io", relationship: official-site-mirror, evidence: [colorforth-repo], assertion_status: documented }
sources:
  - { id: colorforth-site, resource: "https://colorforth.github.io/cf.htm", title: "colorForth", author: "Chuck Moore", source_kind: preserved-official-site }
  - { id: colorforth-repo, resource: "https://github.com/colorforth/colorforth.github.io", title: "colorforth.com website mirror", source_kind: preservation-repository }
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-29'
  disposition: has-associations
  note: One or more relationships are documented by curated primary or institutional
    sources.
text_editors:
- name: colorForth editor
  relationship: integral
  interface_style: graphical-semantic-text
  source: https://colorforth.github.io/cf.htm
  source_kind: preserved-official-site
  assertion_status: documented
# END GENERATED TEXT EDITORS
---

# Identity boundary

colorForth is both a programming language and a standalone operating
environment. The official preserved site says it can boot without another
operating system and includes multitasking, essential drivers, an editor, and
compiler, so it is cataloged as an integrated system rather than merely a
hosted language.
