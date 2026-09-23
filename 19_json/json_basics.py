# JSON
# JSON basics

import json

security_event = {
    "username": "admin",
    "status": "failed",
    "ip_address": "192.168.1.25",
    "attempts": 3,
    "blocked": True
}

json_data = json.dumps(security_event, indent=4)

print("Security Event:")
print(json_data)
