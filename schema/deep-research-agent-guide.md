---
type: Playbook
title: Terra deep-research agent guide
description: Source, tooling, output, and merge rules for delegated operating-system research.
tags: [workflow, research, agents, provenance]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-27T00:00:00-04:00" }
---

# Purpose

Terra agents perform source-first deep dives on bounded, non-overlapping system
manifests. They produce reviewable research results; they do not directly edit
system records. The primary agent normalizes and merges accepted claims.

# Supplied Context

Each manifest contains:

* the system path, title, aliases, and discovery languages;
* the current completeness level and exact target fields;
* provisional first-pass attributes;
* already cataloged sources and editor associations;
* a priority score and batch theme.

Read the current `/systems/<slug>/system.md`, `/schema/field-vocabulary.md`,
`/schema/operating-system-record.md`, and
`/schema/text-editor-associations.md` before researching.

# Research Tools

Agents may use:

* web search and direct browsing for official documentation, institutional
  archives, scholarly papers, contemporary manuals, and native-language
  sources;
* `pdftotext -layout` and `pdfinfo` for born-digital manuals;
* `tesseract` for locally downloaded scans that lack a text layer;
* `curl` for HTTP metadata or official JSON APIs;
* `rg` and `jq` for repository and structured-data inspection.

Download working copies only under a temporary directory. Do not commit
copyrighted manuals, disk images, binaries, or page captures. Record their
stable public catalog or document URL instead.

# Source Strategy

Search in this order:

1. contemporary system manuals, release notes, source trees, distribution
   manifests, licenses, and vendor or project documentation;
2. institutional archives, standards records, museum catalogs, and papers by
   the system's designers;
3. later scholarly histories and preservation projects;
4. high-quality secondary references;
5. Wikipedia and Wikidata for discovery only.

For non-English systems, search the native name, historical romanizations,
developer name, product family, and native terms for manual, operating system,
release, kernel, license, editor, and history. Cite the original-language
source, identify its language, and provide an English paraphrase. Machine
translation does not raise a source's authority.

Search surviving documentation separately from current vendor pages. Prefer a
document-specific URL and page or section locator over a search-result or
landing-page URL. Use archived URLs when the live source is fragile.

# Claim Rules

* Country of origin means the location of original development, not a later
  owner's present headquarters.
* Preserve historical terms such as monitor, executive, supervisor, or control
  program. Do not force them into a modern kernel category.
* “No license found” is not evidence of a proprietary license.
* Separate first release, last release, last source change, support end, and
  later archival activity.
* Do not infer a programming language from an API, application language, or
  supported toolchain.
* Do not infer a GUI from a third-party window system or a CLI from the mere
  existence of a console.
* An editor must have a concrete bundled, integral, first-party, native,
  ported, historically prominent, supported-platform, or development-host
  relationship. Family compatibility alone is insufficient.
* Multiple conflicting claims may coexist. Mark them `disputed` and explain
  the conflict.
* Use `inferred` only when the inference and its premises are explicit.
* Keep excerpts short. Prefer a precise paraphrase plus page, section, command,
  file, tag, or revision locator.

# Output Contract

Write only the assigned
`/inventory/deep-research/results/<batch-id>.json`. The result has one entry
per manifest system:

```json
{
  "batch_id": "wave-001-batch-001",
  "researcher": "agent name",
  "researched_at": "2026-07-27",
  "results": [
    {
      "path": "systems/example",
      "title": "Example",
      "identity_status": "confirmed",
      "research_summary": "Short English synthesis.",
      "sources": [
        {
          "id": "example-manual",
          "title": "Example System Manual",
          "url": "https://example.org/manual.pdf",
          "archived_url": null,
          "source_kind": "contemporary-system-manual",
          "language": "en",
          "date": "1984",
          "primary": true,
          "notes": "Scope and edition."
        }
      ],
      "claims": [
        {
          "field": "programming_languages",
          "value": {"language": "Example", "extent": "primary"},
          "source_ids": ["example-manual"],
          "assertion_status": "documented",
          "source_term": "implementation language",
          "scope": {},
          "locator": "page 12",
          "evidence_note": "English paraphrase of what the source establishes."
        }
      ],
      "editor_associations": [],
      "unresolved": [
        {
          "field": "licenses",
          "disposition": "no-evidence-found",
          "reason": "What was checked and why it remains unresolved.",
          "source_ids": ["example-manual"]
        }
      ]
    }
  ]
}
```

Allowed `identity_status` values are `confirmed`, `corrected`, `ambiguous`, and
`not-a-system`. Never silently research a similarly named but different
system. All source IDs must resolve within the same result entry.

# Merge Boundary

Agents are not alone in the repository. They must not edit, reformat, or revert
`system.md`, site files, schemas, scripts, or another agent's result file.
Only the primary agent merges reviewed claims, assigns catalog source IDs, and
updates dispositions.

After review, `scripts/attach_deep_research_results.py` embeds the complete
validated result as a self-contained `deep_research` snapshot in the system
record. This preserves exact source IDs, claim locators, rejected
generalizations, and unresolved dispositions while field-by-field normalized
promotion proceeds.
