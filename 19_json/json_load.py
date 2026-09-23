# JSON
# Reading JSON data from a file

import json

with open("security_log.json", "r") as file:
    data = json.load(file)

print("Security Log:")
print(data)

print("\nUsername:", data["username"])
print("IP Address:", data["ip_address"])
print("Status:", data["status"])
