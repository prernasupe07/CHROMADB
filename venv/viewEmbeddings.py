import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles_embeddings")

print("collection ready:",collection.name)

data = collection.get(include = ["documents", "embeddings"])

print("documents in the collection:")
for doc, emb, id in zip(data["documents"],data["embeddings"],data["ids"]):
    print(f"id:{id}, documents:{doc}, embedding:{emb[:10]}")