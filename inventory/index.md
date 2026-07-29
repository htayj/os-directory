# Discovery Inventory

Generated and curated inventories used to establish catalog coverage.

# Baseline

* `english-list-occurrences.json` - every list item extracted from the frozen English Wikipedia revision.
* `english-list-source.json` - revision, retrieval, and content-fingerprint metadata.
* `baseline-candidates.json` - optional redirect-resolved candidates produced by the online enrichment script.
* `baseline-occurrence-map.json` - optional occurrence mapping produced with those online candidates.
* `enwiki-os-page-metadata.json` - optional discovery metadata produced by the same API-dependent pass.
* `terra-candidates.json` - deterministic raw candidates assigned to Terra first-pass review.
* `terra-batches.json` - completed batch ledger for Terra first-pass review.
* `terra-manifests/` - non-overlapping worker manifests of at most ten candidates.
* `terra-results/` - one reviewed disposition for every candidate.
* `enwiki-infobox-snapshots.json` - cached provisional attribute snapshots used by system records.
* `wikidata-country-origins.json` - direct or explicitly inferred country evidence.
* `interface-environment-candidates.json` - unique raw GUI/interface terms and their host systems, awaiting entity-type review.
* `text-editor-associations.json` - editor relationships or an explicit no-evidence disposition for every system.
* `text-editor-page-snapshots.json` - frozen linked-page revision metadata and provisional editor discoveries.
* `text-editor-wikidata.json` - frozen direct text-editor platform statements used for provisional discovery.
* `deep-research/` - ranked gap audit, non-overlapping Terra manifests, and
  structured source-first research results awaiting normalized merge.
* [Lisp-machine operating-system coverage](lisp-machine-os-coverage.md) -
  machine-to-system mappings and explicit non-OS or unresolved dispositions for
  every family named by the Computer History Wiki LISP-machine page.
* [Lars Brinkhoff preservation-source audit](preservation/larsbrinkhoff.md) -
  system mappings for 27 selected preservation projects after screening all
  208 public profile repositories, with ownership, fork, and verified external
  contribution boundaries.
* [Computer History Wiki operating-system coverage](gunkies/coverage.md) -
  complete dispositions for 330 pages across all 35 recursively discovered
  categories, including 40 newly cataloged historical systems.

# Supplemental

* `manual-seeds.yaml` - manually identified multilingual or ecosystem candidates awaiting identity resolution.
* `multilingual/` - frozen native-language candidate corpora, normalized
  dispositions, 12 Terra first-pass manifests and results, and provisional
  Wikidata and multilingual Wikipedia-infobox attribute snapshots. The current
  release covers Arabic, Chinese, Czech/Slovak, French, German, Italian,
  Japanese, Korean, Portuguese, and Spanish sources, in addition to the
  Russian/Elbrus ecosystem seed.

# Rebuilding

Run `python scripts/build_baseline_inventory.py` followed by
`python scripts/build_terra_manifests.py` from the bundle root. The optional
`build_baseline_candidates.py` adds redirect and Wikidata enrichment when the
public APIs permit it. Generated occurrences and Terra manifests are
deterministic for the frozen source revision; linked-page metadata reflects the
retrieval date.

Run `python scripts/catalog_text_editors.py` to refresh editor discovery and
write the normalized relationships into every system record. Then run
`python scripts/validate_text_editor_coverage.py` to confirm complete inventory
and record-level coverage.
