---
id: MIGRATION
type: meta
title: "Migration: flat docs/ → typed knowledge objects"
status: active
version: 1
tags: [migration, architecture]
related: [ARCHITECTURE]
summary: >
  Complete, no-backward-compatibility mapping from the prior flat docs/
  and prompts/ structure to the typed knowledge-object layout, and why
  each file became the type it did.
source_of_truth: true
---

# Migration: flat `docs/` → typed knowledge objects

This repository previously kept its rules as 11 numbered pages in a flat `docs/` folder plus one `prompts/prompt-library.md`. That structure was optimized for a human reading top-to-bottom. This migration re-optimizes for AI retrieval — see [ARCHITECTURE.md](ARCHITECTURE.md) for the full reasoning. **No redirects, aliases, or symlinks were kept** for the old paths; every internal reference (workflows, issue templates, README, CONTRIBUTING, SETUP, CHANGELOG) was rewritten in the same pass.

## Path mapping

| Old path | New path | New type | Why this type |
|---|---|---|---|
| `docs/00-objective.md` | `/OBJECTIVE.md` | `meta` | The single static "why" page everything else operationalizes — not itself a Rule, Framework, or Playbook, so it stays a root-level meta object rather than being forced into the object taxonomy. |
| `docs/01-sources-and-priority.md` | `/rules/RULE-001-source-priority-order.md` | `rule` | A fixed search-order constraint with three hard sub-rules (source-count, attribution, direction) — checkable, not a reasoning model. |
| `docs/02-evidence-framework.md` | `/frameworks/FRAMEWORK-001-evidence-tier-framework.md` | `framework` | A seven-tier classification model with resolved edge cases — judgment, not a single yes/no. |
| `docs/03-writing-and-mechanism.md` | `/frameworks/FRAMEWORK-004-writing-and-mechanism.md` | `framework` | A governing principle plus four derived diagnostics — a reasoning model for judging a draft, not one checkable fact. |
| `docs/04-visual-assets.md` | `/rules/RULE-002-visual-asset-priority.md` | `rule` | A fixed four-tier list directly derived from FRAMEWORK-001, plus checkable retrieve/never-fabricate constraints. |
| `docs/05-on-chain-verification.md` | `/frameworks/FRAMEWORK-002-onchain-verification.md` | `framework` | Verification-priority reasoning plus a six-check protocol — a model for classifying evidence, not an atomic constraint. |
| `docs/06-decision-framework.md` | `/frameworks/FRAMEWORK-003-decision-framework.md` | `framework` | Six weighted criteria producing a ranking — the canonical example of a reasoning model. |
| `docs/07-publication-standard.md` | `/rules/RULE-003-publication-standard.md` | `rule` | The Weakest-Link Rule is a single, checkable constraint on how a status gets assigned, even though it references a Framework's tiers as input. |
| `docs/08-qa-gate.md` | `/checklists/CHECKLIST-001-qa-gate.md` | `checklist` | Ten enumerable, independently-answerable items with a combined pass condition — the defining shape of a Checklist. |
| `docs/09-research-workflow.md` | `/playbooks/PLAYBOOK-0001-research-workflow.md` | `playbook` | An ordered procedure (fresh scan → selection → verification → time-pressure handling), not a reasoning model or a single rule. |
| `docs/10-daily-workflow.md` | `/playbooks/PLAYBOOK-0002-daily-workflow.md` | `playbook` | The six numbered phases are the clearest possible Playbook shape in the prior structure. |
| `docs/glossary.md` | `/GLOSSARY.md` | `reference` | Term definitions aren't rules, frameworks, or procedures — kept as a root-level reference object every other object links to on first use. |
| `prompts/prompt-library.md` | `/prompts/PROMPT-0001` … `PROMPT-0007` (+ `/prompts/README.md`) | `prompt` (×7) | Each of the seven prompts already invoked exactly one Playbook phase; splitting them into individual objects means retrieving "the prompt for Phase 3" doesn't require pulling in the other six. |

## What did *not* migrate 1:1

- **New objects created that had no prior equivalent:** four seed `Tool` objects, one seed `Source` object, one seed `Example` object — added specifically to establish the pattern, ID scheme, and sharding convention described in `ARCHITECTURE.md` §7, ahead of real volume arriving.
- **`_schemas/`** — new; the prior structure had no machine-readable contract for what a "page" was allowed to contain.
- **`MANIFEST.jsonl`** — new; the prior structure had no bootstrap index, since 12 files needed no index to browse.

## What stayed exactly the same

The actual rules, tier tables, criteria, and QA questions are **unchanged in substance** — this was a re-typing and re-referencing migration, not a content revision. Every fact, table, and threshold from the prior `docs/` pages exists verbatim in its new home; only the frontmatter, file location, and cross-reference syntax changed.
