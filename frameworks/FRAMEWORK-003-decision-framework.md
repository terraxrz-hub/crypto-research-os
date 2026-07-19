---
id: FRAMEWORK-003
type: framework
title: "Decision Framework"
status: active
version: 1
tags: [story-selection, ranking, ev, wait-rule]
related: [FRAMEWORK-001, RULE-003, PLAYBOOK-0001, PLAYBOOK-0002, GLOSSARY]
owns: ["six-criteria story ranking", "re-ranking rule", "WAIT rule", "time-boxing/escalation path"]
criteria: ["Evidence Strength", "Educational Value", "Market Impact", "Originality", "Shelf Life", "Mechanism Quality"]
summary: >
  The six weighted criteria used to rank candidate stories by expected value,
  the mandatory re-ranking trigger when new evidence weakens confidence, the
  WAIT rule (publish nothing beats publishing something misleading), and the
  time-boxing/escalation path for breaking news.
source_of_truth: true
---

# Decision Framework

Finding a true story isn't enough. The objective is to find the story that creates the **greatest improvement in the reader's understanding and decision-making**. Every research cycle begins with ranking candidate stories before any writing starts.

> This page is the single owner of story-ranking and re-ranking logic. [Research Workflow](/playbooks/PLAYBOOK-0001-research-workflow.md) and [Daily Workflow](/playbooks/PLAYBOOK-0002-daily-workflow.md) reference these six criteria by name — they don't restate them.

## The six evaluation criteria

1. **Evidence Strength** — priority order matches [Evidence Framework](/frameworks/FRAMEWORK-001-evidence-tier-framework.md): Primary > Independent Confirmation > Trusted Intermediaries > Corroborated Secondary > Unverified. Weak evidence lowers the score regardless of how interesting the story looks.
2. **Educational Value** — does it explain a mechanism, correct a misconception, reveal an overlooked fact, or connect separate verified facts? If the reader learns nothing beyond the headline, the score is low.
3. **Market Impact** — liquidity, regulation, institutional adoption, security, infrastructure, market structure. Large price moves alone don't imply high impact.
4. **Originality** — how likely is an informed reader to already know this? Repeated stories score lower than unique, evidence-backed insight.
5. **Shelf Life** — will this matter weeks or months from now? Prefer durable knowledge over temporary headlines.
6. **Mechanism Quality** — can the underlying mechanism be explained clearly? Stories that teach *why* beat stories that only describe *what*.

No single criterion automatically wins. The objective is maximum overall expected value (EV) across all six.

## Alternative Explanations

Before finalizing a story: What else could explain the evidence? Why is the chosen explanation stronger? What evidence would change the conclusion? If multiple explanations remain plausible, keep the uncertainty visible rather than forcing a clean narrative.

## Re-Ranking Rule

If new evidence lowers confidence in the selected story: **stop, re-rank every candidate again.** Never continue simply because research has already started. This is the one and only re-ranking procedure in the framework — [Research Workflow](/playbooks/PLAYBOOK-0001-research-workflow.md) triggers it but doesn't duplicate it.

## Time-boxing / escalation path

For genuinely time-sensitive breaking news where full primary verification isn't feasible inside the relevant window:

- State explicitly that this is a time-boxed assessment, not a fully verified one.
- Publish only at **PASS WITH LIMITATIONS**, with the time constraint stated as the limitation — never at PASS.
- If even a time-boxed limited assessment can't clear the bar, the answer is still **WAIT**. There is no third option between "verify fully" and "WAIT" — a rushed PASS is never acceptable.

## WAIT Rule

If no candidate satisfies the framework: publish nothing. A high-quality WAIT beats a weak story. See [Publication Standard](/rules/RULE-003-publication-standard.md).
