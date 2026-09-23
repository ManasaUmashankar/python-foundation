# Regex Security Practice
# Failed Login Detector

import re

log = "2026-09-21 10:30 Failed login for admin from 192.168.1.25"

pattern = r"failed login"

result = re.search(pattern, log, re.IGNORECASE)

if result:
    print("Failed login detected.")
else:
    print("No failed login detected.")
