from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore

from src.common.config import (
    QDRANT_PATH,
    COLLECTION_NAME,
)

client = QdrantClient(path=QDRANT_PATH)


def get_qdrant_client():
    return client


def get_vector_store():
    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
    )