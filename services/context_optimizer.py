def optimize_context(memories, limit=3):
    seen = set()
    final = []

    for m in memories:
        raw = m.get("raw", "")

        if raw not in seen:
            seen.add(raw)
            final.append(m)

    return final[:limit]