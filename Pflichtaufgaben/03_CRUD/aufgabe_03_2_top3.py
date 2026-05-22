from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]

pipeline = [
    {"$unwind": "$grades"},
    {
        "$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "borough": {"$first": "$borough"},
            "avg_score": {"$avg": "$grades.score"},
        }
    },
    {"$sort": {"avg_score": -1}},
    {"$limit": 3},
]

for restaurant in db.restaurants.aggregate(pipeline):
    print(restaurant["name"], restaurant["borough"], restaurant["avg_score"])
