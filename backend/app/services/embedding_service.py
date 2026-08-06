from chromadb import PersistentClient

from app.services.model_loader import get_model

client = PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="repositories"
)


def store_embeddings(repo_name: str, documents):

    print("Loading model...")
    model = get_model()

    ids = []
    texts = []
    metadatas = []

    print("Preparing documents...")

    for doc in documents:

        ids.append(
            f"{repo_name}_{doc['path']}_{doc['chunk_id']}"
        )

        texts.append(doc["content"])

        metadatas.append(
            {
                "repository": repo_name,
                "path": doc["path"],
                "chunk": doc["chunk_id"],
            }
        )

    print(f"Encoding {len(texts)} chunks...")

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
    ).tolist()

    print("Encoding complete.")

    print("Saving to ChromaDB...")

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    print("Embeddings stored successfully.")

    return len(ids)