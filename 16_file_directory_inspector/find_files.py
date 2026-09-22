# File & Directory Inspector
# Finding files using glob()

from pathlib import Path

directory = Path(".")

print("Log Files:")
print("----------")

for file in directory.glob("*.log"):
    print(file.name)
