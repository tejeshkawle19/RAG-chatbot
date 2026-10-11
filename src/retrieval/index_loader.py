from llama_index.core import VectorStoreIndex

from src.common.vector_store import get_vector_store

from src.common.embedding_factory import get_embedding_model


def load_index():

    vector_store = get_vector_store()

    embed_model = get_embedding_model()

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model,
    )

    return index