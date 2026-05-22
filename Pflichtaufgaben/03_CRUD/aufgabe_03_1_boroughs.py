from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]

boroughs = db.restaurants.distinct("borough")

for borough in boroughs:
    print(borough)
