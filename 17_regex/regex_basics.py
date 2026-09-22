# Regular Expressions
# Regex basics

import re

text = "Security alert: Login attempt from user123."

pattern = r"\d+"

result = re.findall(pattern, text)

print("Numbers found:")
print(result)
