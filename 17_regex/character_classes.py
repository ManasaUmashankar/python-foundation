# Regular Expressions
# Character classes

import re

text = "User123 logged in at 10:30."

uppercase = re.findall(r"[A-Z]", text)
digits = re.findall(r"\d", text)
words = re.findall(r"\w+", text)

print("Uppercase letters:", uppercase)
print("Digits:", digits)
print("Words:", words)
