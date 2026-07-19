# Prompts

**What belongs here:** thin, reusable triggers — each Prompt invokes exactly one Rule/Framework/Playbook phase by reference; none restate the standard they invoke. If a new prompt would do nearly the same thing as an existing one, that existing prompt needs a parameter, not a sibling — this was the exact duplication problem the framework's first redesign resolved, and the discipline still applies at this granularity.

**Why this category exists separate from Playbooks:** a Playbook describes *what a human or agent does* at each phase; a Prompt is the literal, copy-pasteable (or agent-callable) text used to do it. One Playbook phase may have zero, one, or several Prompts depending on how many distinct ways it gets invoked (Phase 4 — Build the Draft — has two: [PROMPT-0004](PROMPT-0004-tweet-writer.md) for the default tweet and [PROMPT-0005](PROMPT-0005-thread-builder.md) for the thread exception).

**Current objects:** [PROMPT-0001](PROMPT-0001-market-scan.md) through [PROMPT-0007](PROMPT-0007-final-qa.md), one per workflow step in [Daily Workflow](../playbooks/PLAYBOOK-0002-daily-workflow.md).

When filing an actual research entry, use the `research-entry` GitHub Issue Form instead of running these ad hoc — it embeds the same steps as structured fields feeding the Research Database.

**Schema:** [`/_schemas/prompt.schema.yaml`](../_schemas/prompt.schema.yaml).
