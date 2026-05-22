from bson import ObjectId
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


def print_list(title, values):
    print(title)
    for value in values:
        print(f"- {value}")


def select_database():
    databases = client.list_database_names()
    print_list("Databases", databases)
    return input("Select Database: ")


def select_collection(database_name):
    db = client[database_name]
    collections = db.list_collection_names()

    print()
    print(database_name)
    print_list("Collections", collections)

    return input("Select Collection: ")


def select_document(database_name, collection_name):
    collection = client[database_name][collection_name]
    documents = list(collection.find({}, {"_id": 1}))

    print()
    print(f"{database_name}.{collection_name}")
    print("Documents")

    for document in documents:
        print(f"- {document['_id']}")

    return input("Select Document: ")


def show_document(database_name, collection_name, document_id):
    collection = client[database_name][collection_name]
    document = collection.find_one({"_id": ObjectId(document_id)})

    print()
    print(f"{database_name}.{collection_name}.{document_id}")

    if document is None:
        print("Document not found")
        return

    for key, value in document.items():
        print(f"{key}: {value}")


database_name = select_database()
collection_name = select_collection(database_name)
document_id = select_document(database_name, collection_name)
show_document(database_name, collection_name, document_id)
