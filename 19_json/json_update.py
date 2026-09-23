# JSON
# Updating JSON data

import json

file_name = "security_event.json"

with open(file_name, "r") as file:
    data = json.load(file)

data["status"] = "investigated"
data["attempts"] = data["attempts"] + 1

with open(file_name, "w") as file:
    json.dump(data, file, indent=4)

print("JSON data updated successfully.")
print("Status:", data["status"])
print("Attempts:", data["attempts"])
