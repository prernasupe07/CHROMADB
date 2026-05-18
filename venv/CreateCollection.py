import chromadb

# client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")


collection = client.create_collection("vehicles")
collection.add(
    documents=["This is a car run on roads"],
    ids=["car1"]
)
print("data added and save permanently in the chroma_db folder")