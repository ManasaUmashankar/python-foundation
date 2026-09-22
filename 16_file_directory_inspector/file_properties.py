# File & Directory Inspector
# Getting file properties

from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists() and file_path.is_file():
    print("File Name:", file_path.name)
    print("Extension:", file_path.suffix)
    print("Size:", file_path.stat().st_size, "bytes")
else:
    print("File not found.")
