# Setup & Migration

## 1. Why each structural change

| V1 problem | V2 fix | Maintenance problem solved |
|---|---|---|
| 15 flat pages, no hierarchy | 4 layers: Philosophy/Standards (`docs/`), Operating layer (Issues+Projects), Tooling (`prompts/`), Dashboard (`README.md`) | A new reader (or future-you) can tell what's foundational vs. operational vs. reference at a glance. |
| Evidence Framework's own two sections disagreed on whether Trusted Intermediaries outranks Corroborated Secondary | One resolved, ordered tier table in `docs/02-evidence-framework.md` | No more internally contradictory canonical page. |
| Three non-identical trust taxonomies (Evidence Framework 6 tiers / Sources & Priority 5 tiers / Visual Assets 4 tiers) | One tier table, referenced by all three pages instead of restated | A CertiK audit, or a Glassnode-vs-CryptoQuant agreement, now has one unambiguous answer instead of three. |
| Same rules re-typed in 4–7 places (QA gate, mechanism-first, publication states, visual priority) and already drifted apart (Visual Assets 4 tiers vs. Daily Workflow's restatement had 5) | One canonical page per rule; every other page link-references it | New rule changes get made once, not hand-copied into 3–5 places every time — the root cause of drift is removed. |
| `Writing & Mechanism` was a title with zero body content, cited by 7 other pages | Written, in `docs/03-writing-and-mechanism.md`, as one governing principle with the rest as consequences | The most externally visible part of the system (the actual writing) now has an owned definition instead of an inferred shadow. |
| `Prompt Library` and `Prompts` were ~85% duplicate pages | Merged into `prompts/prompt-library.md` | One file to update when a prompt changes. |
| `Research Template` was the best-designed page but buried at position 12/15, and discarded after each use | Promoted to the actual daily interface — the `research-entry` Issue form, which persists as a database row instead of a disposable form | Nothing gets thrown away; every entry becomes queryable history. |
| No research journal, no WAIT log, no post-publication review | Every entry — including WAIT outcomes — is a permanent Issue with an `Outcome` field and a scheduled review reminder | Report #500 can now learn from report #1. |
| No correction/error log | `type:correction` issue template, linked back to the original entry | Institutional-grade "how we correct the record" process, previously entirely undefined. |
| "Trusted" sources treated as a permanent, unexamined label | `type:source` issue template = Source Reliability Database, one row per named source | Track record is now tracked, not assumed. |
| Changelog was a growing prose page, easy to forget to update | GitHub Action auto-opens a `type:changelog` issue whenever `docs/` changes on `main` | Rule changes can't happen silently anymore — it's structurally enforced, not just requested. |
| QA Gate was an honor-system checklist | GitHub Action strips a `status:PASS` label if not all 10 checkboxes are ticked | Turns "please check these boxes" into "you cannot mislabel this as PASS." |
| No time-pressure exception path | Explicit time-boxing/escalation section in `docs/06-decision-framework.md` | Breaking news no longer forces a binary choice between "verify fully" or WAIT with no defined middle ground. |
| Decision Framework's 6 criteria were never invoked by name in Daily Workflow's Phase 1 | `docs/10-daily-workflow.md` Phase 1 now names all six explicitly | Story selection is no longer under-specified at the exact moment it happens. |

## 2. Migration plan (Notion V1 → this repo)

1. **Create the repo.** `git init` is already done in this delivered folder — create an empty repo on GitHub (no README/license, to avoid a conflicting initial commit), then:
   ```
   cd crypto-research-os
   git remote add origin https://github.com/<you>/crypto-research-os.git
   git branch -M main
   git push -u origin main
   ```
2. **Enable labels.** The `Label Sync` workflow runs automatically on the first push (it triggers on changes to `.github/labels.yml`, which this push includes) — or trigger it manually from the Actions tab (`workflow_dispatch`) if it doesn't fire.
3. **Create two Projects (v2) boards** — Settings aren't file-based, so this step is manual:
   - **Research Database**: Organization/user → Projects → New project → Board or Table view. Add fields: `Evidence Tier` (single select, matching the 7 tiers), `Publication Status` (single select: WAIT / PASS WITH LIMITATIONS / PASS), `Evidence Strength`, `Educational Value`, `Market Impact`, `Originality`, `Shelf Life`, `Mechanism Quality` (all number, 1–10, matching Decision Framework's six criteria), `Outcome` (text).
   - **Source Reliability Database**: New project → Table view. Add fields: `Default Tier` (single select), `Last Reviewed` (date), `Track Record Summary` (text).
   - Copy each board's URL — you'll need both.
4. **Create a PAT for cross-Project automation.** Projects (v2) at the user/org level can't be written to by the default `GITHUB_TOKEN`. Settings → Developer settings → Fine-grained tokens → create one scoped to this repo with **Projects: Read and write**. Add it as a repo secret named `ADD_TO_PROJECT_PAT`.
5. **Fill in the placeholders** in `.github/workflows/project-auto-add.yml` — replace `OWNER`, `PROJECT_NUMBER`, and `PROJECT_NUMBER_2` with your real project URLs from step 3. Commit and push.
6. **Enable Actions write permissions.** Settings → Actions → General → Workflow permissions → "Read and write permissions" (needed for the QA Gate Enforcement and Changelog Automation workflows to label/comment).
7. **Retire the Notion workspace** once you've filed a few real `research-entry` issues here and confirmed the workflows fire correctly — don't dual-run both systems longer than a week or two, or duplication just moves from Notion pages to Notion-vs-GitHub.

## 3. Missing components (from the audit — now addressed here)

- ✅ Post-publication review → `Outcome` field + weekly `review-reminder.yml`
- ✅ Correction / error log → `type:correction` issue template
- ✅ Source reliability tracking → `type:source` issue template + Source Reliability board
- ✅ Research journal / WAIT archive → every entry is a permanent Issue, including WAIT outcomes
- ✅ Decision log for WAIT outcomes → filterable via the `status:WAIT` label on the Research board
- ✅ Glossary → `docs/glossary.md`
- ✅ Audience/reader-context → added to `docs/00-objective.md`
- ✅ Escalation / time-pressure path → added to `docs/06-decision-framework.md`
- ⚠️ **Reconciliation with the chat-based standing rules** (Market Impact Score, Content Opportunity Score, EV-per-tweet calculus, weekly evergreen-content placement) — **not done here**, since that rule set lives outside this workspace and wasn't in the export. If you want it folded in, paste those standing rules and they can be merged into `docs/06-decision-framework.md` and `docs/10-daily-workflow.md` as a follow-up.

## 4. Final verdict

Version 2. The ideas in V1 were genuinely good — decision quality over speed, the weakest-link publication rule, evidence-proportional confidence — better than most retail crypto commentary operates on. But 15 static pages with no links and one empty canonical page couldn't survive contact with report #500, let alone a second contributor. Issues + Projects doesn't change any of the underlying philosophy — it just gives it a place to persist, get enforced, and get smarter over time instead of repeating the same fixed ruleset forever.
