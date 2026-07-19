"""
llm.py — the generation half of RAG. Deliberately minimal: stdlib
`urllib` only, no SDK dependency, calls the public Anthropic Messages API
directly. If ANTHROPIC_API_KEY isn't set, `call_claude` returns None and
rag.py falls back to an extractive (non-generated) answer — the pipeline
stays runnable end-to-end either way, which matters for a prototype meant
to be run and inspected without requiring credentials first.
"""

import os
import json
import urllib.request
import urllib.error

DEFAULT_MODEL = "claude-sonnet-5"
API_URL = "https://api.anthropic.com/v1/messages"


def call_claude(prompt, system=None, model=DEFAULT_MODEL, max_tokens=800):
    """Return the model's text response, or None if no API key is set or
    the call fails (caller decides how to fall back — see rag.py)."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        body["system"] = system

    request = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"WARNING: Anthropic API call failed ({e.code}): {e.read().decode(errors='replace')[:300]}")
        return None
    except urllib.error.URLError as e:
        print(f"WARNING: Anthropic API call failed: {e}")
        return None

    return "".join(
        block.get("text", "")
        for block in data.get("content", [])
        if block.get("type") == "text"
    )
