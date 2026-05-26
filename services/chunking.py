def chunk_text(
    text: str,
    size=250
):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        size
    ):

        chunk = " ".join(
            words[
                i:i+size
            ]
        )

        chunks.append(chunk)

    return chunks