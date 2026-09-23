# JSON
# Converting a JSON string into a Python object

import json

json_data = '{"username": "admin", "status": "failed", "ip_address": "192.168.1.25"}'

data = json.loads(json_data)

print("Python Object:")
print(data)

print("\nUsername:", data["username"])
print("IP Address:", data["ip_address"])
print("Status:", data["status"])
