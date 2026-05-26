import json

from agents.lyzr_client import ask_lyzr
from services.engineering_dictionary import normalize_term

def extract_reasoning(text):
    prompt = f"""Engineering reasoning:
{text}

Extract ONLY JSON.
Requirements:
1 Correct spelling
2 Engineering terminology
3 STRICT JSON

Format:
{{
"concept":"",
"reason":""
}}

No markdown.
No explanation."""

    result = ask_lyzr(prompt)

    try:
        raw = result.get("response", "{}")
        parsed = json.loads(raw)

        if not parsed.get("concept"):
            parsed["concept"] = "unknown"

        if not parsed.get("reason"):
            parsed["reason"] = text

        parsed["concept"] = normalize_term(parsed.get("concept"))

        return parsed

    except Exception:
        return {"concept": "unknown", "reason": text}