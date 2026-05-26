BLOCKED = ["api key", "ignore instructions", "delete database", "system prompt"]


def validate_query(query):
    q = query.lower()
    for word in BLOCKED:
        if word in q:
            return False, "Unsafe request"
    return True, None