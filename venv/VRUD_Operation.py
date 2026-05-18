import chromadb
#connect to chroma with persistent client
client = chromadb.PersistentClient(path="./chroma_db")

#create or reuse a collection
collection = client.get_or_create_collection(name="vehicles")

print("Collection name:", collection.name)

#Add data to the collection
collection.add(
    documents=["This is a car run on roads",
                "This is a plane flies in the sky",
                "This is a boat travels in water ",
                "This is a bike run on roads"],
    ids=["car1", "plane1", "boat1", "bike1"]
)

print("Data added to the collection successfully!")

data = collection.get()
print("current data")
for i , doc in zip(data["ids"],data["documents"]):
    print(f"id: {i} -> document: {doc}")
