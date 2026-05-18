import chromadb
client = chromadb.Client()

#create collection
collection = client.create_collection(name="vehicles")

print("Collection created successfully!",collection.name)

#Add data to the collection
collection.add(
    documents=["This is a car run on roads",
                "This is a plane flies in the sky",
                "This is a boat travels in water ",
                "This is a bike run on roads"],
    ids=["car1", "plane1", "boat1", "bike1"]
)

#Query the collection
results = collection.query(
    query_texts=["which can carry more than 20 people"],
    n_results=2
)

#print the output
print("Query results:", results)