from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create/Open database
client = PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="repositories"
)


def store_embeddings(repo_name: str, documents):

    ids = []
    embeddings = []
    metadatas = []
    texts = []

    for doc in documents:

        ids.append(
            f"{repo_name}_{doc['path']}_{doc['chunk_id']}"
        )

        texts.append(doc["content"])

        embeddings.append(
            model.encode(doc["content"]).tolist()
        )

        metadatas.append(
            {
                "repository": repo_name,
                "path": doc["path"],
                "chunk": doc["chunk_id"],
            }
        )

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    return len(ids)