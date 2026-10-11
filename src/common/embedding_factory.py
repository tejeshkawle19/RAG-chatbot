from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from src.common.config import (
    EMBEDDING_PROVIDER,
    EMBEDDING_MODEL,
)


def get_embedding_model():

    provider = EMBEDDING_PROVIDER.lower()

    if provider == "huggingface":

        return HuggingFaceEmbedding(
            model_name=EMBEDDING_MODEL
        )

    raise ValueError(
        f"Unsupported Embedding Provider: {EMBEDDING_PROVIDER}"
    )