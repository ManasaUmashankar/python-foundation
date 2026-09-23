# Regex Security Practice
# Suspicious Pattern Detector

import re

log = "Access denied for user admin"

pattern = r"failed|denied|unauthorized|blocked"

result = re.search(pattern, log, re.IGNORECASE)

if result:
    print("Suspicious pattern detected:", result.group())
else:
    print("No suspicious pattern detected.")
