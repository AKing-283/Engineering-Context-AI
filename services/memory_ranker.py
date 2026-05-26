ENGINEERING_PRIORITY = {
    "bellman": 10,
    "negative": 9,
    "dijkstra": 7,
    "positive": 6,
    "laplace": 8,
    "frequency": 7,
    "kirchhoff": 8,
}


def engineering_priority(memories, query=""):
    query = query.lower()
    ranked = []

    for memory in memories:
        score = 0
        payload = str(memory).lower()

        for keyword, weight in ENGINEERING_PRIORITY.items():
            if keyword in payload:
                score += weight

            if keyword in query and keyword in payload:
                score += 15

        ranked.append((score, memory))

    # Sort by score descending
    ranked.sort(reverse=True, key=lambda x: x[0])

    return [item[1] for item in ranked]