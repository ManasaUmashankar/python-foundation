# File Handling
# Working with file paths

from pathlib import Path


file_path = Path("sample.txt")

if file_path.exists():
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
else:
    print("File not found.")
