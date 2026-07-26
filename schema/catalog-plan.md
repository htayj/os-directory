---
type: Catalog Plan
title: Wikipedia operating-systems catalog plan
description: Defines how every distinct operating system in the source list will be inventoried, normalized, researched, and verified.
tags: [plan, coverage, wikipedia, operating-system]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
sources:
  - id: wikipedia-list
    resource: https://en.wikipedia.org/w/index.php?title=List_of_operating_systems&oldid=1365063001
    title: List of operating systems, revision 1365063001
    author: community:wikipedia-editors
    last_modified: 2026-07-20
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format specification, version 0.2
    author: organization:google-cloud-platform
---

# Objective

Create one OKF concept for every distinct operating-system identity listed in
the source snapshot, while retaining every list occurrence and its section
context.[^wikipedia-list] Add a supplemental corpus of systems discovered
through multilingual and hardware-ecosystem research. Enrich each concept with
comparable structured fields and claim-level provenance.

The target snapshot is Wikipedia revision `1365063001`, dated
`2026-07-20T02:00:31Z`. Fixing a revision makes "each operating system listed"
reproducible even if the live page changes.

The English list is a baseline coverage set, not the universe of operating
systems. Supplemental discoveries are governed by
[multilingual discovery](/schema/multilingual-discovery.md) and retain their
own discovery provenance.

# Scope Decisions

The source page mixes system families, product lineages, releases, variants,
ports, distributions, projects, and unnamed systems. Apply
[scope and identity](/schema/scope-and-identity.md) to each item.

* Deduplicate repeated appearances of the same system while preserving all
  source-list occurrences in its record.
* Keep independently named derivatives and forks distinct when contemporary
  sources support a separate identity.
* Represent a version as an **Operating System Release** when it is only a
  release of an already cataloged system.
* Represent an unnamed but identifiable system with a stable descriptive slug;
  do not silently discard it.
* Flag ambiguous labels, lists of systems hidden in one bullet, and items that
  appear not to be operating systems for review.
* Catalog current systems because the requested list includes them, even though
  the bundle's primary interest is historical.
* Do not require an English Wikipedia article or appearance in the English list
  for inclusion.
* Treat hardware-family pages as discovery sources, not proof that the hardware
  name is itself an operating system.
* Preserve native names, scripts, transliterations, and source-language
  terminology.

# Core Information

Every system record must either supply or explicitly mark as not yet known:

1. Canonical name, aliases, and source-list spelling.
2. Creator, developer, maintainer, vendor, sponsor, responsible organization,
   and country or countries of origin, all time-scoped when they changed.
3. Original development context, purpose, design goals, intended users,
   application domain, deployment role, actual later uses, and system traits.
4. Development, support, and distribution status plus announcement,
   first-release, latest-release-per-stream, discontinuation, end-of-support,
   and last-confirmed-update events when applicable.
5. Rights regime, software-freedom status, and exact licenses, separated by
   source, binaries, documentation, component, and time period when they differ.
6. Primary and additional implementation languages, with component and release
   scope when known.
7. Overall system organization plus kernel/executive/monitor name, type,
   structure, placement, lineage, and changes across releases.
8. Interface style, modality, provisioning, access mode, GUI status, shells,
   window systems, and desktop environments.
9. Hardware families, device classes, and CPU instruction-set architectures.
10. Lineage: predecessors, successors, forks, bases, derivatives, and
    documented influence.
11. Distribution, present availability, source availability, and preservation
    state.
12. Evidence and uncertainty for each nontrivial claim.

The complete normalized vocabulary is in
[field vocabulary](/schema/field-vocabulary.md), version `0.1`. That vocabulary
is frozen before mass record generation; later breaking changes require a new
version and migration.

# Date Semantics

Dates that are often conflated are separate:

* an `announced` lifecycle event is a public announcement;
* `first_release` is the earliest documented release of the cataloged identity;
* `latest_releases` records the most recent published release in each relevant
  stream known at `as_of`;
* `last_updated` is the most recent confirmed material product or project
  event, its kind, and the observation method; it is not the edit date of a web
  page;
