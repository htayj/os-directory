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
