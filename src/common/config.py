import os

from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# ===========================
# LLM Configuration
# ===========================

LLM_PROVIDER = os.getenv("LLM_PROVIDER")

GEMINI_MODEL = os.getenv("GEMINI_MODEL")

OPENAI_MODEL = os.getenv("OPENAI_MODEL")

GROQ_MODEL = os.getenv("GROQ_MODEL")

GROK_MODEL = os.getenv("GROK_MODEL")


# ===========================
# Embedding Configuration
# ===========================

EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

# ===========================
# API Keys
# ===========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROK_API_KEY = os.getenv("GROK_API_KEY")

# ===========================
# Qdrant Configuration
# ===========================

QDRANT_PATH = os.getenv("QDRANT_PATH")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
TOP_K = int(os.getenv("TOP_K", 5))

SIMILARITY_THRESHOLD = float(
    os.getenv("SIMILARITY_THRESHOLD", 0.70)
)

DAILY_API_LIMIT = int(os.getenv("DAILY_API_LIMIT", 20))