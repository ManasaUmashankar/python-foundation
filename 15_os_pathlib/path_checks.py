# os & pathlib
# Checking paths using pathlib

from pathlib import Path

file_path = Path("sample.txt")
directory_path = Path("security_reports")

print("File exists:", file_path.exists())
print("Is file:", file_path.is_file())

print("\nDirectory exists:", directory_path.exists())
print("Is directory:", directory_path.is_dir())
