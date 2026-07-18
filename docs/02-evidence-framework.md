# Evidence Framework (canonical, single taxonomy)

> **This is the only tier list in the system.** [Visual Assets](04-visual-assets.md), [Sources & Research Priority](01-sources-and-priority.md), [On-Chain Verification](05-on-chain-verification.md), and [Decision Framework](06-decision-framework.md) all reference this page instead of restating it. If you find a tier definition anywhere else, that's drift — delete it and link here instead.

Every claim is classified by the strength of its evidence chain — never by how many people repeated it. Ten articles citing one source is one piece of evidence, not ten.

## The Tiers

| Tier | Name | Confidence | What qualifies |
|---|---|---|---|
| 1 | **Primary Evidence** | High / Very High | Court filings, government/regulatory documents, official company statements, blockchain explorer records, official GitHub repos, technical documentation — the original record itself. |
| 2 | **Independent Confirmation** | High | Two or more *unrelated* parties, using *different methodologies*, independently reach the same conclusion by directly examining the primary artifact. Covers both "two security firms find the same exploit" and "two analytics platforms independently reach the same on-chain conclusion via different methods." A **single** named technical auditor (CertiK, SlowMist, Trail of Bits, OpenZeppelin, Blockaid) directly examining code also lands here — they're examining the artifact itself, not interpreting someone else's interpretation of it. |
| 3 | **Verified Through Trusted Intermediaries** | Medium–High | A single trusted analytics platform (Arkham, Glassnode, CryptoQuant, Nansen, DeFiLlama, Token Terminal, Dune, SoSoValue, Lookonchain) interpreting raw data, not independently cross-traced. Useful and often reliable — but always attribute explicitly ("According to Arkham…"). |
| 4 | **Corroborated Secondary Reporting** | Medium | Multiple media outlets reporting the same underlying source. Ten outlets repeating one Arkham post is still Tier 3 evidence wearing ten bylines — the *underlying* tier doesn't rise just because it got quoted a lot. |
| 5 | **Single-Source Reporting** | Low | One news report, not yet corroborated or traced upstream. Useful for *discovery*, not for publication as evidence. |
| 6 | **Unverified** | Low / WAIT | Could not be confirmed or disproven. Unverified ≠ false — it means the evidence is insufficient. |
| 7 | **Verified False** | — | Investigated and disproven by reliable evidence. |

**Why Tier 3 sits above Tier 4:** a named, accountable analytics provider directly examining data is stronger evidence than an arbitrary number of outlets repeating one unnamed original source. (Previously the numbered list and the confidence-rules text disagreed on this — this ordering is the resolved, authoritative version.)

## Source → Tier reference (single copy — do not re-derive elsewhere)

| Source type | Named examples | Tier |
|---|---|---|
| Government / regulatory / court records | — | 1 |
| Blockchain explorers | Etherscan, Arbiscan, Basescan, Solscan, Tronscan, Blockstream, mempool.space | 1 |
| Independent technical auditors | CertiK, SlowMist, Trail of Bits, OpenZeppelin, Blockaid | 2 |
| Trusted analytics providers | Arkham, Glassnode, CryptoQuant, Nansen, DeFiLlama, Token Terminal, Dune, SoSoValue, Lookonchain, Kaiko, Messari | 3 |
| High-quality news orgs | CoinDesk, The Block, Bloomberg, Reuters, Financial Times, Nikkei, NHK | 4–5 (discovery + corroboration only) |
| Social media | X/Twitter, Telegram, Discord, Reddit | Discovery only — never an evidence tier on its own |

If a source isn't on this list, classify it by what it *is* (original record → Tier 1, independent direct examination → Tier 2, interpretive platform → Tier 3, media → Tier 4/5) and add it here in the same PR — see [Changelog](../CHANGELOG.md).

## Resolved ambiguous cases

**A source with a good track record, but this specific claim is unverifiable.** Track record never upgrades the tier of an individual claim. It's tracked separately in the Source Reliability Database (`type:source` issues) and may be mentioned as context in the Confidence Level notes, but the Evidence Tier is always assigned by what was verified *this time*.

**A primary document whose authenticity is itself disputed.** Do not classify as Tier 1 until authenticity is confirmed (see the [Primary Document Verification Protocol](05-on-chain-verification.md)). Classify as **"Tier 1 — Contested"** or fall back to a **mixed evidence chain**, and say explicitly what's unresolved.

**Two trusted analytics platforms independently reach the same on-chain conclusion via different methods (e.g. Glassnode and CryptoQuant agree).** This is **Tier 2 (Independent Confirmation)**, not Tier 3 — it's structurally identical to two security firms finding the same exploit.

## Confidence Rules

- Confidence follows the evidence chain, never the repetition count.
- Never raise confidence because many articles repeat the same story.
- General mapping: Tier 1 → High/Very High · Tier 2 → High · Tier 3 → Medium–High · Tier 4 → Medium · Tier 5–6 → Low/WAIT.

See [Glossary](glossary.md) for term definitions and [Decision Framework](06-decision-framework.md) / [Publication Standard](07-publication-standard.md) for how this tier feeds a go/no-go call.
