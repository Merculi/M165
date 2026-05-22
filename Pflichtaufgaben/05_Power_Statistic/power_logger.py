import time

from pymongo import MongoClient

from power import Power


client = MongoClient("mongodb://localhost:27017/")
collection = client["power_statistic"]["logs"]
MAX_LOGS = 10000


def delete_old_logs():
    count = collection.count_documents({})
    if count <= MAX_LOGS:
        return

    amount_to_delete = count - MAX_LOGS
    old_logs = collection.find().sort("timestamp", 1).limit(amount_to_delete)
    old_ids = [log["_id"] for log in old_logs]

    if old_ids:
        collection.delete_many({"_id": {"$in": old_ids}})


while True:
    power = Power()
    collection.insert_one(power.__dict__)
    delete_old_logs()
    print("Messung gespeichert")
    time.sleep(1)
