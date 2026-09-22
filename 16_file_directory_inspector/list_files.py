# File & Directory Inspector
# Listing files and directories

from pathlib import Path

directory = Path(".")

print("Directory Contents:")
print("-------------------")

for item in directory.iterdir():
    print(item)
