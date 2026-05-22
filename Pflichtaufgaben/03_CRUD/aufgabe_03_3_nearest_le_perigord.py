from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]

db.restaurants.create_index([("address.coord", "2d")])

le_perigord = db.restaurants.find_one({"name": "Le Perigord"})

if le_perigord is None:
    print("Le Perigord wurde nicht gefunden.")
else:
    nearest = db.restaurants.find(
        {
            "name": {"$ne": "Le Perigord"},
            "address.coord": {"$near": le_perigord["address"]["coord"]},
        }
    ).limit(1)

    for restaurant in nearest:
        print(restaurant["name"])
        print(restaurant["address"])
