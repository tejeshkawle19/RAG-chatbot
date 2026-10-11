from src.retrieval.query_engine import get_retriever
from src.common.config import (
    SIMILARITY_THRESHOLD,
    DAILY_API_LIMIT,
)
from src.common.llm_factory import get_llm
from src.memory.chat_memory import ChatMemory
from src.retrieval.query_rewriter import rewrite_query
from src.monitoring.api_usage import (
    record_api_call,
    get_usage,
)


def main():

    retriever = get_retriever()

    llm = get_llm()

    memory = ChatMemory()

    print("=" * 60)
    print("Credit Card RAG Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        # ======================================
        # Rewrite Query
        # ======================================

        history = memory.get_history()

        rewritten_question = rewrite_query(
            history,
            question,
        )

        print("\nRewritten Question")
        print("=" * 60)
        print(rewritten_question)

        print("\nSearching...")

        # ======================================
        # Retrieve Chunks
        # ======================================

        nodes = retriever.retrieve(rewritten_question)

        if not nodes:
            print("\nNo relevant documents found.")
            continue

        best_score = nodes[0].score if nodes[0].score else 0.0

        print("\nDebug Information")
        print("=" * 60)
        print(f"Similarity Score : {best_score:.4f}")
        print("=" * 60)

        if best_score < SIMILARITY_THRESHOLD:
            print("\nI am Maven Specialized in credit card, I can only answer questions related to credit cards.")
            continue

        context = ""

        print("\nRetrieved Chunks")
        print("=" * 70)

        for i, node in enumerate(nodes, start=1):

            print(f"\nChunk {i}")
            print(f"Similarity Score : {node.score:.4f}")
            print("-" * 70)
            print(node.text)
            print("=" * 70)

            context += node.text + "\n\n"

        prompt = f"""
You are a Credit Card Expert.

Answer ONLY using the context below.

Rules:

- Do not use outside knowledge.
- If the answer is not in the context, reply:

I don't have enough information in my knowledge base.

Context:

{context}

Question:

{rewritten_question}

Answer:
"""

        used, remaining = get_usage()

        print("\nAPI Usage")
        print("=" * 60)
        print(f"Used Today      : {used}/{DAILY_API_LIMIT}")
        print(f"Remaining Calls : {remaining}")
        print("=" * 60)

        print("\nGenerating Answer...\n")

        try:

            response = llm.complete(prompt)

            record_api_call()

            print("Answer")
            print("=" * 70)
            print(response.text)

            memory.add_user(question)
            memory.add_assistant(response.text)

        except Exception as e:

            print("\nLLM Error")
            print("=" * 70)
            print(str(e))


if __name__ == "__main__":
    main()