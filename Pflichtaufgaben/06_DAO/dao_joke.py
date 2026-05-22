from bson import ObjectId
from pymongo import MongoClient

from joke import Joke


class DaoJoke:
    def __init__(self, connection_string):
        client = MongoClient(connection_string)
        self.collection = client["jokes_db"]["jokes"]

    def insert(self, joke):
        result = self.collection.insert_one(joke.__dict__)
        return result.inserted_id

    def get_category(self, category):
        jokes = []
        documents = self.collection.find({"category": category})

        for document in documents:
            jokes.append(Joke(**document))

        return jokes

    def delete(self, joke_id):
        result = self.collection.delete_one({"_id": ObjectId(joke_id)})
        return result.deleted_count
