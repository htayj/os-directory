# Discovery Inventory

Generated and curated inventories used to establish catalog coverage.

# Baseline

* `english-list-occurrences.json` - every list item extracted from the frozen English Wikipedia revision.
* `english-list-source.json` - revision, retrieval, and content-fingerprint metadata.

# Supplemental

* `manual-seeds.yaml` - manually identified multilingual or ecosystem candidates awaiting identity resolution.

# Rebuilding

Run `python scripts/build_baseline_inventory.py` from the bundle root. Generated
files are deterministic for the frozen source revision.
