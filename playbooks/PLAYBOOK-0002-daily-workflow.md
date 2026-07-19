---
id: PLAYBOOK-0002
type: playbook
title: "Daily Workflow"
status: active
version: 1
tags: [workflow, daily, phases]
related: [PLAYBOOK-0001, FRAMEWORK-003, FRAMEWORK-001, FRAMEWORK-004, RULE-002, CHECKLIST-001]
phases: ["Phase 1 Market Scan & Story Selection", "Phase 2 Verification", "Phase 3 Explain the Mechanism", "Phase 4 Build the Draft", "Phase 5 Visual Assets", "Phase 6 QA Gate"]
depends_on: [FRAMEWORK-003, FRAMEWORK-001, FRAMEWORK-004, RULE-002, CHECKLIST-001]
produces: research
summary: >
  The six-phase day-to-day sequence, mirrored field-for-field by the
  research-entry GitHub Issue Form: market scan and ranking, verification,
  mechanism explanation, drafting, visual assets, and the QA Gate.
source_of_truth: true
---

# Daily Workflow

The day-to-day sequence. For the form you actually fill out while doing this, see the **`research-entry`** GitHub Issue template (Issues → New Issue → Research Entry) — it mirrors these phases as fields.

## Before starting

Begin with a completely fresh research cycle — see [Research Workflow](/playbooks/PLAYBOOK-0001-research-workflow.md#fresh-research-every-time). No reused scans, drafts, or market data.

## Phase 1 — Market Scan & Story Selection

Search the entire crypto market: market structure, regulation, security, on-chain activity, institutional adoption, infrastructure, stablecoins, macro events. Rank candidates using the **six criteria in [Decision Framework](/frameworks/FRAMEWORK-003-decision-framework.md#the-six-evaluation-criteria)** — Evidence Strength, Educational Value, Market Impact, Originality, Shelf Life, Mechanism Quality. Don't rank informally; use the actual six dimensions.

## Phase 2 — Verification

Follow [Sources & Research Priority](/rules/RULE-001-source-priority-order.md) and classify findings with [Evidence Framework](/frameworks/FRAMEWORK-001-evidence-tier-framework.md). Never confuse repeated reporting with independent evidence.

## Phase 3 — Explain the Mechanism

Before why it matters, explain how it happened. See [Writing & Mechanism](/frameworks/FRAMEWORK-004-writing-and-mechanism.md).

## Phase 4 — Build the Draft

Standalone tweet first; thread only if a genuine attempt to compress fails. See [Writing & Mechanism](/frameworks/FRAMEWORK-004-writing-and-mechanism.md#format).

## Phase 5 — Visual Assets

Retrieve supporting visuals per the single priority list in [Visual Assets](/rules/RULE-002-visual-asset-priority.md) — four tiers, no more, no fewer. Every visual states its decision value.

## Phase 6 — QA Gate

Run the ten questions in [QA Gate](/checklists/CHECKLIST-001-qa-gate.md). Any "No" → revise or set status to WAIT.

## Final Output

Every response ends with: Publication Status, Confidence Level, Evidence Classification, and any Verification Limitations.
