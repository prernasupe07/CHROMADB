import numpy as np

import chromadb

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    
    return dot_product / (norm_vec1 * norm_vec2)


client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles_embeddings")

data = collection.get(include = ["documents", "embeddings"])
print("Comparing embeddings:")

emb_car = data["embeddings"][0]  # embedding for "car runs on petrol"
emb_bus = data["embeddings"][1]  # embedding for "bus carries passengers"
emb_bike = data["embeddings"][2] # embedding for "bicycle run without fuel"

#cpmare the simarity between car and bus
sim_car_bus = cosine_similarity(emb_car, emb_bus)

#compare the simarity between car and bike
sim_car_bike = cosine_similarity(emb_car, emb_bike)

print("consine similarity")
print(f"car vs bus: {sim_car_bus:.4f}")
print(f"car vs bike: {sim_car_bike:.4f}")