# Sources

**What belongs here:** the Source Reliability Database — one object per named, evidence-originating entity, tracking its calibration over time. This is the file-based counterpart to the `type:source` GitHub Issue Form: an issue is opened and discussed live; once a track record stabilizes, it graduates into a Source object here for permanent, indexable retrieval.

**Why this category exists separate from Tools:** see `/tools/README.md`. In short — Tool is "how to query it," Source is "should I trust what it said, based on history." A source's `default_tier` here is a *starting point*, never an override — [Evidence Tier Framework](../frameworks/FRAMEWORK-001-evidence-tier-framework.md) is explicit that a good track record never upgrades a specific claim's tier.

**Naming & sharding:** `SOURCE-######` (6-digit ID, room for 10,000+), sharded into subfolders per 1,000-ID range (`sources/000001/` covers 000001–000999, etc.) from day one, since this is the largest-volume object type at target scale.

**Current objects (seed set):** [SOURCE-000001](000001/SOURCE-000001-arkham-intelligence.md).

**Schema:** [`/_schemas/source.schema.yaml`](../_schemas/source.schema.yaml).
