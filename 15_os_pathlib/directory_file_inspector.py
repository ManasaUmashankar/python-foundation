# os & pathlib
# Mini Project: Directory & File Inspector

from pathlib import Path

directory = Path(".")

print("Directory & File Inspector")
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
