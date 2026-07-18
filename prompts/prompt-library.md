# Prompt Library

The old workspace had two pages here (**Prompt Library** and **Prompts**) that were ~85% the same six prompts under different names. Merged into one, deduplicated set. Each prompt is a thin trigger for a standard already defined elsewhere — none of these restate the rules, they just invoke them.

## 1. Market Scan
**Purpose:** find the highest-EV story available right now.
> Run a fresh market scan (see [Research Workflow](../docs/09-research-workflow.md)). Never reuse previous data — refresh all prices. Rank candidates using the six [Decision Framework](../docs/06-decision-framework.md) criteria. Explain why the winner beats the alternatives. Consider alternative explanations. End with a Publication Status per [Publication Standard](../docs/07-publication-standard.md).

## 2. Fact Check
**Purpose:** verify every factual claim before publication.
> Search fresh. Verify every number. Trace every claim to its original source using [Sources & Research Priority](../docs/01-sources-and-priority.md). Classify each with [Evidence Framework](../docs/02-evidence-framework.md). Preserve disagreements. State what remains unknown.

## 3. Verify On-Chain
**Purpose:** confirm a blockchain-specific claim.
> Verify this on-chain claim per [On-Chain Verification](../docs/05-on-chain-verification.md). Try to retrieve wallet, transaction hash, block height, explorer link. State exactly what could and couldn't be verified.

## 4. Tweet Writer
**Purpose:** turn verified research into a standalone tweet.
> Write one standalone tweet, under 280 characters, following [Writing & Mechanism](../docs/03-writing-and-mechanism.md): mechanism before conclusion, facts before analysis, preserve uncertainty, no hype.

## 5. Thread Builder
**Purpose:** used only when one tweet can't hold the mechanism.
> Build a thread. Every tweet under 280 characters. Natural split, no repeated information, uncertainty still preserved.

## 6. Visual Search
**Purpose:** find supporting visuals.
> Find supporting visuals per the priority order in [Visual Assets](../docs/04-visual-assets.md). Label every visual: source, evidence level, why it adds decision value. Say "No supporting visual recommended" if nothing qualifies.

## 7. Final QA
**Purpose:** last check before publishing.
> Run the full [QA Gate](../docs/08-qa-gate.md). Answer all ten questions. State PASS / PASS WITH LIMITATIONS / WAIT. Mention every remaining limitation.

---
When filing an actual research entry, use the **`research-entry`** issue form instead of running these ad hoc — it embeds the same steps as structured fields feeding the Research Database.
