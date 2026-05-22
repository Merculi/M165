from pymongo import MongoClient


connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)

try:
    client.admin.command("ping")
    print("Verbindung zu MongoDB erfolgreich.")
except Exception as error:
    print("Verbindung fehlgeschlagen:")
    print(error)
