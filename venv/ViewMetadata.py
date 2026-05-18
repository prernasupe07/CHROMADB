import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="vehicles")

#View the metadata of the collection

data = collection.get(include=["documents", "metadatas"])

print("Metadata of the collection:")
for i, doc, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"id: {i} -> document: {doc} -> metadata: {meta}")

