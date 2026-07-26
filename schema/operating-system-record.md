---
type: Catalog Schema
title: Operating-system record
description: Defines the producer fields and body sections used for operating-system concepts.
tags: [schema, operating-system, cataloging]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
---

# Required OKF Field

Every concept has a non-empty `type`. System records use
`type: Operating System`; related records use the types defined in
[scope and identity](/schema/scope-and-identity.md).

# Recommended OKF Fields

Use `title`, `description`, `tags`, `status`, `generated`, and `sources` as
defined by OKF v0.2. Use `resource` only when there is one canonical URI for the
underlying subject, not merely a useful web page about it.

Add `verified` only after a human or deterministic process checks the content
against the cited evidence. Keep per-claim attribution as Markdown footnotes
whose labels match `sources[].id`.

# Catalog Extension Fields

Use the normalized producer-defined fields in
[field vocabulary](/schema/field-vocabulary.md). Unknown values must not be
guessed. During systematic coverage work, record applicable gaps in
`field_dispositions` so `not-researched`, `no-evidence-found`, `unknown`,
`disputed`, and `not-applicable` remain distinguishable.

# Expected Body Sections

Use only sections for which evidence exists:

* **Overview** - identity, purpose, period, and historical context.
* **Purpose and Design Goals** - why the system was created, for whom, and the stated constraints or ambitions.
* **History and Releases** - dated development and release narrative.
* **Licensing and Availability** - source, binary, documentation, and time-scoped license facts.
* **Implementation and Kernel** - languages, kernel name and type, userland, process, memory, storage, networking, and security model.
* **Interfaces** - command, graphical, batch, programming, and administrative interfaces.
* **Platforms** - supported hardware families, architectures, devices, and virtual targets.
* **System Facilities** - scheduling, user model, memory, storage, networking, IPC, security, drivers, packaging, virtualization, and reliability.
* **Lineage and Compatibility** - predecessors, descendants, ports, forks, influence, and compatibility.
* **Preservation** - surviving source, binaries, media, documentation, emulation, and access constraints.
* **Open Questions** - unresolved or conflicting claims.

# Paths

Use this layout for an operating-system family:

```text
systems/<system-slug>/
  index.md
  system.md
  releases/
    index.md
    <release-slug>.md
  artifacts/
    index.md
    <artifact-slug>.md
```

Use lower-case ASCII slugs with hyphens. Links in prose should normally be
bundle-relative paths beginning with `/`.
