import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="vehicles_embeddings")

print("collection name:", collection.name)


collection.add(
    documents=[
        "car runs on petrol",
        "bus carries paassengers",
        "bicycle run without fuel",
        "boat travels on water",
        "plane flies in the sky",
    ],
    ids=["cars1", "bus1", "bicycle1", "boat1", "plane1"],
)

print("documents added to the collection with embeddings automatically generated!") 

