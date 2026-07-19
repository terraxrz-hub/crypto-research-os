"""
demo.py — runs a handful of real queries end-to-end and prints every stage:
  User query -> Retriever (metadata filter + TF-IDF search + ranking +
  graph expansion) -> assembled context (what would be sent to Claude) ->
  Response (generated if ANTHROPIC_API_KEY is set, extractive otherwise).

Run: python3 demo.py
"""

from rag import answer, SYSTEM_PROMPT

QUERIES = [
    "What does the QA gate require before a story can PASS?",
    "How do I classify evidence that comes from a single trusted analytics platform?",
    "What should I do if a story is breaking news and I can't fully verify it in time?",
]


def run(query):
    print("#" * 78)
    result = answer(query, verbose=True)

    print("--- Assembled context (what gets sent to the LLM) ---")
    print(result["context"][:1200] + ("...\n[truncated for display]" if len(result["context"]) > 1200 else ""))
    print()
    print(f"--- Response ({result['mode']}) ---")
    print(result["answer"])
    print()


if __name__ == "__main__":
    print("SYSTEM PROMPT (fixed, sent with every query):\n")
    print(SYSTEM_PROMPT)
    print()

    for q in QUERIES:
        run(q)
