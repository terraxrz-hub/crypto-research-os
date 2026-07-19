# Architecture & Setup Guide

This is the one-time setup for turning this repository into a running instance of the framework, plus the design rationale behind why each layer is built the way it is.

## 1. Design rationale

| Design decision | What it solves |
|---|---|
| Nine knowledge-object types across the Philosophy/Standards layer (`rules/`, `frameworks/`, `playbooks/`, `checklists/`), Reference layer (`tools/`, `sources/`, `research/`, `examples/`), Tooling (`prompts/`), Operating layer (Issues + Projects) | A new reader (or future-you) can tell what's foundational vs. operational vs. reference at a glance. |
| One resolved, ordered evidence-tier table, owned by `/frameworks/FRAMEWORK-001-evidence-tier-framework.md` | A single unambiguous answer for any evidence question — e.g. whether a named analytics platform outranks ten outlets repeating one unnamed source — instead of several pages independently defining overlapping taxonomies that can drift apart. |
| One canonical page per rule; every other page link-references it instead of restating it | Rule changes get made once, not hand-copied into several places every time — this removes the root cause of documentation drift rather than just tidying it up after the fact. |
| `/frameworks/FRAMEWORK-004-writing-and-mechanism.md` states the governing principle explicitly, with everything else as a named consequence of it | The most externally visible part of the system — the actual writing — has an owned, explicit definition instead of an inferred shadow. |
| `/prompts/README.md` is a single deduplicated set, one prompt per workflow step | One file to update when a prompt changes; no overlapping near-duplicate prompt sets to keep in sync. |
| The `research-entry` Issue Form is the daily interface, not a disposable draft | Nothing gets thrown away; every entry — including WAIT outcomes — becomes a queryable, permanent row in the Research Database. |
| Every entry has an `Outcome` field and a scheduled review reminder | Report #500 can learn from report #1, and a stated limitation can't quietly age out of anyone's attention. |
| `type:correction` Issue Form, linked back to the original entry | A defined, auditable process for correcting the record — not an undefined, ad hoc one. |
| `type:source` Issue Form = Source Reliability Database, one row per named source | Track record is tracked over time, not assumed and frozen the first time a source turns out to be right. |
| GitHub Action auto-opens a `type:changelog` issue whenever the knowledge layer (`rules/`, `frameworks/`, `playbooks/`, `checklists/`) changes on `main` | Rule changes can't happen silently — capturing the reason for a change is structurally enforced, not just requested. |
| GitHub Action strips a `status:PASS` label if not all 10 QA checkboxes are ticked | Turns "please check these boxes" into "you cannot mislabel this as PASS." |
| Explicit time-boxing/escalation section in `/frameworks/FRAMEWORK-003-decision-framework.md` | Breaking news doesn't force a binary choice between "verify fully" or WAIT with no defined middle ground. |
| `/playbooks/PLAYBOOK-0002-daily-workflow.md` Phase 1 names the six Decision Framework criteria explicitly | Story selection is never under-specified at the exact moment it happens. |

## 2. First-time setup

1. **Enable labels.** The **Label Sync** workflow runs automatically on any push that touches `.github/labels.yml` — or trigger it manually from the Actions tab (`workflow_dispatch`).
2. **Create two Projects (v2) boards** — board configuration isn't file-based, so this step is manual:
   - **Research Database**: your account or org → Projects → New project → Board or Table view. Add fields: `Evidence Tier` (single select, matching the 7 tiers in `/frameworks/FRAMEWORK-001-evidence-tier-framework.md`), `Publication Status` (single select: WAIT / PASS WITH LIMITATIONS / PASS), `Evidence Strength`, `Educational Value`, `Market Impact`, `Originality`, `Shelf Life`, `Mechanism Quality` (all number, 1–10, matching the Decision Framework's six criteria), `Outcome` (text).
   - **Source Reliability Database**: New project → Table view. Add fields: `Default Tier` (single select), `Last Reviewed` (date), `Track Record Summary` (text).
   - Copy each board's URL.
3. **Set repository variables** (Settings → Secrets and variables → Actions → Variables) rather than editing workflow files directly:
   - `RESEARCH_PROJECT_URL` — the Research Database board URL from step 2.
   - `SOURCE_PROJECT_URL` — the Source Reliability Database board URL from step 2.

   Keeping these as repository **variables** instead of hardcoded values in `project-auto-add.yml` means the workflow file never needs to change per-repository, and the **Verify Setup** job (see below) can check they're populated before anything relies on them.
4. **Create a PAT for cross-Project automation.** Projects (v2) at the user/org level can't be written to by the default `GITHUB_TOKEN`. Settings → Developer settings → Fine-grained tokens → create one scoped to this repository with **Projects: Read and write**. Add it as a repository secret named `ADD_TO_PROJECT_PAT`. Set a calendar reminder near its expiry — an expired PAT fails the "add to project" step silently from the maintainer's point of view (no Issue is annotated), which is the one failure mode this framework doesn't yet self-report.
5. **Enable Actions write permissions.** Settings → Actions → General → Workflow permissions → "Read and write permissions" (needed for QA Gate Enforcement, Changelog Automation, and the review reminder to label/comment).
6. **Apply branch protection.** Run `scripts/apply-branch-protection.sh` (requires the [`gh` CLI](https://cli.github.com/), authenticated) to apply the recommended ruleset on `main` in one step, or configure manually per Settings → Branches:
   - Require a pull request before merging (no direct pushes to `main`).
   - Require the **Validate** workflow to pass.
   - Require conversation resolution before merging.

   Branch protection matters here specifically because a docs change lands directly on `main` and immediately fires the Changelog Automation workflow — a stray, unreviewed push shouldn't be able to trigger that on its own.
7. **(Optional) Enable the AI-assisted research scan.** If you want `ai-research-scan.yml` available, add an `ANTHROPIC_API_KEY` repository secret. This workflow drafts a *scaffold* Research Entry issue from a topic you give it — it does not perform verification and every field it fills is explicitly marked `[ai-drafted, unverified]`. It is a starting point for the human-run Daily Workflow, not a substitute for it; the QA Gate still applies in full before anything can reach `status:PASS`.
8. **Tag your first release.** Once the above is running end-to-end, tag `v2.1.0` (`git tag v2.1.0 && git push origin v2.1.0`) — the **Release** workflow will build the GitHub Release automatically from `CHANGELOG.md` and commit history. See the versioning note in `CHANGELOG.md` for how releases and the changelog relate going forward.

## 3. Verifying setup

Run the **Validate** workflow manually (Actions tab → Validate → Run workflow) at any point. It checks: YAML syntax across `.github/**`, that `RESEARCH_PROJECT_URL` / `SOURCE_PROJECT_URL` variables are set and not left as placeholder text, and that internal documentation links resolve. Fix anything it flags before relying on the automation in production.
