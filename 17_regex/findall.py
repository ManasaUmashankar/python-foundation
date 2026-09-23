# Regular Expressions
# Finding all matches

import re

text = "Failed login from 192.168.1.10 and 10.0.0.25."

pattern = r"\d+\.\d+\.\d+\.\d+"

ip_addresses = re.findall(pattern, text)

print("IP Addresses Found:")
print(ip_addresses)
