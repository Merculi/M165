from pymongo import MongoClient
import matplotlib.pyplot as plt


client = MongoClient("mongodb://localhost:27017/")
collection = client["power_statistic"]["logs"]

logs = list(collection.find().sort("timestamp", 1))

timestamps = [log["timestamp"] for log in logs]
cpu_values = [log["cpu"] for log in logs]
ram_used_values = [log["ram_used"] for log in logs]
ram_total_values = [log["ram_total"] for log in logs]

ram_used_percent = [
    used / total * 100
    for used, total in zip(ram_used_values, ram_total_values)
]

plt.plot(timestamps, cpu_values, label="CPU in Prozent")
plt.plot(timestamps, ram_used_percent, label="RAM in Prozent")

plt.xlabel("Zeit")
plt.ylabel("Auslastung in Prozent")
plt.title("CPU- und RAM-Auslastung")
plt.legend()
plt.grid(True)
plt.show()
