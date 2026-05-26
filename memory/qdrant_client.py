import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()

COLLECTION = "engineering_memory"

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)


def initialize_qdrant():
    collections = client.get_collections()
    names = [c.name for c in collections.collections]

    if COLLECTION not in names:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
        print("Created collection")
    else:
        print(f"Collection '{COLLECTION}' already exists.")


def reset_collection():
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass

    initialize_qdrant()