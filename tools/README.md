# Tools

**What belongs here:** named external platforms, APIs, or interfaces an agent or researcher *queries* — block explorers, analytics dashboards, security-audit firms. A Tool object documents *how to use* something (URL, access method, category, default reliability tier when it's the sole cited source).

**Why this category exists separate from Sources:** a Tool and a Source can refer to the same named platform (e.g. Arkham Intelligence is both `TOOL-00001` and `SOURCE-000001`) but answer different questions. Tool answers "how do I query this / what does it return / what tier does its output default to." Source answers "has this specific named origin of a claim been right before, and when." Splitting them means an agent doing live lookups filters `type:tool`, while an agent grading a past claim's reliability filters `type:source` — without either object being bloated with the other's fields.

**Naming & sharding:** `TOOL-#####` (5-digit ID, room for 2,000+), sharded into subfolders by the first two ID digits (`tools/00/`, `tools/01/`, ...) once any shard exceeds ~500 files — see `/ARCHITECTURE.md` §7 for the scaling rationale.

**Current objects (seed set, demonstrating the pattern):** [TOOL-00001](00/TOOL-00001-arkham-intelligence.md), [TOOL-00002](00/TOOL-00002-glassnode.md), [TOOL-00003](00/TOOL-00003-certik.md), [TOOL-00004](00/TOOL-00004-etherscan.md).

**Schema:** [`/_schemas/tool.schema.yaml`](../_schemas/tool.schema.yaml).
