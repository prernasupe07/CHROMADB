import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

#get the existing collection
collection = client.get_collection(name="vehicles")

#retrive all stored data
data = collection.get()

print("all documents inside vehicles:")
for i , doc in zip(data["ids"],data["documents"]):
    print(f"id: {i} -> document: {doc}")