# Regular Expressions
# Finding matches with finditer()

import re

text = "Failed login. Failed password. Successful login."

pattern = r"Failed"

matches = re.finditer(pattern, text)

print("Matches Found:")
print("--------------")

for match in matches:
    print("Text:", match.group())
    print("Position:", match.start())
