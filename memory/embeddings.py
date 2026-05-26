from sentence_transformers import SentenceTransformer

# Initialize the model globally so it only loads into memory once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str) -> list[float]:
    """Generates a dense vector embedding list for a given text input."""
    return model.encode(text).tolist()