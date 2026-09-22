# File & Directory Inspector
# Mini Project

from pathlib import Path

directory = Path(".")

print("File & Directory Inspector")
print("--------------------------")

for item in directory.iterdir():

    if item.is_file():
        print(
            "FILE  |",
            item.name,
            "| Size:",
            item.stat().st_size,
            "bytes",
            "| Extension:",
            item.suffix
        )

    elif item.is_dir():
        print("DIR   |", item.name)
