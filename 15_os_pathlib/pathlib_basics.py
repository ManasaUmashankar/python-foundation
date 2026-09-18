# os & pathlib
# pathlib basics

from pathlib import Path

current_directory = Path.cwd()

print("Current Directory:")
print(current_directory)

file_path = Path("sample.txt")

print("\nFile Path:")
print(file_path)
