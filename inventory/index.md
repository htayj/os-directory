# Discovery Inventory

Generated and curated inventories used to establish catalog coverage.

# Baseline

* `english-list-occurrences.json` - every list item extracted from the frozen English Wikipedia revision.
* `english-list-source.json` - revision, retrieval, and content-fingerprint metadata.
* `baseline-candidates.json` - redirect-resolved and deduplicated system/release candidates.
* `baseline-occurrence-map.json` - disposition of every baseline occurrence.
* `enwiki-os-page-metadata.json` - cached discovery metadata for linked OS articles.
* `terra-candidates.json` - deterministic raw candidates assigned to Terra first-pass review.
* `terra-batches.json` - batch ledger for Terra first-pass review.
* `terra-manifests/` - non-overlapping worker manifests of at most ten candidates.

# Supplemental

* `manual-seeds.yaml` - manually identified multilingual or ecosystem candidates awaiting identity resolution.

# Rebuilding

Run `python scripts/build_baseline_inventory.py` followed by
`python scripts/build_terra_manifests.py` from the bundle root. The optional
`build_baseline_candidates.py` adds redirect and Wikidata enrichment when the
public APIs permit it. Generated occurrences and Terra manifests are
deterministic for the frozen source revision; linked-page metadata reflects the
retrieval date.
