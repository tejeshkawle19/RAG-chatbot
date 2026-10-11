from src.retrieval.index_loader import load_index


def get_retriever():

    index = load_index()

    retriever = index.as_retriever(
        similarity_top_k=5
    )

    return retriever