# Support

## Using the framework

Start with [`docs/00-objective.md`](../docs/00-objective.md), then [`docs/10-daily-workflow.md`](../docs/10-daily-workflow.md) for the day-to-day sequence. `README.md` covers the repository layout and daily-use steps at a glance.

## Something isn't working

- **A workflow isn't firing, or a label isn't being applied/removed as expected** — check `SETUP.md` §3 ("Verifying setup") and run the **Validate** workflow manually first; most issues trace back to an unset repository variable or secret.
- **You disagree with how a rule is written, or think two pages have drifted apart** — open an Issue using the **Changelog Entry** form describing the inconsistency, or, if you know the fix, open a pull request per `CONTRIBUTING.md`.
- **You found a security-relevant issue** (a leaked token, an exploitable workflow) — see `.github/SECURITY.md` instead; do not open a public Issue for this.

## Questions about the framework's rules themselves

Open a discussion or Issue rather than emailing — keeping the question in-repo means the answer becomes part of the searchable history, consistent with how this framework treats every other decision.
