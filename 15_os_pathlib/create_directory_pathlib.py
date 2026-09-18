# os & pathlib
# Creating a directory using pathlib

from pathlib import Path

directory = Path("security_logs")

if not directory.exists():
    directory.mkdir()
    print("Directory created successfully.")
else:
    print("Directory already exists.")
