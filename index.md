---
okf_version: "0.2"
---

# Historical Operating Systems Catalog

An Open Knowledge Format bundle for documenting historical operating systems,
their releases, surviving artifacts, creators, and hardware contexts.

Browse the generated [operating-system and text-editor table](https://htayj.github.io/os-directory/)
for full-text search, faceted filtering, multi-column sorting, column controls,
pagination, and CSV export.

The frozen English Wikipedia baseline is fully dispositioned: 754 normalized
candidates from 901 list occurrences. A separate native-language discovery
release covers ten non-English language traditions plus the Russian/Elbrus
ecosystem pass. The bundle contains 581 system-lineage records: the original
530-system English, multilingual, Elbrus, and TI Explorer release; five
Lisp-machine-coverage additions; DTSS and Small ITS; and 40 systems discovered
through the recursive Computer History Wiki category audit; plus PDP-6
Timesharing System 1.4, BBN Exec III, TI System V/68, and colorForth found
through a complete audit of Lars Brinkhoff's publicly visible GitHub
organization memberships. Releases, aliases, groupings, non-OS items, and
unresolved identities remain explicit inventory results rather than being
forced into system records.

# Catalog

* [Operating systems](systems/) - System lineages, releases, variants, and surviving artifacts.
* [Discovery inventories](inventory/) - Frozen English, multilingual, preservation, Lisp-machine, and Gunkies coverage ledgers.
* [Graphical environments](environments/) - Desktop environments, operating environments, window systems, and interface shells.
* [Organizations](organizations/) - Companies, universities, research groups, and other responsible bodies.
* [Hardware platforms](hardware/) - Machines and architectures on which cataloged systems ran.
* [Sources](sources/) - Bibliographic and archival sources described as first-class concepts.

# Catalog Method

* [Catalog plan](schema/catalog-plan.md) - Coverage, fields, evidence standards, and phased execution plan.
* [Multilingual discovery](schema/multilingual-discovery.md) - How systems absent from the English list are found and reviewed.
* [Field vocabulary](schema/field-vocabulary.md) - Normalized attributes and their meanings.
* [Scope and identity](schema/scope-and-identity.md) - Rules for deciding what receives a distinct record.
* [Operating-system record](schema/operating-system-record.md) - Domain fields and expected sections for system concepts.
* [Text-editor associations](schema/text-editor-associations.md) - Evidence rules for bundled, native, ported, and historically prominent editors.
* [Terra deep-research guide](schema/deep-research-agent-guide.md) - Bounded manifests, primary-source strategy, structured results, validation, and merge boundaries.
* [Graphical-environment record](schema/interface-environment-record.md) - Identity and architecture rules for desktop and operating environments.
* [Contribution workflow](schema/contribution-workflow.md) - How to add sourced records and represent uncertainty.

# Project

* [Templates](templates/) - Copyable starters for new catalog records.
* [Update log](log.md) - Chronological changes to this bundle.
