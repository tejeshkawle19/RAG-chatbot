# import pandas as pd

# from llama_index.core import Document, VectorStoreIndex, StorageContext

# from src.common.vector_store import get_vector_store
# from src.common.embedding_factory import get_embedding_model

# # Read CSV
# df = pd.read_csv("data/raw/credit_cards_master_sheet_25-05.csv")

# documents = []

# for _, row in df.iterrows():

#     text = ""

#     for column in df.columns:
#         text += f"{column}: {row[column]}\n"

#     documents.append(
#         Document(text=text)
#     )

# # Connect to Qdrant
# vector_store = get_vector_store()

# storage_context = StorageContext.from_defaults(
#     vector_store=vector_store
# )

# VectorStoreIndex.from_documents(
#     documents,
#     storage_context=storage_context,
#     embed_model=get_embedding_model(),
# )

# print(f"✅ Successfully ingested {len(documents)} credit cards.")

import pandas as pd
from pathlib import Path

from llama_index.core import (
    Document,
    VectorStoreIndex,
    StorageContext,
)

from src.common.vector_store import get_vector_store
from src.common.embedding_factory import get_embedding_model


RAW_DATA_PATH = Path("data/raw")

documents = []


# -------------------------
# Read all files
# -------------------------
for file in RAW_DATA_PATH.iterdir():

    # -------------------------
    # CSV
    # -------------------------
    if file.suffix == ".csv":

        print(f"\nReading CSV : {file.name}")

        df = pd.read_csv(file)

        for _, row in df.iterrows():

            text = ""

            for column in df.columns:
                text += f"{column}: {row[column]}\n"

            documents.append(
                Document(
                    text=text,
                    metadata={
                        "source": file.name,
                        "type": "credit_card"
                    }
                )
            )

    # -------------------------
    # TXT
    # -------------------------
    elif file.suffix == ".txt":

        print(f"\nReading TXT : {file.name}")

        with open(file, "r", encoding="utf-8") as f:

            text = f.read()

        documents.append(
            Document(
                text=text,
                metadata={
                    "source": file.name,
                    "type": "user_profile"
                }
            )
        )


print(f"\nTotal Documents : {len(documents)}")


# -------------------------
# Connect to Qdrant
# -------------------------
vector_store = get_vector_store()

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=get_embedding_model(),
)

print("\n✅ Ingestion Complete!")