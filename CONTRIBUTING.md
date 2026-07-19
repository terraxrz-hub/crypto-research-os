# Contributing

This framework's entire value depends on one discipline: **every rule has exactly one canonical page, and every other page links to it instead of restating it.** The redesign that produced this repository's current structure exists specifically because that discipline was absent before — three non-identical trust taxonomies, the same QA rules re-typed in several places, a canonical page cited everywhere that was itself empty. Contributing here means actively defending that discipline, not just adding content.

## Before changing anything in `docs/`

1. **Find the owning page.** Every concept in the framework has exactly one home — check the "canonical" callouts at the top of pages like `docs/02-evidence-framework.md` and `docs/08-qa-gate.md` for examples of how ownership is declared. If you're about to write a sentence that restates a rule instead of linking to it, stop.
2. **If the concept is genuinely new**, give it its own numbered page (next in sequence) and link to it from every page that touches it. Don't fold a new independent rule into an existing page as a tangent.
3. **If you're changing an existing rule**, change it in its one owning page. Then grep the repository for any other place that might have drifted into restating the old version, and fix those to link instead.
4. **Update the Issue Forms if they reference the changed rule** (e.g. a dropdown option in `research-entry.yml` that mirrors an Evidence Tier name) — the forms and the docs must never say different things about the same taxonomy.

## Pull requests

- Open a PR against `main`; direct pushes are blocked by branch protection (see `SETUP.md` §2 step 6).
- Use the PR template's checklist — it specifically asks which canonical page owns the concept you touched and whether any other page needed a corresponding link update.
- A `docs/**` change on `main` auto-opens a `type:changelog` Issue. Fill in the `Reason` and `Impact` fields on it before considering the change done — an undocumented "why" is exactly the failure mode this framework is designed to prevent.
- Small wording/typo fixes that carry no rule-level meaning can include `[skip-changelog]` in the commit message to avoid opening a changelog issue for something with nothing to explain.

## Changing workflows or repository configuration

Treat `.github/workflows/`, `.github/labels.yml`, and the Projects board field schemas in `SETUP.md` as also-canonical, even though the boards themselves aren't files in this repo. If you change a board's fields, update `SETUP.md` in the same PR so the two don't drift apart — open a **Changelog Entry** issue (the manual form) to record it, since it won't be caught by the automatic docs-triggered workflow.

## Code of conduct

Be direct, be precise, and default to citing the owning page rather than re-explaining a rule in a comment or review. Disagreements about where a rule should live are welcome — silently duplicating it instead of resolving the disagreement is the one thing not welcome here.
