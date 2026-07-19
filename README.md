# Crypto Research OS

A GitHub-native research operating system for daily crypto research, verification, and publication — one canonical page per rule, database-backed history instead of static prose, and a QA gate that's enforced by automation rather than trusted on the honor system.

GitHub is the platform of record: Issues are the database, Projects is the reporting layer, Actions is the enforcement layer, and `docs/` is the single, versioned source of truth for the rules themselves. There is no external workspace, export, or secondary tool to keep in sync — everything the framework needs to operate lives in this repository.

See [SETUP.md](SETUP.md) for first-time setup (Projects boards, secrets, branch protection, releases) and [CHANGELOG.md](CHANGELOG.md) for version history. See [CONTRIBUTING.md](CONTRIBUTING.md) before changing any file in `docs/`.

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
│   └── prompt-library.md          — Tooling layer: one prompt per workflow step, each a thin trigger into docs/
├── scripts/
│   └── apply-branch-protection.sh — Reproducible `gh` script for the recommended ruleset (see SETUP.md)
├── .github/
│   ├── ISSUE_TEMPLATE/            — Operating layer: Research, Source Reliability, Correction, and Changelog "databases"
│   ├── workflows/                 — Automation: QA gate enforcement, changelog automation, project sync, review reminders, releases, validation, AI-assisted drafting
│   ├── labels.yml                 — Evidence tiers, publication status, entry types as repo labels
│   ├── dependabot.yml             — Keeps third-party Actions current
│   ├── CODEOWNERS
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── SECURITY.md
│   └── SUPPORT.md
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

## The two databases

This repository doesn't bolt on an external database — GitHub's own primitives *are* the database:

- **Research Database** → every `type:research` Issue (via the **Research Entry** form), surfaced on a GitHub Projects (v2) board with custom fields (Evidence Tier, Publication Status, the six EV components). One row per story evaluated, including WAIT outcomes.
- **Source Reliability Database** → every `type:source` Issue (via the **Source Reliability Record** form), on its own Project board, tracking a source's track record instead of treating "trusted" as a permanent label.
- **Changelog** → `type:changelog` Issues — auto-opened whenever `docs/` changes on `main`, or opened manually via the **Changelog Entry** form for changes that don't touch `docs/` directly (e.g. a Project board schema change).
- **Corrections** → `type:correction` Issues, linked back to the original research entry.

Every one of these is a native GitHub object: an Issue, a label, a Project field. Nothing here requires exporting to, or importing from, anything else.

## Daily use

1. Open a new **Research Entry** issue (Issues → New Issue).
2. Work the phases in [Daily Workflow](docs/10-daily-workflow.md) — each maps to a field on the form.
3. Tick the 10 QA Gate checkboxes as you satisfy them.
4. Apply the `status:PASS` (or `status:PASS-WITH-LIMITATIONS`) label. **QA Gate Enforcement** will bounce it back if the boxes aren't all checked.
5. Publish. Come back later and fill in **Outcome** — or let the weekly review reminder nudge you.

## Why GitHub-native

Everything the framework needs — history, enforcement, review, versioning, access control — is a first-class GitHub feature: Issues for records, Projects for views, Actions for enforcement, labels for taxonomy, branch protection and CODEOWNERS for governance, Releases for versioning. Building directly on these primitives means the system of record, the automation that enforces its rules, and the audit trail of how those rules changed all live in one place, under one permission model, with one history. See [SETUP.md](SETUP.md) for exactly how each piece is wired together.
