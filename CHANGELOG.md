# Changelog

Every meaningful change to the operating framework is recorded here or as a `type:changelog` GitHub Issue — preserving the reasoning behind each change so rules evolve deliberately, not accidentally.

**From V2 onward:** changelog entries live as Issues labeled `type:changelog` (auto-opened by the **Changelog Automation** workflow whenever `docs/` changes on `main`), with structured fields: Date, Version, Section Changed, Change, Reason, Impact. This file preserves the V1 history so nothing is lost, and is not appended to by hand going forward — check the `type:changelog` label for the live log.

## Version History (carried over from V1)

### v1.0 — Initial operating framework
Included: Objective, Research Workflow, Evidence Framework, On-Chain Verification, Mechanism Framework, Publication Standards, Content Rules, Writing Rules, Visual Assets, Verification Discipline, Quality Assurance.

### v1.1
- **Section:** Writing Rules
- **Change:** Single standalone tweets became the default output. Threads only after a genuine attempt to fit the content into one tweet, or when explicitly requested.
- **Reason:** Prevent unnecessary threads; force concise communication.
- **Impact:** Every research cycle now begins by optimizing for one standalone tweet.

### v1.2
- **Section:** Visual Assets
- **Change:** Visual retrieval became mandatory whenever primary or official visuals are available. Recommending a chart is no longer sufficient.
- **Reason:** Readers should verify important claims directly.
- **Impact:** Research now includes visual evidence retrieval as a standard workflow step.

### v2.0 — Full architecture redesign (this repository)
- **Section:** Everything.
- **Change:** Migrated from 15 flat Notion pages with no hierarchy, no databases, and heavy rule duplication to a database-backed GitHub system — see [SETUP.md](SETUP.md) for the full migration plan and rationale.
- **Reason:** V1 had one direct internal contradiction (Evidence Framework's own two sections disagreed), three non-identical trust taxonomies, drifted duplicate rule copies, an empty canonical Writing page cited by seven others, and no research history, source reliability tracking, or post-publication review.
- **Impact:** One canonical page per rule; Issues + Projects as a queryable Research Database and Source Reliability Database; Actions enforcing the QA Gate instead of relying on the honor system.
