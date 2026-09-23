# JSON
# Converting a Python object into a JSON string

import json

security_event = {
    "username": "admin",
    "status": "failed",
    "ip_address": "192.168.1.25",
    "attempts": 3
}

json_data = json.dumps(security_event, indent=4)

print("JSON String:")
print(json_data)
