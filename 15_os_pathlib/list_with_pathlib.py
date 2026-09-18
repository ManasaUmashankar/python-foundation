# os & pathlib
# Listing files and folders using pathlib

from pathlib import Path

current_directory = Path(".")

print("Files and Folders:")
print("------------------")

for item in current_directory.iterdir():
    print(item)
