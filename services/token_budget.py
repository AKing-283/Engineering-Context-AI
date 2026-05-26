def limit_context(memory, max_chars=400):
    total = 0
    output = []

    for item in memory:
        text = item.get("raw", "")

        if total + len(text) > max_chars:
            break

        total += len(text)
        output.append(item)

    return output