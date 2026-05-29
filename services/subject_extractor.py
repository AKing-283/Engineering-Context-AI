import re

def extract_subjects_from_lyzr_response(lyzr_text: str) -> str:
    """
    Hybrid Subject Extractor:
    - Input: Long paragraph returned by Lyzr classification
    - Output: Clean comma-separated subjects like:
      "Graph Theory, Algorithm Design, Computer Science"
    """

    # Normalize text
    text = lyzr_text.strip()

    # Split on common separators
    parts = re.split(r"[.,;]| and | under | in | specifically | categorized as | called | known as ", text, flags=re.IGNORECASE)

    # Extract candidates that look like engineering/CS subjects
    candidates = []
    for part in parts:
        part = part.strip()

        # Must start with capital letter (Graph Theory, Algorithm Design)
        if re.match(r"^[A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+)*$", part):
            candidates.append(part)

    # Deduplicate
    unique = []
    for c in candidates:
        if c not in unique:
            unique.append(c)

    # If nothing detected, fallback to "General"
    if not unique:
        return "General"

    # Return comma-separated subjects
    return ", ".join(unique)