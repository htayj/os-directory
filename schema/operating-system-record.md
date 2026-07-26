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

These producer-defined fields are optional. Unknown values should be omitted,
not guessed.

| Field | Shape | Meaning |
|---|---|---|
| `names` | list of strings | Contemporary names, abbreviations, and documented aliases. |
| `developers` | list of paths or URIs | Responsible organizations or groups. |
| `introduced` | date or string | Earliest documented introduction; qualify uncertainty in the body. |
| `discontinued` | date or string | End of development or availability; qualify uncertainty in the body. |
| `lineage` | list of mappings | Relationships such as `predecessor`, `successor`, `fork`, `derived-from`, or `influenced-by`, each with a `target`. |
| `platforms` | list of paths or URIs | Supported hardware-platform concepts. |
| `interfaces` | list of strings | Documented operator or programming interfaces. |
| `languages` | list of strings | Implementation languages supported by evidence. |
| `availability` | string | A concise access or preservation summary, not a legal conclusion. |

# Expected Body Sections

Use only sections for which evidence exists:

* **Overview** - identity, purpose, period, and historical context.
* **History** - dated development and release narrative.
* **Architecture** - kernel, process, memory, storage, networking, and security model.
* **Interfaces** - command, graphical, batch, programming, and administrative interfaces.
* **Hardware** - supported or required platforms.
* **Lineage and Influence** - predecessors, descendants, ports, forks, and documented influence.
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
