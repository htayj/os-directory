---
type: Catalog Plan
title: Text-editor association pass
description: Evidence and normalization rules for relating text editors to operating systems.
tags: [plan, text-editor, relationships]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T00:00:00-04:00" }
---

# Purpose

This pass records text editors historically or technically associated with
each cataloged operating-system lineage. It does not treat every cross-platform
editor as associated with every system it could theoretically run on.

# Required Result

Every system record must contain one of:

1. one or more sourced `text_editors` relationships; or
2. an empty `text_editors` list plus a dated `field_dispositions` entry saying
   `not-researched` or `no-evidence-found`.

# Evidence Priority

Use contemporary system manuals, release notes, distribution manifests,
editor manuals, source trees, and vendor documentation first. Preservation
archives and scholarly histories are next. Wikipedia and Wikidata may supply
provisional discovery relationships, but those remain provisional until
checked against stronger evidence.

# Identity Rules

* Preserve the editor's actual product name and distinguish renamed releases.
* Do not collapse a command, editor family, emulation mode, and derivative
  implementation into one identity.
* Distinguish line editors, screen editors, structural editors, word
  processors, IDEs, and general development environments.
* Include an IDE only when it supplies a genuine plain-text or source editor;
  record that relationship in a note.
* Exclude file viewers, pagers, binary-only patchers, document formatters, and
  word processors without a plain-text editing mode.

# Scope and Uncertainty

Editor availability often changes by system release, installation profile,
hardware platform, or optional product. Scope those claims rather than
projecting one release's bundle across the entire lineage. Multiple
contradictory sources may coexist with distinct assertion statuses.
