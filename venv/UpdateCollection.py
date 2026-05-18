import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="vehicles")

#Update an existing document
collection.update(
    ids=["car1"],
    documents=["This is an updated description of the car that runs on roads"]
)

print("Document updated successfully!")

#retrive all stored data
record = collection.get(ids=["car1"])
print(record)
