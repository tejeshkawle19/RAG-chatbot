from llama_index.llms.gemini import Gemini
from llama_index.llms.openai import OpenAI
from llama_index.llms.groq import Groq

from src.common.config import (
    LLM_PROVIDER,

    GEMINI_MODEL,
    OPENAI_MODEL,
    GROQ_MODEL,
    GROK_MODEL,

    GEMINI_API_KEY,
    OPENAI_API_KEY,
    GROQ_API_KEY,
    GROK_API_KEY,
)


def get_llm():

    provider = LLM_PROVIDER.lower()

    # -------------------------
    # Gemini
    # -------------------------
    if provider == "gemini":

        return Gemini(
            model=GEMINI_MODEL,
            api_key=GEMINI_API_KEY,
        )

    # -------------------------
    # OpenAI
    # -------------------------
    elif provider == "openai":

        return OpenAI(
            model=OPENAI_MODEL,
            api_key=OPENAI_API_KEY,
        )

    # -------------------------
    # Groq
    # -------------------------
    elif provider == "groq":

        return Groq(
            model=GROQ_MODEL,
            api_key=GROQ_API_KEY,
        )

    # -------------------------
    # Grok (xAI)
    # -------------------------
    elif provider == "grok":

        return OpenAI(
            model=GROK_MODEL,
            api_key=GROK_API_KEY,
            api_base="https://api.x.ai/v1",
        )

    else:

        raise ValueError(
            f"Unsupported LLM Provider : {LLM_PROVIDER}"
        )