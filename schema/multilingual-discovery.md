---
type: Catalog Plan
title: Multilingual and ecosystem discovery
description: A reproducible deep-pass method for finding operating systems absent from the English Wikipedia list.
tags: [plan, discovery, multilingual, coverage]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
sources:
  - id: elbrus-en
    resource: https://en.wikipedia.org/wiki/Elbrus_(computer)
    title: Elbrus (computer)
    language: en
    author: community:wikipedia-editors
    accessed: 2026-07-26
  - id: elbrus-ru
    resource: https://ru.wikipedia.org/wiki/Эльбрус_(семейство_компьютеров)
    original_title: Эльбрус (семейство компьютеров)
    translated_title: Elbrus (computer family)
    language: ru
    author: community:wikipedia-editors
    accessed: 2026-07-26
  - id: mcst-elbrus-os
    resource: https://www.mcst.ru/elbrus_os
    original_title: Операционные системы «Эльбрус»
    translated_title: Elbrus operating systems
    language: ru
    author: organization:mcst
    accessed: 2026-07-26
---

# Purpose

The English Wikipedia list is broad but structurally unable to represent every
historical, regional, institutional, military, educational, embedded, or
short-lived operating system. This plan discovers additional systems without
pretending that any single language edition or knowledge graph is complete.

The Elbrus ecosystem demonstrates the problem: the English hardware article
primarily describes computers and processors,[^elbrus-en] while the Russian
article describes the original operating-system environment and later
МСВС-Э,[^elbrus-ru] and current MCST material separately documents modern
operating systems called ОС «Эльбрус».[^mcst-elbrus-os] These are discovery
leads requiring identity resolution, not one timeless “Elbrus OS” record.

# Coverage Sets

Keep two independently measurable sets:

1. **English-list baseline** - the fixed revision named in the main
   [catalog plan](/schema/catalog-plan.md).
2. **Supplemental discovery** - candidates found by the versioned passes below,
   frozen by query/source revision and observation date.

A system may belong to both sets. Its record retains every discovery path.

# Discovery Passes

## 1. Wikidata and Cross-Language Sitelinks

Query items classified as operating systems or relevant subclasses and collect
all language sitelinks, labels, aliases, inception dates, developers, and
platform relations as discovery metadata. Do not treat a Wikidata statement as
verified historical evidence.

Compare the resulting identities against the baseline by QID, redirects,
native names, aliases, lineage, and manual review. QID equality is strong
identity evidence; label similarity alone is not.

## 2. Multilingual Lists and Categories

Parse operating-system lists, categories, and historical-computing indexes in
every Wikipedia edition exposed by the candidate graph. Prioritize manual deep
review where the pass finds candidates absent from English.

Maintain a versioned language lexicon for terms equivalent or historically
related to:

* operating system;
* executive, monitor, supervisor, control program, and dispatcher;
* disk, network, real-time, embedded, teaching, and research operating system;
* system software, system programming environment, and resident system.

Language keywords generate candidates; they do not establish concept type.

## 3. Hardware-Ecosystem Pages

Inspect computer-family, processor, workstation, mainframe, minicomputer,
console, mobile-device, controller, and appliance pages for:

* bundled or required system software;
* “software,” “operating system,” “monitor,” or “programming system” sections;
* model-specific releases and ports;
* compatibility modes and hosted environments; and
* manuals or external links naming otherwise undocumented systems.

Never create an OS concept merely because a hardware family and software share
a name.

## 4. National and Institutional Histories

Search computer museums, academy and university archives, manufacturer
histories, government technical libraries, finding aids, and national
encyclopedias. Give special attention to computing traditions whose primary
documentation was not published in English.

Record the institution, country, language, source kind, access date, and any
archived copy. Prefer contemporary manuals and source artifacts over later
summaries.

## 5. Bibliographic and Full-Text Snowballing

Follow system names, predecessor/successor claims, citations, bibliographies,
manual series, conference proceedings, source-tree references, and preserved
media labels. Search native names and historically appropriate terms, not only
modern translations of “operating system.”

## 6. Family and Lineage Gap Audit

For every cataloged system, review named predecessors, successors, forks,
ports, bundled variants, and companion systems. Record absent relations as
candidates and distinguish a release from an independently named lineage.

# Candidate Record

Before inclusion, each candidate records:

```yaml
method:
language:
native_label:
source:
source_revision:
observed_at:
context:
proposed_identity:
disposition: needs-review
related_candidates: []
notes:
```

Allowed dispositions are defined in
[field vocabulary](/schema/field-vocabulary.md). Exclusions remain in the
inventory so later passes do not repeatedly rediscover and reconsider them.

# Identity and Translation Rules

* Preserve native names exactly, including script and diacritics.
* Record language with BCP 47 and script with ISO 15924 codes.
* Store transliteration separately from translation and identify the scheme.
* Do not translate brand names or acronyms unless a source does so.
* Treat translated pages as sources distinct from their originals.
* Keep an original quotation only when needed to resolve identity or technical
  terminology; otherwise summarize to minimize copied text.
* Mark machine-assisted translations and retain the original-language source.
* Escalate ambiguous executive/monitor terminology for review rather than
  forcing a modern kernel or OS classification.

# Deep-Pass Completion

The supplemental pass is complete for a catalog release when:

* every scheduled discovery query and source snapshot is recorded;
* every candidate has a disposition;
* native names and discovery languages are retained;
* included systems have the same core-field requirements as baseline systems;
* exclusions distinguish duplicates, releases, artifacts, non-OS software, and
  insufficient evidence;
* results are summarized by language and discovery method; and
* newly discovered lineage edges have been recursively audited.

This is a repeatable release criterion, not a claim that no unknown operating
system exists.

[^elbrus-en]: The English article establishes the Elbrus hardware family and links several language editions but provides little operating-system identity detail.
[^elbrus-ru]: The Russian article names the original OS/software environment and a later Linux-based system shipped with Elbrus-3M1.
[^mcst-elbrus-os]: MCST's current product material distinguishes modern Elbrus operating-system products and versions.
