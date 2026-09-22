# File & Directory Inspector
# Inspecting directory contents

from pathlib import Path

directory = Path(".")

print("Directory Inspection")
print("--------------------")

for item in directory.iterdir():

    if item.is_file():
        print(
            "FILE |",
            item.name,
            "| Size:",
            item.stat().st_size,
            "bytes",
            "| Extension:",
            item.suffix
        )

    elif item.is_dir():
        print("DIR  |", item.name)
