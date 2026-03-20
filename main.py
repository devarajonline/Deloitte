import json
from datetime import datetime

# Convert ISO timestamp to milliseconds
def iso_to_milliseconds(iso_string):
    dt = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

# Unify the data format
def unify_data(data):
    if "deviceId" in data:
        return data
    else:
        return {
            "deviceId": data["device"]["id"],
            "temperature": data["metrics"]["temp"],
            "humidity": data["metrics"]["hum"],
            "timestamp": iso_to_milliseconds(data["time"])
        }

# Read JSON files
with open("data-1.json") as f1:
    data1 = json.load(f1)

with open("data-2.json") as f2:
    data2 = json.load(f2)

# Convert to unified format
result1 = unify_data(data1)
result2 = unify_data(data2)

print("Unified Data 1:", result1)
print("Unified Data 2:", result2)
