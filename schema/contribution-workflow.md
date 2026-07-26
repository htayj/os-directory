---
type: Playbook
title: Contribution workflow
description: A source-first workflow for adding and reviewing historical operating-system records.
tags: [workflow, provenance, review]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
---

# Before Writing

1. Decide whether the subject is a system, release, artifact, organization,
   hardware platform, or historical source using
   [scope and identity](/schema/scope-and-identity.md).
2. Prefer contemporary primary evidence. Use later scholarship for synthesis,
   correction, and context.
3. Check for an existing concept or alias before creating a new identity.

# Authoring

1. Copy the closest file from `/templates/`.
2. Choose a stable lower-case hyphenated path.
3. Add each consulted work to `sources` with a stable `id` and concrete
   `resource`.
4. Attach source-specific claims to footnotes whose labels match those IDs.
5. Distinguish documented facts, synthesis, and inference in the prose.
6. Link related concepts with ordinary Markdown links.
7. Add the record to the nearest `index.md`.
8. Add a dated entry to `/log.md`.

# Review

Check that:

* names and dates retain the precision of their sources;
* system, release, and artifact identities have not been conflated;
* quoted or redistributed material has an appropriate rights basis;
* download claims identify the exact artifact rather than a landing page;
* conflicting sources remain visible;
* `verified` reflects an actual source check; and
* the bundle validator passes.

# Validation

From the bundle root, run:

```sh
python scripts/validate_okf.py
```

The validator checks structural OKF v0.2 conformance and local Markdown links.
It does not establish historical accuracy, source credibility, or legal status.
