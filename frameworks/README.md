# Frameworks

**What belongs here:** multi-criteria reasoning systems — a Framework doesn't produce a single yes/no, it produces a classification or ranking (an Evidence Tier, a six-dimension EV score, a verification path). Frameworks are what a Playbook invokes at each phase; a Framework is what a Rule is derived from when the reasoning needs to collapse to a hard constraint.

**Why this category exists (separate from Rules and Playbooks):** an agent retrieving "how do I classify this evidence" needs the *reasoning model* (tiers + resolved edge cases), not a step-by-step procedure (that's a Playbook) and not a single hard constraint (that's a Rule, though a Framework may spawn one — e.g. FRAMEWORK-001's tier table is referenced by RULE-002's visual tier mapping).

**Current objects:** [FRAMEWORK-001](FRAMEWORK-001-evidence-tier-framework.md) (evidence tiers — canonical), [FRAMEWORK-002](FRAMEWORK-002-onchain-verification.md) (on-chain verification), [FRAMEWORK-003](FRAMEWORK-003-decision-framework.md) (story ranking / EV), [FRAMEWORK-004](FRAMEWORK-004-writing-and-mechanism.md) (writing discipline).

**Schema:** [`/_schemas/framework.schema.yaml`](../_schemas/framework.schema.yaml).