* `development-ended`, `distribution-ended`, and `support-ended` are distinct
  lifecycle events.

Each date separates granularity (`day`, `month`, `year`), qualifier (`exact`,
`circa`, `before`, `after`, `range`, `uncertain`), and assertion status
(`documented`, `inferred`, `disputed`, `provisional`, `unknown`). The record
retains source precision rather than manufacturing a full date.

# Evidence Policy

Use the Wikipedia list only for membership, spelling, list context, and links.
Research factual attributes from the strongest available sources in this order:

1. Contemporary manuals, release notes, source trees, media, and vendor or
   project documentation.
2. Archives, museum catalogs, finding aids, standards records, and scholarly
   histories.
3. High-quality secondary references.
4. Wikipedia and Wikidata as discovery aids or explicitly labeled provisional
   sources.

Every source-derived claim should have a footnote keyed to `sources[].id`.
Machine-harvested records remain `status: draft` and unverified. `verified`
means an actual source comparison, not successful parsing or schema validation.

# Completeness Levels

Coverage is measured separately from research depth:

* **Inventory complete**: every source-list occurrence maps to a concept, a
  release concept, or a documented review exception.
* **Core complete**: every core field, including origin and original purpose,
  has a sourced value or an explicit field disposition.
* **Deep complete**: applicable technical, preservation, and historical fields
  are researched beyond the core.
* **Human reviewed**: identity, origin, purpose, dates, license, language,
  kernel, interface, and platform claims have been checked against cited
  evidence.

Each concept records `catalog_completeness` and machine-readable
`field_dispositions`, distinguishing `not-researched`, `no-evidence-found`,
`unknown`, `disputed`, `not-applicable`, and `withheld`.

# Execution Phases

## 1. Freeze and Parse the Baseline Coverage Source

Save the source revision metadata and extract list occurrences with heading
path, displayed label, target page, annotations, nesting, and order. Preserve
duplicates at this stage.

## 2. Run Supplemental Discovery

Execute the versioned multilingual, Wikidata, hardware-ecosystem, archival, and
snowball passes in
[multilingual discovery](/schema/multilingual-discovery.md). Preserve every
candidate and its disposition, including false positives and ambiguous names.

## 3. Normalize Identities

Resolve redirects, aliases, nested releases, combined bullets, and duplicate
occurrences. Produce a review queue for ambiguous cases. Never merge solely on
similar names.

## 4. Create Draft Concepts

Generate a system directory and `system.md` for every normalized identity.
Record source-list provenance and completeness as `inventory`. Add release
concepts where a discovery source names a release rather than a distinct
lineage.

## 5. Enrich Core Fields

Research and populate core attributes. Prefer structured fields for comparison
and prose for qualifications, conflicts, and change over time.

## 6. Add Deep Technical and Preservation Data

Add architecture, scheduling, memory, storage, security, networking,
compatibility, distribution, surviving artifacts, emulation, and access/rights
information where applicable and supportable.

## 7. Validate and Review

Run structural OKF and local-link validation, source-inventory coverage checks,
versioned-schema and controlled-vocabulary checks, claim-envelope validation,
entity-reference checks, duplicate-ID checks, and core-completeness checks.
Report unresolved gaps without converting them into guessed values.

# Acceptance Criteria

The cataloging request is complete when:

* the frozen source inventory is committed;
* every baseline occurrence and supplemental candidate has a recorded
  disposition;
* every distinct system has a conformant OKF concept;
* all core fields, including origin, purpose, and intended users, have a sourced value or explicit disposition;
* native names and source languages are preserved;
* coverage metrics are reported by discovery method and language;
* no record claims human verification without review;
* the indexes expose every concept through progressive disclosure; and
* all validators pass.

[^wikipedia-list]: Wikipedia's list defines inclusion by notability and allows overlapping classifications; this plan preserves those classifications as source context rather than treating them as a taxonomy.
[^okf-spec]: OKF v0.2 requires frontmatter and a non-empty `type` for non-reserved Markdown concepts; its provenance, trust, lifecycle, and extension fields support this catalog design.
