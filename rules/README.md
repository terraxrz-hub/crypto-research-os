# Rules

**What belongs here:** atomic, non-negotiable constraints — a single canonical statement that's either satisfied or not. Each Rule has one `statement` field expressing it in one sentence.

**Why this category exists (separate from Frameworks):** a Rule is a boolean constraint an agent or Action can check directly ("was the visual retrieved, not just recommended?"); a Framework is a multi-criteria reasoning system that produces a judgment, not a yes/no. Keeping them separate means an AI retriever can ask "give me every hard constraint on this task" (filter `type:rule`) without also pulling in the reasoning models needed to apply judgment.

**Current objects:** [RULE-001](RULE-001-source-priority-order.md) (source search order), [RULE-002](RULE-002-visual-asset-priority.md) (visual tiers), [RULE-003](RULE-003-publication-standard.md) (weakest-link publication logic).

**Schema:** [`/_schemas/rule.schema.yaml`](../_schemas/rule.schema.yaml).
