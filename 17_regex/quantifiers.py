# Regular Expressions
# Regex quantifiers

import re

text = "User123 ID45 Code7890"

three_digits = re.findall(r"\d{3}", text)
one_or_more_digits = re.findall(r"\d+", text)

print("Three-digit matches:", three_digits)
print("One or more digits:", one_or_more_digits)
