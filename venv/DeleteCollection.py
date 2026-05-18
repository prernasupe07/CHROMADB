import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="vehicles")

#Delete one document

collection.delete(ids=["car1"])

print("Document deleted successfully!")

#Delete the entire collection

collection.delete()

print("Collection deleted successfully!")

 