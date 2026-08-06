from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = PersistentClient(path="vector_db")

collection = client.get_collection("repositories")


def search_repository(repository: str, query: str, n_results: int = 5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where={
            "repository": repository
        }
    )

    response = []

    for i in range(len(results["documents"][0])):

        response.append(
            {
                "path": results["metadatas"][0][i]["path"],
                "content": results["documents"][0][i],
                "distance": results["distances"][0][i],
            }
        )

    return response