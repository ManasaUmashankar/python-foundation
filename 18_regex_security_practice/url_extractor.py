# Regex Security Practice
# URL Extractor

import re

text = "Visit https://example.com/security for more information."

pattern = r"https?://\S+"

result = re.search(pattern, text)

if result:
    print("URL:", result.group())
else:
    print("No URL found.")
