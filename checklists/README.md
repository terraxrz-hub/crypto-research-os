# Checklists

**What belongs here:** finite, enumerable, machine-checkable item lists used as a gate before some transition (e.g. before a status can become PASS). Unlike a Rule (one statement) or a Framework (a reasoning model), a Checklist is a *list of discrete items*, each independently answerable, with a stated pass/fail rule for the whole list.

**Why this category exists separate from Rules:** a Checklist's `items` field is structured data an Action or agent can enumerate and verify individually (see `enforced_by` on CHECKLIST-001) — a Rule's single `statement` field can't represent "10 independent yes/no items with a combined pass condition."

**Current objects:** [CHECKLIST-001](CHECKLIST-001-qa-gate.md) (QA Gate — the ten-question publication gate, enforced by a GitHub Action).

**Schema:** [`/_schemas/checklist.schema.yaml`](../_schemas/checklist.schema.yaml).
