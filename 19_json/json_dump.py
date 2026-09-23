# JSON
# Writing data to a JSON file

import json

security_event = {
    "username": "admin",
    "status": "failed",
    "ip_address": "192.168.1.25",
    "attempts": 3
}

with open("security_event.json", "w") as file:
    json.dump(security_event, file, indent=4)

print("JSON file created successfully.")
