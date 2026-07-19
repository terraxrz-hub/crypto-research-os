# Crypto Research OS

A GitHub-native **AI Research Operating System** for crypto research, verification, and publication — typed knowledge objects instead of flat prose, database-backed history instead of static docs, and a QA gate enforced by automation rather than trusted on the honor system.

GitHub is the platform of record: Issues are the live database, Projects is the reporting layer, Actions is the enforcement layer, and the **knowledge layer** below is the versioned, retrieval-ready source of truth — designed to be a long-term knowledge base for an AI agent, not just documentation for a human. See [ARCHITECTURE.md](ARCHITECTURE.md) for the full design (object taxonomy, retrieval strategy, knowledge graph, scalability to 5,000+ objects), [MIGRATION.md](MIGRATION.md) for how the prior flat structure was cut over, [SETUP.md](SETUP.md) for first-time repository setup, and [CONTRIBUTING.md](CONTRIBUTING.md) before changing any knowledge object.

## Knowledge layer

```
crypto-research-os
├── OBJECTIVE.md                 — the one static "why" page everything else operationalizes
├── GLOSSARY.md                  — single definitions, referenced on first use everywhere
├── rules/                       — atomic, checkable constraints (RULE-001 .. 003)
├── frameworks/                  — multi-criteria reasoning models (FRAMEWORK-001 .. 004)
├── playbooks/                   — ordered procedures (PLAYBOOK-0001 .. 0002)
├── checklists/                  — enumerable, machine-checkable gates (CHECKLIST-001 — QA Gate)
├── tools/                       — queryable external platforms (TOOL-00001 .. , sharded by id)
├── sources/                     — tracked evidence-reliability records (SOURCE-000001 .. , sharded)
├── research/                    — graduated, finalized findings (empty until Issues graduate — see ARCHITECTURE.md §8)
├── examples/                    — worked, illustrative applications (EXAMPLE-00001 .. )
├── prompts/                     — thin trigger text, one per Playbook phase (PROMPT-0001 .. 0007)
├── _schemas/                    — JSON-Schema contract per object type
├── MANIFEST.jsonl               — flat index of every knowledge object (id, type, tags, related, path)
├── ARCHITECTURE.md              — full design rationale
├── MIGRATION.md                 — old docs/ → new object-type mapping
├── scripts/
│   └── apply-branch-protection.sh
├── .github/
│   ├── ISSUE_TEMPLATE/           — Operating layer: Research, Source Reliability, Correction, Changelog forms
│   ├── workflows/                 — QA gate enforcement, changelog automation, project sync, review reminders, releases, validation, AI-assisted drafting
│   ├── labels.yml, dependabot.yml, CODEOWNERS, PULL_REQUEST_TEMPLATE.md, SECURITY.md, SUPPORT.md
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

Every file under `rules/`, `frameworks/`, `playbooks/`, `checklists/`, `tools/`, `sources/`, `research/`, `examples/`, and `prompts/` is a **knowledge object**: YAML frontmatter (id, type, status, version, tags, `related` graph edges, an embedding-ready `summary`) plus a body under ~800 words. See [ARCHITECTURE.md §3](ARCHITECTURE.md#3-knowledge-objects) for the full schema per type.

## The two live databases

GitHub Issues + Projects are the *operating* layer — where research happens live, before it graduates into the static knowledge layer above:

- **Research Database** → every `type:research` Issue (via the **Research Entry** form), surfaced on a GitHub Projects (v2) board with custom fields (Evidence Tier, Publication Status, the six EV components). One row per story evaluated, including WAIT outcomes.
- **Source Reliability Database** → every `type:source` Issue (via the **Source Reliability Record** form), tracking a source's track record over time — the live counterpart to `/sources/`.
- **Changelog** → `type:changelog` Issues — auto-opened whenever `rules/`, `frameworks/`, `playbooks/`, or `checklists/` changes on `main`, or opened manually via the **Changelog Entry** form for anything else worth recording.
- **Corrections** → `type:correction` Issues, linked back to the original research entry.

## Daily use

1. Open a new **Research Entry** issue (Issues → New Issue).
2. Work the phases in [Daily Workflow](/playbooks/PLAYBOOK-0002-daily-workflow.md) — each maps to a field on the form.
3. Tick the 10 QA Gate checkboxes as you satisfy them.
4. Apply the `status:PASS` (or `status:PASS-WITH-LIMITATIONS`) label. **QA Gate Enforcement** will bounce it back if the boxes aren't all checked.
5. Publish. Come back later and fill in **Outcome** — or let the weekly review reminder nudge you.

## AI integration prototype

[`/prototype/`](prototype/) is a working, minimal RAG pipeline validating this architecture end-to-end (loader → chunker/indexer → retriever → LLM) against the real knowledge objects above — see [`prototype/README.md`](prototype/README.md) for how to run it and what it found. This is a reference implementation, not part of the knowledge taxonomy itself.

## Why AI-first, GitHub-native

Every fact the framework relies on — a rule, a reasoning model, a procedure, a source's track record — is a single, typed, cross-referenced object with retrieval metadata, so it can be indexed into a vector database, retrieved by an AI agent, or traversed as a knowledge graph without the repository's structure changing at all. GitHub's own primitives (Issues, Projects, Actions, labels, branch protection) remain the live operating layer on top. See [ARCHITECTURE.md](ARCHITECTURE.md) for exactly how each piece is designed to support both a human contributor today and a retrieval-augmented AI agent tomorrow.
