# Publication Standard

Every story ends with one of three publication statuses. The status is determined by the **weakest verified part of the evidence chain** — not the strongest.

## PASS

Use only when: core claims are supported by Primary Evidence or genuine Independent Confirmation (Tier 1–2, see [Evidence Framework](02-evidence-framework.md)); no material verification gap remains; confidence is proportional to the evidence; the story improves the reader's understanding or decision-making.

## PASS WITH LIMITATIONS

Publishable, but an important limitation remains — e.g. the story depends on a single trusted analytics provider (Tier 3), a transaction/explorer record couldn't be independently verified, only part of the story is Tier 1, implementation details are pending, or the assessment was time-boxed under the [escalation path](06-decision-framework.md#time-boxing--escalation-path). **Every limitation must be stated inside the final content, not hidden.**

## WAIT

Choose WAIT whenever evidence is insufficient, important contradictions remain unresolved, confidence is too low, or the story wouldn't improve the reader's decisions. Publishing nothing beats publishing something misleading.

## Weakest-Link Rule

Publication status is set by the weakest verified link. Nine strong facts cannot upgrade one unverified claim. One missing verification can prevent PASS.

## Transparency Rule

Never hide verification gaps. Always state what was verified, what couldn't be, and why confidence is limited. Readers should know exactly where certainty ends.

## Re-review trigger

A **PASS WITH LIMITATIONS** entry is not closed once published. If the missing verification later becomes available, or new evidence contradicts the original claim:

1. Reopen the corresponding `type:research` issue (or file a new `type:correction` issue linking back to it).
2. Re-run the evidence classification with the new information.
3. If the conclusion changes, publish a correction and record it — see the `type:correction` issue template.
4. Update the original issue's **Outcome** field regardless of whether the conclusion changed, so the record is never silently left stale.

This closes the gap the audit flagged: previously nothing tracked whether a limitation got resolved or a conclusion needed revisiting after publication.
