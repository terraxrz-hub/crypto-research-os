---
id: CHECKLIST-001
type: checklist
title: "QA Gate"
status: active
version: 1
tags: [qa, publication, enforcement, canonical]
related: [RULE-003, FRAMEWORK-004, RULE-002, PLAYBOOK-0002]
validates: [PLAYBOOK-0002, RULE-003]
machine_checkable: true
items:
  - id: 1
    question: "Is every factual claim independently verified?"
  - id: 2
    question: "Have all prices and market data been refreshed immediately before publication?"
  - id: 3
    question: "Are facts, analysis, and uncertainty clearly separated?"
  - id: 4
    question: "Does every conclusion remain proportional to the available evidence?"
  - id: 5
    question: "Does the content explain the mechanism before the conclusion?"
  - id: 6
    question: "Would I still stand behind every sentence six months from now?"
  - id: 7
    question: "Does this content teach something beyond today's headline?"
  - id: 8
    question: "Is this the highest expected-value story available right now?"
  - id: 9
    question: "Would this still be valuable if published anonymously?"
  - id: 10
    question: "Could every sentence survive scrutiny from a knowledgeable critic?"
enforced_by: [qa-gate-enforcement.yml]
summary: >
  The canonical ten-question gate every piece of content passes before
  publication. All ten must be "Yes" (all ten checkboxes ticked in the
  research-entry Issue Form) before a status:PASS or
  status:PASS-WITH-LIMITATIONS label survives — the QA Gate Enforcement
  GitHub Action strips the label otherwise.
source_of_truth: true
---

# QA Gate

Every piece of content passes the same review before publication. This catches weak evidence, hidden assumptions, overstated conclusions, and unnecessary complexity. **Publishing quickly is never more important than publishing correctly.**

> This is the canonical QA Gate. [Daily Workflow](/playbooks/PLAYBOOK-0002-daily-workflow.md), the `research-entry` issue form, and the [Prompt Library](/prompts/README.md) all say "run the QA Gate" and point here — none of them restate the ten questions.

## QA Principles

- Every factual claim must be traceable to evidence.
- Every conclusion must match the strength of the evidence.
- Facts, analysis, and uncertainty stay clearly separated.
- The mechanism is explained before the conclusion.
- If something can't be defended, it doesn't get published.

## The 10-Question Gate

- [ ] 1. Is every factual claim independently verified?
- [ ] 2. Have all prices and market data been refreshed immediately before publication?
- [ ] 3. Are facts, analysis, and uncertainty clearly separated?
- [ ] 4. Does every conclusion remain proportional to the available evidence?
- [ ] 5. Does the content explain the mechanism before the conclusion?
- [ ] 6. Would I still stand behind every sentence six months from now?
- [ ] 7. Does this content teach something beyond today's headline?
- [ ] 8. Is this the highest expected-value story available right now?
- [ ] 9. Would this still be valuable if published anonymously?
- [ ] 10. Could every sentence survive scrutiny from a knowledgeable critic?

**Decision rule:** if any answer is No, revise the content or set the Publication Status to WAIT. Never lower the standard just to publish.

The `research-entry` issue form embeds these same ten boxes as real checkboxes. The **QA Gate Enforcement** GitHub Action blocks a `status:PASS` or `status:PASS WITH LIMITATIONS` label from being applied unless all ten are checked — this is the "honor system → enforced system" fix from the audit (Step 13).

## Final checklist before publishing

- Evidence classification is correct.
- Confidence matches the evidence.
- All important uncertainty is disclosed.
- Source disagreements are preserved.
- Attribution is accurate.
- Visual recommendations (if any) are correctly labeled — see [Visual Assets](/rules/RULE-002-visual-asset-priority.md).
- The writing improves decision quality.

## Final output

Every research report ends with: **Publication Status** (PASS / PASS WITH LIMITATIONS / WAIT), plus any material changes since the initial scan, stated explicitly — never updated silently.
