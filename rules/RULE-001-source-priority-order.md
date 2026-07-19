---
id: RULE-001
type: rule
title: "Source Priority Order"
status: active
version: 1
tags: [sources, verification, priority]
related: [FRAMEWORK-001, PLAYBOOK-0001, PLAYBOOK-0002]
statement: >
  Research must move upward through a fixed five-level source hierarchy
  (primary > independent technical > trusted analytics > news > social),
  and evidence strength is judged by proximity to the original event, never
  by how many outlets repeat the same claim.
enforced_by: []
applies_to: [research, playbook]
summary: >
  Defines the search order for evidence (primary sources first, social media
  last) and three hard rules: ten articles citing one source are still one
  piece of evidence; always attribute non-independently-verified claims
  explicitly; research should always move upward toward the original event.
source_of_truth: true
---

# Sources & Research Priority

The quality of research depends on the quality of its sources. This framework prioritizes evidence by its **proximity to the original event** — not popularity, publication count, or speed. Multiple articles repeating the same claim never outweigh one authentic primary source.

This page governs *where to look and in what order*. For *how to classify what you find*, see the single tier table in [Evidence Framework](/frameworks/FRAMEWORK-001-evidence-tier-framework.md) — the source list there is canonical; this page just describes the search sequence.

## Search order

1. **Primary sources** — government publications, regulatory filings, court documents, official announcements, blockchain explorer records, official GitHub repos, technical documentation.
2. **Independent technical sources** — direct code/security examination (Blockaid, CertiK, SlowMist, Trail of Bits, OpenZeppelin).
3. **Trusted analytics providers** — when raw data is hard to interpret directly (Arkham, Glassnode, CryptoQuant, Nansen, DeFiLlama, Token Terminal, Dune, SoSoValue).
4. **High-quality news organizations** — to discover stories and add context (CoinDesk, The Block, Bloomberg, Reuters, Financial Times, Nikkei, NHK). News should *lead* research, not *end* it — always trace claims back upstream.
5. **Social media** — X, Telegram, Discord, Reddit. Lowest priority: valuable for discovering emerging stories, never sufficient as evidence alone.

## Rules

- **Source count rule:** ten articles citing one source are still one piece of evidence.
- **Attribution rule:** whenever a claim isn't independently verified, attribute it explicitly ("According to Arkham…", "Per Glassnode…"). Never let wording imply stronger verification than exists.
- **Direction rule:** research should move *upward* through this list whenever possible. The goal isn't just finding information — it's reaching the evidence closest to the original event.

When two sources disagree, the one closer to the original event wins.
