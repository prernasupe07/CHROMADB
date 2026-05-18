import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="vehicles_semantic")

collection.add(
    documents=[
        "car runs on petrol",
        "bus carries paassengers",
        "bicycle run without fuel",
        "boat travels on water",
        "plane flies in the sky",
    ],
    ids=["cars1", "bus1", "bicycle1", "boat1", "plane1"]
)
print("sample data added!")

#search semantically

results = collection.query(
    query_texts=["vehicle that does not need fuel"],
    n_results=3
)
print("semantic search results:")
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"{doc} (distance:{dist:.4f})")


