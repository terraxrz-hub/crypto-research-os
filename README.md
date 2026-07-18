# Crypto Research OS (v2)

A research operating system for daily crypto research, verification, and publication — one canonical page per rule, database-backed history instead of static prose, and a QA gate that's enforced rather than trusted.

Migrated from a 15-page flat Notion workspace. See [SETUP.md](SETUP.md) for the full migration plan, what changed and why, and exact setup steps for the Projects boards and Actions secrets. See [CHANGELOG.md](CHANGELOG.md) for version history.

## Architecture

```
crypto-research-os
├── docs/                          — Philosophy & Standards layer (static, one page per rule)
│   ├── 00-objective.md
│   ├── 01-sources-and-priority.md
│   ├── 02-evidence-framework.md   ← canonical evidence tiers, referenced everywhere
│   ├── 03-writing-and-mechanism.md
│   ├── 04-visual-assets.md
│   ├── 05-on-chain-verification.md
│   ├── 06-decision-framework.md
│   ├── 07-publication-standard.md
│   ├── 08-qa-gate.md
│   ├── 09-research-workflow.md
│   ├── 10-daily-workflow.md       ← start here for the day-to-day sequence
│   └── glossary.md
├── prompts/
│   └── prompt-library.md          — Tooling layer, merged & deduplicated
├── .github/
│   ├── ISSUE_TEMPLATE/            — Operating layer: the Research + Source Reliability + Correction "databases"
│   ├── workflows/                 — Automation: QA gate enforcement, changelog automation, project sync, review reminders
│   └── labels.yml                 — Evidence tiers, publication status, entry types as repo labels
└── CHANGELOG.md
```

## The two "databases"

This repo doesn't use a real database — it uses GitHub natively as one:

- **Research Database** → every `type:research` Issue (via the **Research Entry** template), surfaced on a GitHub Projects (v2) board with custom fields (Evidence Tier, Publication Status, EV components). One row per story evaluated, including WAIT outcomes — the audit's single biggest fix.
- **Source Reliability Database** → every `type:source` Issue (via the **Source Reliability Record** template), on its own Project board, tracking a source's track record instead of treating "trusted" as a permanent label.
- **Changelog** → `type:changelog` Issues, auto-opened whenever `docs/` changes on `main`.
- **Corrections** → `type:correction` Issues, linked back to the original research entry.

## Daily use

1. Open a new **Research Entry** issue (Issues → New Issue).
2. Work the phases in [Daily Workflow](docs/10-daily-workflow.md) — each maps to a field on the form.
3. Tick the 10 QA Gate checkboxes as you satisfy them.
4. Apply the `status:PASS` (or `PASS-WITH-LIMITATIONS`) label. **QA Gate Enforcement** will bounce it back if the boxes aren't all checked.
5. Publish. Come back later and fill in **Outcome** — or let the weekly review reminder nudge you.

## Why this exists instead of Notion

Full rationale in [SETUP.md](SETUP.md), but in short: the original 15-page workspace had one internal contradiction, three conflicting trust taxonomies, drifted duplicate copies of the same rules in up to 7 places, an empty canonical "Writing & Mechanism" page cited everywhere, and no research history, source reliability tracking, or post-publication review. Flat prose can't fix that on its own — it needed a place to persist state.
