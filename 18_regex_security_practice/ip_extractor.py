# Regex Security Practice
# IP Address Extractor

import re

text = "Failed login detected from 192.168.1.25"

pattern = r"\d+\.\d+\.\d+\.\d+"

result = re.search(pattern, text)

if result:
    print("IP Address:", result.group())
else:
    print("No IP address found.")
