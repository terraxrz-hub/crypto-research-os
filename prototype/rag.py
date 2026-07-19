"""
rag.py — Step 5 & 6: the minimal RAG prototype and the end-to-end query
demo (User -> Retriever -> Knowledge Objects -> LLM -> Response).

`answer()` is the single entry point: it runs retriever.retrieve(), builds
a context block from the results, and either calls the real LLM (if
ANTHROPIC_API_KEY is set) or falls back to a purely extractive answer
built directly from the retrieved chunks. The fallback exists so this
prototype demonstrates the full pipeline even with zero external
dependencies or credentials — the only thing that changes with a key
present is *who* writes the final sentence, not what was retrieved.
"""

import json
import os

from indexer import TfidfIndex
from retriever import retrieve, load_objects_by_id
from llm import call_claude

SYSTEM_PROMPT = """You are the retrieval assistant for the Crypto Research OS knowledge base.

Answer ONLY using the knowledge objects provided in the context below. Every claim you make must be traceable to one of them — cite the object id in square brackets after each claim, e.g. [RULE-003].

If the provided context does not fully answer the question, say so explicitly rather than filling the gap from general knowledge — this mirrors the framework's own WAIT principle [RULE-003]: an incomplete but honest answer beats a confident but unsupported one.

Be concise. Do not repeat the full text of an object; synthesize."""


def _build_context(ranked, expanded, objects_by_id):
    """Turn retrieval results into the context block passed to the LLM (or
    used directly by the extractive fallback)."""
    lines = []

    lines.append("## Directly matched objects")
    for r in ranked:
        obj = objects_by_id.get(r["object_id"], {})
        lines.append(
            f"\n### [{r['object_id']}] {obj.get('title', '')} (type: {obj.get('type')}, "
            f"path: {obj.get('_path')})"
        )
        lines.append(f"Matched excerpt: {r['matched_text']}")
        if obj.get("summary"):
            lines.append(f"Summary: {obj['summary'].strip()}")

    if expanded:
        lines.append("\n## Related objects (pulled in via graph expansion, not direct text match)")
        for e in expanded:
            obj = objects_by_id.get(e["object_id"], {})
            lines.append(
                f"\n### [{e['object_id']}] {obj.get('title', '')} (type: {obj.get('type')}) — {e['reason']}"
            )
            if obj.get("summary"):
                lines.append(f"Summary: {obj['summary'].strip()}")

    return "\n".join(lines)


def _extractive_fallback(query, ranked, objects_by_id):
    """No API key available — build a readable answer directly from the
    top matched chunks instead of calling an LLM. Not a generated answer;
    labeled as such so it's never mistaken for one."""
    lines = [
        f'[No ANTHROPIC_API_KEY set — showing extractive results instead of a generated answer for: "{query}"]',
        "",
    ]
    for r in ranked:
        obj = objects_by_id.get(r["object_id"], {})
        lines.append(f"[{r['object_id']}] {obj.get('title','')} — {r['matched_text']}")
    return "\n".join(lines)


def answer(query, index_dir="index", types=None, tags=None, top_k=5, verbose=True):
    chunks = [json.loads(l) for l in open(os.path.join(index_dir, "chunks.jsonl"), encoding="utf-8")]
    idf = json.load(open(os.path.join(index_dir, "tfidf.json"), encoding="utf-8"))["idf"]
    index = TfidfIndex(chunks, idf=idf)
    objects_by_id = load_objects_by_id(index_dir)

    ranked, expanded = retrieve(index, query, objects_by_id, types=types, tags=tags, top_k=top_k)

    if verbose:
        print(f"USER QUERY: {query}\n")
        print("RETRIEVER — direct matches:")
        for r in ranked:
            print(f"  [{r['score']:.3f}] {r['object_id']} ({r['matched_chunk']})")
        print("RETRIEVER — graph-expanded context:")
        for e in expanded:
            print(f"  {e['object_id']} — {e['reason']}")
        print()

    context = _build_context(ranked, expanded, objects_by_id)

    llm_response = call_claude(
        prompt=f"Question: {query}\n\nContext:\n{context}",
        system=SYSTEM_PROMPT,
    )

    if llm_response is not None:
        final_answer = llm_response
        mode = "generated"
    else:
        final_answer = _extractive_fallback(query, ranked, objects_by_id)
        mode = "extractive-fallback"

    return {
        "query": query,
        "ranked": ranked,
        "expanded": expanded,
        "context": context,
        "mode": mode,
        "answer": final_answer,
    }


if __name__ == "__main__":
    import sys

    query = " ".join(sys.argv[1:]) or "What does the QA gate require before a story can PASS?"
    result = answer(query)
    print("=" * 70)
    print(f"RESPONSE ({result['mode']}):\n")
    print(result["answer"])
