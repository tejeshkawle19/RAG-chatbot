from src.common.llm_factory import get_llm

client = get_llm()


def rewrite_query(history, question):

    prompt = f"""
You are a query rewriting assistant.

Conversation History:
{history}

Current User Question:
{question}

Rewrite the user's latest question into a complete standalone question.

Rules:
- Preserve the meaning.
- Resolve pronouns like:
  - it
  - its
  - this card
  - that card
  - they
- Return ONLY the rewritten question.
"""

    response = client.complete(prompt)

    return response.text.strip()

# import re


# def rewrite_query(history, question):

#     question = question.strip()

#     # If there is no history, return as is
#     if not history:
#         return question

#     history_lines = history.strip().split("\n")

#     # Find the last user question
#     last_user = None

#     for line in reversed(history_lines):
#         if line.startswith("User:"):
#             last_user = line.replace("User:", "").strip()
#             break

#     if last_user is None:
#         return question

#     pronouns = [
#         "it",
#         "its",
#         "this",
#         "that",
#         "this card",
#         "that card",
#         "these",
#         "those",
#         "them",
#         "they",
#     ]

#     lower_question = question.lower()

#     if any(word in lower_question for word in pronouns):

#         rewritten = re.sub(
#             r"\bit\b|\bits\b|\bthis\b|\bthat\b|\bthem\b|\bthey\b",
#             last_user,
#             question,
#             flags=re.IGNORECASE,
#         )

#         return rewritten

#     return question