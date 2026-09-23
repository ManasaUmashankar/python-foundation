# Regular Expressions
# search() vs match()

import re

text = "ERROR: Failed login attempt."

search_result = re.search(r"Failed", text)
match_result = re.match(r"ERROR", text)

if search_result:
    print("search(): Pattern found.")

if match_result:
    print("match(): Pattern found at the beginning.")
