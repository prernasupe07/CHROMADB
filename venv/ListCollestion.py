import chromadb
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.list_collections()
print("all collections available:")
for c in collection:
    print("-", c.name)