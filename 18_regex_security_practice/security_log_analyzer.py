# Regex Security Practice
# Security Log Analyzer

import re

log = "2026-09-21 10:30 Failed login for admin from 192.168.1.25"

username = re.search(r"for (\w+)", log)
ip_address = re.search(r"\d+\.\d+\.\d+\.\d+", log)
failed_login = re.search(r"failed login", log, re.IGNORECASE)
suspicious_pattern = re.search(
    r"failed|denied|unauthorized|blocked",
    log,
    re.IGNORECASE
)

print("Security Log Analyzer")
print("---------------------")
print("Log:", log)

if failed_login:
    print("Event: Failed login")

if username:
    print("Username:", username.group(1))

if ip_address:
    print("IP Address:", ip_address.group())

if suspicious_pattern:
    print("Status: Investigation Required")
else:
    print("Status: No suspicious pattern detected.")
