# QA Gate

Every piece of content passes the same review before publication. This catches weak evidence, hidden assumptions, overstated conclusions, and unnecessary complexity. **Publishing quickly is never more important than publishing correctly.**

> This is the canonical QA Gate. [Daily Workflow](10-daily-workflow.md), the `research-entry` issue form, and the [Prompt Library](../prompts/prompt-library.md) all say "run the QA Gate" and point here — none of them restate the ten questions.

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
- Visual recommendations (if any) are correctly labeled — see [Visual Assets](04-visual-assets.md).
- The writing improves decision quality.

## Final output

Every research report ends with: **Publication Status** (PASS / PASS WITH LIMITATIONS / WAIT), plus any material changes since the initial scan, stated explicitly — never updated silently.
