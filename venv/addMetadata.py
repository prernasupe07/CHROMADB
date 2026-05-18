import chromadb

client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(name="vehicles")

#Add data to the collection
collection.add(
    documents=["This is a bus run on roads",
                "This is a plane flies in the sky",
                "This is a boat travels in water ",
                "Bicycle is run without fuel"],
    ids=["bus1", "plane1", "boat1", "bicycle"],

    metadatas=[{"type":"public_transport","fuel":"diesel"},
               {"type":"aircraft","fuel":"jet_fuel"},
               {"type":"watercraft","fuel":"diesel"},
               {"type":"two_wheeler","fuel":"manual"}
               ]
)


print("Data with metadata added to the collection successfully!")


