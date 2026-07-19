# Research

**What belongs here:** completed, published Research Entries — the permanent, indexable knowledge base an AI Retriever actually searches for "what have we found/concluded before." This is the file-based archive counterpart to the `type:research` GitHub Issue: research is *run* as a live Issue (see the `research-entry` form and [Daily Workflow](../playbooks/PLAYBOOK-0002-daily-workflow.md)), and *graduates* into a static Research object here once its Publication Status is finalized (PASS, PASS WITH LIMITATIONS, or a recorded WAIT worth keeping for pattern purposes).

**Why the split (live Issue vs. static object):** an Issue is mutable and optimized for in-progress collaboration (comments, label transitions, project board views); a Research object is immutable-once-published and optimized for embedding/retrieval (fixed content, stable ID, one clean chunk boundary). Keeping active work in Issues and only graduating finished work here means the vector index never has to re-embed a document that's still changing.

**Naming & sharding:** `RESEARCH-######` (6-digit ID, room for 5,000+), sharded per 1,000-ID range (`research/000001/`), mirroring `/sources/`.

**Current objects:** none yet — no entry has graduated from the GitHub Issues pipeline. See `/ARCHITECTURE.md` §8 for the graduation mechanism this repository is structured to support (not yet automated — see that section's note on scope).

**Schema:** [`/_schemas/research.schema.yaml`](../_schemas/research.schema.yaml).
