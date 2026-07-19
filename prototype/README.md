# AI Integration Prototype

This is the first integration layer that lets an AI system consume the [v2.2 knowledge architecture](../ARCHITECTURE.md) — a minimal, working, end-to-end RAG pipeline validating the design rather than re-theorizing it. Six files, one external dependency (`pyyaml`), no vector database or API key required to run.

```
User query
   │
   ▼
retriever.py  ──►  [1] metadata filter (type/tags/status)
                    [2] semantic search (TF-IDF cosine similarity)
                    [3] ranking (similarity × type-priority × source_of_truth)
                    [4] graph expansion (1-hop via `related`/`depends_on`/...)
   │
   ▼
rag.py  ──►  assemble context from retrieved knowledge objects
   │
   ▼
llm.py  ──►  Claude (if ANTHROPIC_API_KEY set) — else extractive fallback
   │
   ▼
Response, every claim traceable to a cited object id
```

## Files

| File | Maps to ARCHITECTURE.md | What it does |
|---|---|---|
| `loader.py` | — (repository access) | Parses every knowledge object's frontmatter + body from the actual folder structure. |
| `indexer.py` | §2 (chunking), §4 (index prep) | Splits each object into a summary chunk + one chunk per `##` section; fits a TF-IDF index; persists both to `index/`. |
| `retriever.py` | §4 (retrieval strategy) | The four-stage pipeline above, implemented exactly as specified — filter → search → rank → expand. |
| `llm.py` | §6 (future AI integration) | ~50-line stdlib wrapper around the Anthropic Messages API. No SDK dependency. |
| `rag.py` | §5 (RAG prototype) | Ties retrieval + generation together; falls back to an extractive answer with no key. |
| `demo.py` | §6 (end-to-end query) | Runs three real queries through the full pipeline and prints every stage. |

## Running it

```bash
cd prototype
pip install -r requirements.txt

# Step 1: build the index (chunks + TF-IDF) from the repository
python3 indexer.py .. index

# Step 2: ask a question
python3 rag.py "What does the QA gate require before a story can PASS?"

# Or run the full three-query demo with every stage printed
python3 demo.py
```

To get real generated answers instead of the extractive fallback:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 rag.py "How do I classify evidence from a single analytics platform?"
```

Nothing else changes — the retrieval, ranking, and context assembly are identical either way; only the final synthesis step differs. This was a deliberate design choice so the prototype is fully runnable and inspectable without credentials, per "keep the implementation simple."

## Actual results (from `demo_transcript.txt`, this repository's real content, no key set)

Query: *"What does the QA gate require before a story can PASS?"*
```
RETRIEVER — direct matches:
  [0.442] PLAYBOOK-0002 (PLAYBOOK-0002::section::phase-6-qa-gate)
  [0.377] CHECKLIST-001 (CHECKLIST-001::summary)
  [0.356] FRAMEWORK-004 (FRAMEWORK-004::section::checklist-before-drafting)
  [0.341] PROMPT-0007   (PROMPT-0007::section::final-qa)
  [0.307] EXAMPLE-00001 (EXAMPLE-00001::section::qa-gate-check-selected)
RETRIEVER — graph-expanded context:
  PLAYBOOK-0001, FRAMEWORK-003, FRAMEWORK-001, RULE-002, RULE-003
```
Query: *"What should I do if a story is breaking news and I can't fully verify it in time?"*
```
RETRIEVER — direct matches:
  [0.398] FRAMEWORK-003 (FRAMEWORK-003::section::time-boxing-escalation-path)
  [0.366] PLAYBOOK-0001 (PLAYBOOK-0001::section::time-pressure)
  ...
```
Both land exactly on the right section of the right object — see `demo_transcript.txt` for the full run of all three queries, including the assembled context block and final response.

## Design decisions (and why they're deliberately minimal)

- **TF-IDF instead of real embeddings.** At 25 objects / 106 chunks, TF-IDF cosine similarity already produces correct top-k results (see above) with zero external services, zero API cost, and zero setup. `indexer.TfidfIndex` exposes the same `.query(text, top_k, filter_fn)` interface a real vector DB client would — swapping it is a one-class change, not a pipeline rewrite (see "Swapping in real embeddings" below). Building a real embedding pipeline before there's enough content for TF-IDF to actually fall short would be exactly the premature optimization this task asked to avoid.
- **JSONL files instead of a real vector database.** `index/chunks.jsonl`, `objects.jsonl`, and `tfidf.json` are the entire "database" — human-readable, diffable, greppable. At the §7 target scale (5,000+ Research, 10,000+ Sources) this stops being sufficient; that migration is described below, not built now, because it isn't needed yet.
- **No SDK dependency for the LLM call.** `llm.py` is ~50 lines of `urllib`. Easier to audit than a dependency, and avoids pinning to an SDK version for something this small.
- **Extractive fallback, not a mocked LLM response.** A fake generated-sounding answer would misrepresent what the system actually did. Showing the real retrieved chunks with a clear "no key set" label is more honest and, for evaluating retrieval quality specifically, arguably more useful than a generated paraphrase would be.

## Known limitations (real usage should surface more — this is a first pass)

- **TF-IDF is a keyword matcher, not a semantic one.** It found the right objects on all three demo queries because the framework's own vocabulary is fairly distinctive (e.g. "QA gate," "time-boxing"), but a paraphrase using none of the source vocabulary (e.g. "what's the deadline rule for fast-moving stories") would score worse than a real embedding model would. This is the single most likely place real usage will demand the upgrade described below.
- **No re-ranking model, no query expansion, no hybrid search.** Ranking is the simple formula in `retriever.py` (`similarity × type-priority × source_of_truth boost`) — deliberately, per ARCHITECTURE.md §4, but it hasn't been tuned against real query logs because none exist yet.
- **Graph expansion is unconditional 1-hop, not relevance-gated.** Every related id gets pulled in regardless of how tangential; at higher `related`-list fan-out (a well-connected Rule, say) this could dilute context. Fine at current scale (max fan-out observed: 5), worth revisiting once Research/Source volume grows.
- **No evaluation harness.** There's no labeled query set to measure retrieval precision/recall against — the "actual results" above are spot-checked by reading them, not scored. Worth building once there's a backlog of real queries to draw from.

## Swapping in real embeddings later (when usage justifies it)

Everything above `indexer.TfidfIndex` and below `retriever.retrieve()` is agnostic to how similarity is computed. To move to real embeddings:

1. Replace `TfidfIndex` with a client for whatever vector store is chosen (a hosted vector DB, or a local `sentence-transformers` + FAISS setup), exposing the same `.query(text, top_k, filter_fn)` shape.
2. In `build_index()`, replace the TF-IDF fit with a batch embedding call over the same chunk list `chunk_object()` already produces — the chunk boundaries don't change.
3. `retriever.py`, `rag.py`, `llm.py`, and `demo.py` need zero changes.

This is the seam ARCHITECTURE.md §6 described in advance ("nothing in the repository needs to change; embedding is a read-only batch job over existing files") — this prototype is the proof that seam is where the design says it is.
