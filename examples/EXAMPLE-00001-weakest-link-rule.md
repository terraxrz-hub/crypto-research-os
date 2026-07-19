---
id: EXAMPLE-00001
type: example
title: "Worked Example: Applying the Weakest-Link Rule"
status: active
version: 1
tags: [example, weakest-link, qa-gate]
related: [RULE-003, FRAMEWORK-001, CHECKLIST-001]
illustrates: [RULE-003, FRAMEWORK-001]
outcome: "PASS WITH LIMITATIONS"
summary: >
  A fictional, illustrative walkthrough (not a real research entry) showing
  how nine Tier-1/2 facts plus one Tier-3 fact resolve to PASS WITH
  LIMITATIONS rather than PASS, per the Weakest-Link Rule.
source_of_truth: false
---

# Worked Example: Applying the Weakest-Link Rule

> **This is a fictional illustration, not a real research finding.** It exists to show how [Publication Standard](/rules/RULE-003-publication-standard.md)'s Weakest-Link Rule resolves a mixed-tier evidence chain in practice.

## Scenario (illustrative)

A hypothetical protocol "Protocol X" pauses withdrawals. The scaffold researcher gathers:

1. The protocol's official on-chain pause transaction, verified directly via a block explorer — **Tier 1**.
2. The protocol's official status-page statement confirming the pause — **Tier 1**.
3–9. Seven additional on-chain and official-statement facts establishing the timeline, contract address, and affected pools — all **Tier 1** or **Tier 2** (independently confirmed by two unrelated on-chain analysts using different methods).
10. The *stated reason* for the pause ("suspected exploit attempt") — sourced only from a single trusted analytics platform's post interpreting the transaction pattern, not independently confirmed — **Tier 3**.

## Applying the rule

Nine of ten facts are Tier 1–2. Per the [Evidence Tier Framework](/frameworks/FRAMEWORK-001-evidence-tier-framework.md), Tier 3 evidence is real and usable — but per [Publication Standard](/rules/RULE-003-publication-standard.md)'s Weakest-Link Rule, publication status is set by the *weakest* verified link, not the average or the strongest. Nine strong facts cannot upgrade the one Tier-3 claim.

## Resulting status: PASS WITH LIMITATIONS

The piece can publish the confirmed pause, timeline, and affected pools as verified fact (Tier 1–2). The *reason* for the pause must be explicitly attributed ("according to [platform]...") and flagged as the limitation, per the Transparency Rule. It cannot be written as settled fact, and the entry cannot be labeled `status:PASS`.

## QA Gate check (selected)

- Question 4 ("does every conclusion remain proportional to the available evidence?") — Yes, because the reason is explicitly hedged rather than stated flatly.
- Question 1 ("is every factual claim independently verified?") — No for the stated reason specifically — this is exactly why the status is PASS WITH LIMITATIONS rather than PASS, not a reason to answer "No" for the whole entry.

See the full ten questions in [QA Gate](/checklists/CHECKLIST-001-qa-gate.md).
