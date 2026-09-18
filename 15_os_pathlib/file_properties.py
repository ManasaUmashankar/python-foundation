# os & pathlib
# Getting file properties

from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists() and file_path.is_file():
    properties = file_path.stat()

    print("File:", file_path)
    print("Size:", properties.st_size, "bytes")
else:
    print("File not found.")
