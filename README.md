# 🏦 RAG Chatbot with Query Rewriting & Conversation Memory
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-LlamaIndex-purple?style=for-the-badge" alt="LlamaIndex"/>
  <img src="https://img.shields.io/badge/VectorDB-Qdrant-red?style=for-the-badge&logo=qdrant&logoColor=white" alt="Qdrant"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  A Retrieval-Augmented Generation (RAG) chatbot that answers questions about credit cards using your own data.<br/>
  Built with <b>LlamaIndex</b> and <b>Qdrant</b>.
</p>

---

## 📌 About

This is a **simple, naive RAG** — not a fully optimized one. It works well, but many advanced techniques (reranking, hybrid search, evaluation) are not included yet. See the [Roadmap](#-roadmap) below.

The prompt is written for **credit cards**, but you can use this project for any domain by changing the data and the prompt.

---

## ⚙️ Features

- 🔍 Semantic search over your own documents
- 🤖 Supports OpenAI, Groq, and Google Gemini
- 🧠 Configurable embedding provider via `.env` (default: Hugging Face `BAAI/bge-small-en-v1.5`)
- 🗄️ Qdrant vector database
- 🔄 Query rewriting using the LLM
- 💬 Conversation memory (last 6 messages, can be increased)
- 📄 Accepts `.csv` and `.txt` files
- 💻 Simple command-line chat interface
- 📊 API usage monitoring

---

## 🏗️ How It Works

```text
data/raw/  ──▶  ingestion.py  ──▶  Embeddings  ──▶  Qdrant
                                                        │
User Question  ──▶  Query Rewrite  ──▶  Retrieve  ──▶  LLM  ──▶  Answer
```

1. Put your data in `data/raw/`
2. Run `ingestion.py` to embed and store it in Qdrant
3. Run `main.py` to chat

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| Framework | LlamaIndex |
| Vector DB | Qdrant |
| Embeddings | Hugging Face `BAAI/bge-small-en-v1.5` |
| LLMs | OpenAI / Groq / Gemini |

---

## 📁 Project Structure

```text
project-root/
├── src/
│   ├── __init__.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── embedding_factory.py    # Embedding model setup
│   │   ├── llm_factory.py          # LLM provider setup
│   │   └── vector_store.py         # Qdrant connection
│   ├── memory/
│   │   └── chat_memory.py          # Conversation memory
│   ├── monitoring/
│   │   └── api_usage.py            # Tracks API usage
│   ├── prompts/
│   │   └── rag_prompt.py           # Domain-specific prompt
│   └── retrieval/
│       ├── __init__.py
│       ├── chatbot.py              # Main chat loop
│       ├── index_loader.py         # Loads Qdrant index
│       ├── query_engine.py         # Retrieval engine
│       └── query_rewriter.py       # LLM-based query rewriting
│
├── data/
│   └── raw/                        # Put your .csv / .txt files here
│
├── ingestion.py                    # Builds the Qdrant index
├── main.py                         # Entry point to run the chatbot
├── check_qdrant.py                 # Utility: test Qdrant connection
├── list_models.py                  # Utility: list available LLM models
├── requirements.txt
│
├── .env                            # (Ignored) Your API keys
├── qdrant_storage/                 # (Ignored) Local Qdrant DB files
├── api_usage.json                  # (Ignored) API usage logs
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Setup

### 1. Clone the repo

```bash
git clone https://github.com/tejeshkawle19/<RAG-chatbot>.git
cd <RAG-chatbot>
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys

Create a `.env` file in the project root:

```env
# LLM API keys (add the one you're using)
OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here

# Embedding provider
EMBEDDING_PROVIDER=huggingface

# Qdrant (only needed if using Qdrant Cloud)
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_key
```

> 💡 `EMBEDDING_PROVIDER` tells the app which embedding backend to use.  
> Currently supported: `huggingface` (uses `BAAI/bge-small-en-v1.5`).  
> To change the model itself, edit `src/common/embedding_factory.py`.

> ⚠️ Never commit your `.env` file. It is already in `.gitignore`.

---

## 📖 How to Use

### Step 1 — Add data

Put your `.csv` or `.txt` files inside `data/raw/`.

### Step 2 — Run ingestion

```bash
python ingestion.py
```

You should see:

```text
ingestion complete
```

> Re-run this only when you change your data or embedding model.

### Step 3 — Start chatting

```bash
python main.py
```

Then ask questions like:

```text
You: What is the annual fee for the Platinum card?
Bot: The Platinum card has an annual fee of ₹5,000...
```

---

## 🔄 Using a Different Domain

This project is set up for credit cards, but easy to repurpose:

1. Replace files in `data/raw/` with your own data
2. Update the prompt in `src/prompts/rag_prompt.py`
3. Re-run `ingestion.py`, then `main.py`

**Example:** for a medical chatbot, swap the credit card data with medical documents and rewrite the prompt accordingly.

---

## 🔧 Changing the Embedding Model

Edit `src/common/embedding_factory.py`:

```python
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
```

After changing it, **delete the Qdrant collection** (or the local `qdrant_storage/` folder) and run `ingestion.py` again. Old embeddings won't work with a new model.

---

## 🐞 Common Issues

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `401` / auth error | Check your API key in `.env` |
| No `ingestion complete` message | Check files are in `data/raw/` and are valid |
| Qdrant connection error | Run `python check_qdrant.py` to test the connection |
| Bad answers | Delete Qdrant collection and re-run ingestion |
| `Dimension mismatch` | You changed the embedding model — recreate the collection |

---

## 🗺️ Roadmap

- [ ] Reranking of retrieved chunks
- [ ] Hybrid search (dense + sparse)
- [ ] Metadata filtering
- [ ] Source citations in answers
- [ ] Evaluation with RAGAS
- [ ] Web UI (Streamlit / Gradio)
- [ ] Docker support

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Tejesh Kawle**
- GitHub: [@tejeshkawle19](https://github.com/tejeshkawle19)
- LinkedIn: [tejesh-analyst](https://www.linkedin.com/in/tejesh-analyst)

---

## 🙏 Acknowledgements

- [LlamaIndex](https://www.llamaindex.ai/) — RAG framework
- [Qdrant](https://qdrant.tech/) — vector database
- [Hugging Face](https://huggingface.co/BAAI/bge-small-en-v1.5) — `BAAI/bge-small-en-v1.5` embeddings
- [OpenAI](https://openai.com/) · [Groq](https://groq.com/) · [Google Gemini](https://ai.google.dev/) — LLM providers
