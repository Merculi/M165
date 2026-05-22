from bson import ObjectId
from pymongo import MongoClient

from room import Room


class DaoRoom:
    def __init__(self, connection_string):
        client = MongoClient(connection_string)
        self.collection = client["buildings"]["rooms"]

    def create(self, room):
        result = self.collection.insert_one(room.__dict__)
        return result.inserted_id

    def read(self):
        rooms = []

        for document in self.collection.find():
            rooms.append(Room(**document))

        return rooms

    def update(self, room_id, room):
        result = self.collection.update_one(
            {"_id": ObjectId(room_id)},
            {
                "$set": {
                    "name": room.name,
                    "seats": room.seats,
                    "is_reservable": room.is_reservable,
                }
            },
        )
        return result.modified_count

    def delete(self, room_id):
        result = self.collection.delete_one({"_id": ObjectId(room_id)})
        return result.deleted_count
