# File & Directory Inspector
# Checking whether a path is a file or directory

from pathlib import Path

path = Path("sample.txt")

if path.is_file():
    print("This is a file.")
elif path.is_dir():
    print("This is a directory.")
else:
    print("Path does not exist.")
