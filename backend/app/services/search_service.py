from chromadb import PersistentClient

from app.services.model_loader import get_model

client = PersistentClient(path="vector_db")

collection = client.get_or_create_collection(name="repositories")


def search_repository(repository: str, query: str, n_results: int = 5):

    model = get_model()

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