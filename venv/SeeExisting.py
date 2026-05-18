import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="vehicles")
print(collection.get())