import chromadb

client = chromadb.PersistentClient(path="./chroma_db")  
collection = client.get_collection(name="vehicles")

#filter by transport type
public_transport =  collection.get(where={"type": "public_transport"})
print("public transport vehicles:")
print(public_transport)

#filter by fuel type
diesel_vehicles = collection.get(where={"fuel": "diesel"})
print("diesel vehicles:")
print(diesel_vehicles)

