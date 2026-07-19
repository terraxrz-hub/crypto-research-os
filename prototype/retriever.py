"""
retriever.py — Step 2: building a simple retrieval pipeline.

Implements exactly the four-stage pipeline ARCHITECTURE.md §4 already
specified:

    query -> [1] metadata filter -> [2] semantic search (TF-IDF here,
    real embeddings later) -> [3] ranking -> [4] graph expansion -> results

Nothing here is specific to TF-IDF — stage 2 only calls `index.query(...)`,
so swapping indexer.TfidfIndex for a real vector DB client changes zero
lines in this file (see /prototype/README.md).
"""

import json
import os

# Type-priority weights, taken directly from ARCHITECTURE.md §4 step 3:
# "a Rule/Checklist should outrank a Research object even at equal
# similarity, since Research is a past application of the rule, not the
# rule itself." Frameworks/Playbooks sit in between; Prompts rank lowest
# since they're thin triggers, rarely the thing a query is actually about.
TYPE_PRIORITY = {
    "rule": 1.20,
    "checklist": 1.20,
    "framework": 1.10,
    "meta": 1.05,
    "playbook": 1.05,
    "reference": 1.00,
    "research": 1.00,
    "source": 0.95,
    "tool": 0.95,
    "example": 0.90,
    "prompt": 0.85,
}

SOURCE_OF_TRUTH_BOOST = 1.10


def _rank_score(similarity, chunk):
    score = similarity * TYPE_PRIORITY.get(chunk.get("type"), 1.0)
    if chunk.get("source_of_truth"):
        score *= SOURCE_OF_TRUTH_BOOST
    return score


def load_objects_by_id(index_dir):
    """Load index/objects.jsonl into an {id: object} dict for graph
    expansion and context assembly — avoids re-walking the filesystem on
    every query."""
    path = os.path.join(index_dir, "objects.jsonl")
    by_id = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            oid = obj.get("id")
            if oid:
                by_id[oid] = obj
    return by_id


def retrieve(index, query, objects_by_id, types=None, tags=None, top_k=5, expand=True):
    """Run the four-stage pipeline. Returns (ranked, expanded):
      - ranked:   top_k objects that matched the query directly, each with
                  {object_id, score, matched_chunk}
      - expanded: objects pulled in via a 1-hop graph traversal from the
                  ranked set's `related` (etc.) edges, not because they
                  matched the query text themselves
    """

    # --- Stage 1: metadata filter --------------------------------------
    def filt(chunk):
        if chunk.get("status") not in (None, "active"):
            return False
        if types and chunk.get("type") not in types:
            return False
        if tags and not (set(tags) & set(chunk.get("tags") or [])):
            return False
        return True

    # --- Stage 2: semantic search (within the filtered set) ------------
    # Over-fetch (top_k * 4 chunks) before collapsing to one best chunk per
    # object, since several chunks from the same object may all score.
    hits = index.query(query, top_k=top_k * 4, filter_fn=filt)

    # --- Stage 3: ranking (dedupe to one best chunk per object, rank) ---
    best_per_object = {}
    for similarity, chunk in hits:
        score = _rank_score(similarity, chunk)
        oid = chunk["object_id"]
        if oid not in best_per_object or score > best_per_object[oid]["score"]:
            best_per_object[oid] = {
                "object_id": oid,
                "score": round(score, 4),
                "similarity": round(similarity, 4),
                "matched_chunk": chunk["chunk_id"],
                "matched_text": chunk["text"],
            }

    ranked = sorted(best_per_object.values(), key=lambda r: -r["score"])[:top_k]
    result_ids = {r["object_id"] for r in ranked}

    # --- Stage 4: graph expansion (1-hop, per ARCHITECTURE.md §4 step 4) -
    expanded = []
    if expand:
        for r in ranked:
            obj = objects_by_id.get(r["object_id"], {})
            related_ids = set()
            for field in ("related", "depends_on", "enforced_by", "validates", "illustrates"):
                val = obj.get(field)
                if isinstance(val, list):
                    related_ids.update(x for x in val if isinstance(x, str))
                elif isinstance(val, str):
                    related_ids.add(val)

            for rid in related_ids:
                if rid in result_ids or rid not in objects_by_id:
                    continue
                target = objects_by_id[rid]
                if target.get("status") not in (None, "active"):
                    continue
                expanded.append({
                    "object_id": rid,
                    "reason": f"related to {r['object_id']} (matched \"{query[:40]}...\")"
                              if len(query) > 40 else f"related to {r['object_id']}",
                })
                result_ids.add(rid)

    return ranked, expanded


if __name__ == "__main__":
    import sys
    from indexer import TfidfIndex

    index_dir = sys.argv[1] if len(sys.argv) > 1 else "index"
    query = " ".join(sys.argv[2:]) or "what does the QA gate require before PASS"

    chunks = [json.loads(l) for l in open(os.path.join(index_dir, "chunks.jsonl"), encoding="utf-8")]
    idf = json.load(open(os.path.join(index_dir, "tfidf.json"), encoding="utf-8"))["idf"]
    index = TfidfIndex(chunks, idf=idf)
    objects_by_id = load_objects_by_id(index_dir)

    ranked, expanded = retrieve(index, query, objects_by_id, top_k=5)

    print(f"Query: {query!r}\n")
    print("Ranked (direct matches):")
    for r in ranked:
        print(f"  [{r['score']:.3f}] {r['object_id']:15s} via {r['matched_chunk']}")
    print("\nExpanded (1-hop graph neighbors):")
    for e in expanded:
        print(f"  {e['object_id']:15s} — {e['reason']}")
