# Regular Expressions
# Regex groups

import re

text = "User: admin | IP: 192.168.1.25"

pattern = r"User:\s(\w+)\s\|\sIP:\s(\d+\.\d+\.\d+\.\d+)"

result = re.search(pattern, text)

if result:
    username = result.group(1)
    ip_address = result.group(2)

    print("Username:", username)
    print("IP Address:", ip_address)
