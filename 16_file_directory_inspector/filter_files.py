# File & Directory Inspector
# Filtering files by extension

from pathlib import Path

directory = Path(".")

print("Python Files:")
print("-------------")

for item in directory.iterdir():
    if item.is_file() and item.suffix == ".py":
        print(item.name)
