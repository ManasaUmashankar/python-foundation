# Regular Expressions
# Practical regex security practice

import re

log = "Failed login for admin from 192.168.1.25"

username = re.search(r"for (\w+)", log)
ip_address = re.search(r"\d+\.\d+\.\d+\.\d+", log)

print("Security Log:")
print(log)

if username:
    print("Username:", username.group(1))

if ip_address:
    print("IP Address:", ip_address.group())
