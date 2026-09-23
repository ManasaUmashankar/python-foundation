# Regex Security Practice
# Email Address Extractor

import re

text = "Security report sent to analyst@example.com"

pattern = r"[\w.-]+@[\w.-]+\.\w+"

result = re.search(pattern, text)

if result:
    print("Email Address:", result.group())
else:
    print("No email address found.")
