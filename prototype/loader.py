"""
loader.py — Step 1: Loading the knowledge objects.

Walks the same folders ARCHITECTURE.md defines as the knowledge layer,
parses each object's YAML frontmatter + Markdown body, and returns a flat
list of plain dicts. This is the only module that knows about the
repository's folder layout — every other module works with the dicts this
one produces, so if the folder layout ever changes, only this file changes.

Deliberately NOT reading MANIFEST.jsonl as the source of truth here: the
manifest is a *derived* index (see /MANIFEST.jsonl and its generation in
the v2.2 migration), and a loader that re-parses the actual files is the
one thing that can never drift from what's really on disk. build_index.py
regenerates the manifest-equivalent data as a side effect of indexing.
"""

import os
import re
import glob
import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.S)

# Same set of globs as ARCHITECTURE.md §1/§3 — the knowledge layer only.
# OBJECTIVE.md and GLOSSARY.md are root-level "meta"/"reference" objects,
# included for completeness since a query like "what's the mission" should
# still be answerable.
OBJECT_GLOBS = [
    "OBJECTIVE.md",
    "GLOSSARY.md",
    "rules/*.md",
    "frameworks/*.md",
    "playbooks/*.md",
    "checklists/*.md",
    "prompts/*.md",
    "tools/**/*.md",
    "sources/**/*.md",
    "research/**/*.md",
    "examples/*.md",
]


def load_objects(repo_root):
    """Return a list of dicts, one per knowledge object.

    Each dict has every frontmatter field plus:
      - _body: the Markdown body (frontmatter stripped)
      - _path: repo-root-relative path with a leading "/" (matches the
        convention ARCHITECTURE.md §2 defines for cross-references)
    README.md files inside each category folder are skipped — they're
    category documentation, not knowledge objects (no frontmatter, by
    design — see e.g. /rules/README.md).
    """
    objects = []
    seen_paths = set()

    for pattern in OBJECT_GLOBS:
        for path in glob.glob(os.path.join(repo_root, pattern), recursive=True):
            if os.path.basename(path) == "README.md":
                continue
            if path in seen_paths:
                continue
            seen_paths.add(path)

            with open(path, encoding="utf-8") as f:
                text = f.read()

            match = FRONTMATTER_RE.match(text)
            if not match:
                # A file under a knowledge-layer folder with no frontmatter
                # is a data-quality problem, not a silent skip — surface it.
                print(f"WARNING: {path} has no parseable frontmatter, skipping")
                continue

            frontmatter_yaml, body = match.group(1), match.group(2)
            try:
                fm = yaml.safe_load(frontmatter_yaml) or {}
            except yaml.YAMLError as e:
                print(f"WARNING: {path} frontmatter failed to parse: {e}")
                continue

            rel_path = os.path.relpath(path, repo_root).replace(os.sep, "/")
            fm["_body"] = body.strip()
            fm["_path"] = "/" + rel_path
            objects.append(fm)

    return objects


if __name__ == "__main__":
    import sys
    import json

    repo_root = sys.argv[1] if len(sys.argv) > 1 else ".."
    objs = load_objects(repo_root)
    print(f"Loaded {len(objs)} knowledge objects from {repo_root}\n")
    by_type = {}
    for o in objs:
        by_type.setdefault(o.get("type", "?"), 0)
        by_type[o.get("type", "?")] += 1
    print(json.dumps(by_type, indent=2))
