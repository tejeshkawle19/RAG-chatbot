# from qdrant_client import QdrantClient

# client = QdrantClient(path="./qdrant_db")

# points, _ = client.scroll(
#     collection_name="credit_cards",
#     limit=10,
#     with_vectors=True,
#     with_payload=True,
# )

# for point in points:
#     print("=" * 80)
# print("ID:", point.id)
# print("Vector Dimension:", len(point.vector))

# print("\nStored Text:")
# print(point.payload["_node_content"])

from qdrant_client import QdrantClient

client = QdrantClient(path="./qdrant_db")

points = client.scroll(
    collection_name="credit_cards",
    limit=2,
    with_vectors=True,
    with_payload=True
)

print(points)