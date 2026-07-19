---
id: PLAYBOOK-0001
type: playbook
title: "Research Workflow"
status: active
version: 1
tags: [workflow, research, verification]
related: [FRAMEWORK-003, RULE-001, FRAMEWORK-001, PLAYBOOK-0002]
phases: ["fresh research every time", "story selection", "verification order", "time pressure handling"]
depends_on: [FRAMEWORK-003, RULE-001, FRAMEWORK-001]
produces: research
summary: >
  The always-fresh-research discipline (never reuse prior scans or prices),
  how story selection defers entirely to the Decision Framework's six
  criteria, verification order per Source Priority, and the time-boxing
  fallback for breaking news.
source_of_truth: true
---

# Research Workflow

## Fresh research every time

Start every task with a new market scan, regardless of how recently a previous scan was performed. Never reuse prices, market data, flows, or statistics from an earlier session. Refresh all critical numbers again immediately before the final draft — if anything changed since the initial research, state the change explicitly rather than silently updating it.

## Story selection

Search for the highest expected-value story, not the loudest or most viral one. Candidates are ranked using the six criteria owned by [Decision Framework](/frameworks/FRAMEWORK-003-decision-framework.md) — this page doesn't re-derive them.

If a stronger story appears during verification, trigger the [Decision Framework's Re-Ranking Rule](/frameworks/FRAMEWORK-003-decision-framework.md#re-ranking-rule) before continuing. Don't stay anchored to the first story selected just because research has already started.

## Verification order

Follow [Sources & Research Priority](/rules/RULE-001-source-priority-order.md). Never confuse repeated reporting with independent evidence — see the Corroborated Secondary tier in [Evidence Framework](/frameworks/FRAMEWORK-001-evidence-tier-framework.md).

## Time pressure

If a story is breaking and full primary verification isn't feasible in the relevant window, follow the [time-boxing / escalation path](/frameworks/FRAMEWORK-003-decision-framework.md#time-boxing--escalation-path) — don't let verification loop indefinitely between "verify further" and "re-rank" with no forcing function. Set an explicit time-box; if the bar isn't cleared by then, the answer is WAIT, or PASS WITH LIMITATIONS with the time constraint stated as the limitation.
