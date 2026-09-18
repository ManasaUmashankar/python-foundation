# os & pathlib
# Checking whether a path exists

import os

path = "security_reports"

if os.path.exists(path):
    print("Path exists.")
else:
    print("Path does not exist.")
