# Changelog

Every meaningful change to the operating framework is recorded here or as a `type:changelog` GitHub Issue — preserving the reasoning behind each change so rules evolve deliberately, not accidentally.

**Versioning strategy:** changelog entries live as Issues labeled `type:changelog`, with structured fields (Version, Section Changed, Change, Reason, Impact) — auto-opened by the **Changelog Automation** workflow whenever `docs/` changes on `main`, or opened manually via the **Changelog Entry** issue form for changes that don't touch `docs/` directly (a Projects board schema change, a workflow permission change, etc.). This file is a static index of tagged releases and is not appended to by hand for day-to-day rule changes — check the `type:changelog` label for the live log, and see [Releases](https://github.com/terraxrz-hub/crypto-research-os/releases) for the versioned, citable snapshots.

A version gets tagged (`vX.Y.Z`, see the **Release** workflow) when a set of `type:changelog` issues represents a coherent, shippable change to the framework — not on every individual docs edit.

## Version History

### v2.1.0 — Production hardening & GitHub-native governance
- **Section:** Repository governance and automation.
- **Change:** Added `LICENSE`, `CODEOWNERS`, `SECURITY.md`, `CONTRIBUTING.md`, `SUPPORT.md`, a pull request template, a manual `type:changelog` Issue Form, Dependabot for GitHub Actions, a `Validate` workflow (YAML syntax, documentation link integrity, placeholder-configuration checks), and a `Release` workflow. Replaced hardcoded placeholder values in `project-auto-add.yml` with repository variables (`RESEARCH_PROJECT_URL`, `SOURCE_PROJECT_URL`). Scoped the QA Gate Enforcement checkbox count to the QA Gate section specifically, instead of the full issue body, to avoid miscounting checkbox-like text elsewhere in an entry. Added an optional AI-assisted research-scaffolding workflow, explicitly scoped to drafting only — verification and publication status remain human-owned.
- **Reason:** An audit of v2.0 found the framework's rules were sound but several operational pieces were either unrealized (Projects boards were setup instructions, not repository state), fragile (regex-based QA parsing over the entire issue body), or simply absent (no license, no governance files, no release process).
- **Impact:** The repository now matches what its own documentation claims: a working, enforced, versioned system rather than a rulebook with some unfinished wiring.

### v2.0 — Full architecture redesign (this repository)
- **Section:** Everything.
- **Change:** Established the current structure — `docs/` as the single Philosophy & Standards layer with one canonical page per rule, Issue Forms + Projects as the Research Database and Source Reliability Database, and Actions enforcing the QA Gate and changelog process instead of relying on manual discipline.
- **Reason:** The prior structure was flat, undifferentiated documentation with duplicated rules, an internally inconsistent evidence taxonomy, and no persisted research history, source-reliability tracking, or post-publication review.
- **Impact:** One canonical page per rule; Issues + Projects as a queryable Research Database and Source Reliability Database; Actions enforcing the QA Gate instead of relying on the honor system. See `SETUP.md` §1 for the full rationale behind each structural decision.

### v1.2
- **Section:** Visual Assets.
- **Change:** Visual retrieval became mandatory whenever primary or official visuals are available. Recommending a chart is no longer sufficient.
- **Reason:** Readers should be able to verify important claims directly.
- **Impact:** Research now includes visual evidence retrieval as a standard workflow step.

### v1.1
- **Section:** Writing Rules.
- **Change:** Single standalone tweets became the default output. Threads only after a genuine attempt to fit the content into one tweet, or when explicitly requested.
- **Reason:** Prevent unnecessary threads; force concise communication.
- **Impact:** Every research cycle now begins by optimizing for one standalone tweet.

### v1.0 — Initial operating framework
Included: Objective, Research Workflow, Evidence Framework, On-Chain Verification, Mechanism Framework, Publication Standards, Content Rules, Writing Rules, Visual Assets, Verification Discipline, Quality Assurance.
