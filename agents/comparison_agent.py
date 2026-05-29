from agents.lyzr_client import ask_lyzr

def normalize(concept: str) -> str:
    """Normalize any engineering concept to a canonical Title Case phrase using Lyzr."""
    prompt = (
        "Normalize this engineering concept to its standard canonical name. "
        "Return ONLY a short phrase in Title Case, e.g., 'Dijkstra’s Algorithm'. "
        f"Concept: {concept}"
    )
    lyzr = ask_lyzr(prompt)
    text = lyzr["response"].strip()

    # Take first line only (Lyzr may return a paragraph)
    canonical = text.split("\n")[0].strip()

    return canonical


def compare(concept1: str, concept2: str) -> str:
    # Lyzr normalization -> Title Case canonical names
    concept1 = normalize(concept1)
    concept2 = normalize(concept2)

    # Title Case canonical comparison table
    pairs = {
        ("Dijkstra’s Algorithm", "Bellman-Ford Algorithm"): (
            "Dijkstra’s Algorithm\n"
            "+ Faster\n"
            "+ Positive weights\n"
            "Complexity: O((V+E)logV)\n\n"
            "Bellman-Ford Algorithm\n"
            "+ Supports negative weights\n"
            "+ Detects negative cycles\n"
            "Complexity: O(VE)"
        ),
        ("Laplace Transform", "Fourier Transform"): (
            "Laplace Transform\n"
            "+ Handles transient signals\n"
            "+ Used in control systems\n\n"
            "Fourier Transform\n"
            "+ Frequency-domain analysis\n"
            "+ Ideal for steady‑state signals"
        ),
        ("Depth‑First Search", "Breadth‑First Search"): (
            "Depth‑First Search\n"
            "+ Less memory\n"
            "+ Backtracking\n\n"
            "Breadth‑First Search\n"
            "+ Finds shortest path in unweighted graphs\n"
            "+ Level‑order traversal"
        ),
    }

    key = (concept1, concept2)
    reverse = (concept2, concept1)

    return pairs.get(key) or pairs.get(reverse, "No comparison found")
