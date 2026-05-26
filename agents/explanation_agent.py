from agents.lyzr_client import ask_lyzr

RULES = """
You are an Engineering AI.

Rules:
1. Use student memory.
2. Explain concepts.
3. No hallucinations.
4. Engineering only.
5. Under 120 words.
"""


def explain(question: str, memory: list) -> dict:
    """Combines system rules, retrieved memory context, and user question to generate a response via Lyzr."""
    prompt = f"""
{RULES}

Student Memory:
{memory}

Question:
{question}
"""
    return ask_lyzr(prompt)