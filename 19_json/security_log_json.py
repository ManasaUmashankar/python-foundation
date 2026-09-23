# JSON
# Mini Project: Security Log JSON Manager

import json

file_name = "security_logs.json"

security_event = {
    "timestamp": "2026-09-22 10:30",
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event": "failed_login",
    "severity": "medium"
}

with open(file_name, "w") as file:
    json.dump(security_event, file, indent=4)

print("Security event saved successfully.")

with open(file_name, "r") as file:
    data = json.load(file)

print("\nSecurity Event")
print("--------------")
print("Timestamp:", data["timestamp"])
print("Username:", data["username"])
print("IP Address:", data["ip_address"])
print("Event:", data["event"])
print("Severity:", data["severity"])
