# On-Chain Verification

## Explorer-first rule

For every blockchain-related claim, attempt to verify it directly from the blockchain before relying on third-party reports.

**Verification priority:** wallet address → transaction hash → block height → blockchain explorer record (Etherscan, Arbiscan, Basescan, Solscan, Tronscan, Blockstream, mempool.space, etc.).

## If primary verification isn't possible

If you cannot retrieve the transaction or explorer record yourself, do not describe the claim as independently verified. Instead:

- Explain exactly what's missing.
- Lower the confidence level.
- Attribute the information to its original provider.

## Primary vs. trusted intermediary verification

- **Primary verification** — you personally verified the transaction on-chain via the explorer. (Tier 1)
- **Trusted intermediary verification** — the information comes from a reputable analytics platform (Arkham, Lookonchain, Glassnode, CryptoQuant, Nansen, SoSoValue). Valuable and often reliable, but not the same as direct on-chain verification. (Tier 3 — see [Evidence Framework](02-evidence-framework.md))

## Primary Document Verification Protocol

Retrieving a document is not enough. Before classifying anything as **Tier 1 — Primary Verified**, apply six checks:

1. Confirm the document is authentic.
2. Confirm every factual claim is supported by the document.
3. Separate the document's findings from any party's allegations or interpretations.
4. Quote figures accurately, or clearly mark paraphrases.
5. Preserve unresolved ambiguity instead of resolving it.
6. If only part of the story is directly supported, classify it as a **mixed evidence chain**, not fully Tier 1.

If the document's authenticity itself is disputed, see the "contested primary evidence" case in [Evidence Framework](02-evidence-framework.md).

## Principle

Evidence quality is determined by what you personally verified — not by how many people repeated the same claim. Primary verification always outranks secondary reporting.
