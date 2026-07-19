"""
indexer.py — Steps 3 & 4: preparing the repository for embeddings, and the
indexing process.

Two things live here:

1. `chunk_object()` — implements the chunk boundaries ARCHITECTURE.md §2
   already specified: one "summary" chunk (the frontmatter `summary` field)
   plus one "section" chunk per `##` heading in the body. This is the exact
   unit that would get embedded by a real embedding model — nothing about
   this changes when TF-IDF below is swapped for real embeddings later.

2. `TfidfIndex` — a small, dependency-free stand-in for a real embedding
   model. It turns each chunk's text into a sparse term-frequency /
   inverse-document-frequency vector and answers nearest-neighbor queries
   by cosine similarity. This is deliberately NOT a neural embedding: at
   25 objects / ~60 chunks, TF-IDF already gives sensible top-k results,
   needs zero external services or API keys, and keeps the prototype
   runnable end-to-end offline — matching "keep it simple, avoid premature
   optimization." See /prototype/README.md "Swapping in real embeddings"
   for exactly what changes (one class, same interface) when that's
   warranted by real usage.

Persistence: `build_index()` writes two flat files under index/:
  - chunks.jsonl  — one JSON object per chunk (text + metadata), human-
    readable, diffable, and the natural ingestion format for a real vector
    DB later (e.g. `for line in chunks.jsonl: vector_db.upsert(...)`).
  - tfidf.json    — the fitted IDF table, so a query-time process doesn't
    need to re-scan the repo just to answer one question.
"""

import os
import re
import json
import math
import datetime
from collections import Counter


def _json_default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

SECTION_SPLIT_RE = re.compile(r"\n(?=## )")
HEADER_RE = re.compile(r"^##\s+(.*)")
TOKEN_RE = re.compile(r"[a-z0-9]+")

# Fields (beyond the common schema) that carry graph edges — collected here
# so retriever.py's graph-expansion step (ARCHITECTURE.md §4 step 4) has a
# single place to look them up regardless of object type.
RELATIONSHIP_FIELDS = [
    "related", "depends_on", "enforced_by", "validates",
    "illustrates", "applies_to", "sources_cited", "tools_used", "tool_ref",
]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:50]


def tokenize(text):
    return TOKEN_RE.findall(text.lower())


def chunk_object(obj):
    """Return a list of chunk dicts for one knowledge object."""
    oid = obj.get("id")
    if not oid:
        return []

    base_meta = {
        "object_id": oid,
        "type": obj.get("type"),
        "title": obj.get("title"),
        "status": obj.get("status", "active"),
        "tags": obj.get("tags") or [],
        "source_of_truth": bool(obj.get("source_of_truth", False)),
        "path": obj.get("_path"),
        "related": sorted({
            rid
            for field in RELATIONSHIP_FIELDS
            for rid in (obj.get(field) or (
                [obj.get(field)] if isinstance(obj.get(field), str) else []
            ))
            if isinstance(rid, str)
        }),
    }

    chunks = []

    summary = (obj.get("summary") or "").strip()
    if summary:
        chunks.append({
            "chunk_id": f"{oid}::summary",
            "level": "summary",
            "text": summary,
            **base_meta,
        })

    body = obj.get("_body", "")
    for section in SECTION_SPLIT_RE.split(body):
        section = section.strip()
        if not section:
            continue
        header_match = HEADER_RE.match(section)
        header = header_match.group(1) if header_match else (obj.get("title") or "body")
        chunks.append({
            "chunk_id": f"{oid}::section::{slugify(header)}",
            "level": "section",
            "section_title": header,
            "text": section,
            **base_meta,
        })

    return chunks


class TfidfIndex:
    """Minimal TF-IDF vector index with cosine-similarity search.

    Interface intentionally mirrors what a real vector DB client looks
    like (`.query(text, top_k, filter_fn)`), so retriever.py doesn't need
    to change when this class is swapped for a real one.
    """

    def __init__(self, chunks, idf=None):
        self.chunks = chunks
        self._doc_tokens = [tokenize(c["text"]) for c in chunks]

        if idf is None:
            df = Counter()
            for toks in self._doc_tokens:
                for t in set(toks):
                    df[t] += 1
            n = len(chunks)
            self.idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items()}
        else:
            self.idf = idf

        self._doc_vecs = [self._vectorize(toks) for toks in self._doc_tokens]
        self._doc_norms = [
            math.sqrt(sum(v * v for v in vec.values())) or 1e-9
            for vec in self._doc_vecs
        ]

    def _vectorize(self, tokens):
        tf = Counter(tokens)
        return {t: c * self.idf[t] for t, c in tf.items() if t in self.idf}

    def query(self, text, top_k=10, filter_fn=None):
        q_vec = self._vectorize(tokenize(text))
        q_norm = math.sqrt(sum(v * v for v in q_vec.values())) or 1e-9

        scored = []
        for i, chunk in enumerate(self.chunks):
            if filter_fn and not filter_fn(chunk):
                continue
            vec = self._doc_vecs[i]
            dot = sum(w * vec.get(t, 0.0) for t, w in q_vec.items())
            sim = dot / (q_norm * self._doc_norms[i])
            if sim > 0:
                scored.append((sim, chunk))

        scored.sort(key=lambda x: -x[0])
        return scored[:top_k]


def build_index(repo_root, index_dir):
    """Load objects, chunk them, fit the TF-IDF index, and persist both."""
    from loader import load_objects

    objects = load_objects(repo_root)
    chunks = [c for obj in objects for c in chunk_object(obj)]

    index = TfidfIndex(chunks)

    os.makedirs(index_dir, exist_ok=True)

    with open(os.path.join(index_dir, "chunks.jsonl"), "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False, default=_json_default) + "\n")

    with open(os.path.join(index_dir, "tfidf.json"), "w", encoding="utf-8") as f:
        json.dump({"idf": index.idf}, f)

    # objects.jsonl: the full parsed objects (incl. _body), keyed by id —
    # what the RAG layer reads to assemble full context, and what
    # graph-expansion (retriever.py) reads to resolve a related id to a
    # real object without re-walking the filesystem.
    with open(os.path.join(index_dir, "objects.jsonl"), "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(json.dumps(obj, ensure_ascii=False, default=_json_default) + "\n")

    return objects, chunks, index


if __name__ == "__main__":
    import sys

    repo_root = sys.argv[1] if len(sys.argv) > 1 else ".."
    index_dir = sys.argv[2] if len(sys.argv) > 2 else "index"

    objects, chunks, index = build_index(repo_root, index_dir)
    print(f"Indexed {len(objects)} objects into {len(chunks)} chunks.")
    print(f"Vocabulary size: {len(index.idf)} terms.")
    print(f"Wrote {index_dir}/chunks.jsonl, {index_dir}/tfidf.json, {index_dir}/objects.jsonl")
