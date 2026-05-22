from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]

name = input("Name: ").strip()
cuisine = input("Kueche: ").strip()

query = {}

if name:
    query["name"] = {"$regex": name, "$options": "i"}

if cuisine:
    query["cuisine"] = {"$regex": cuisine, "$options": "i"}

results = db.restaurants.find(query)

for restaurant in results:
    print()
    print(f"ID: {restaurant['_id']}")
    print(f"Name: {restaurant.get('name')}")
    print(f"Kueche: {restaurant.get('cuisine')}")
    print(f"Bezirk: {restaurant.get('borough')}")
