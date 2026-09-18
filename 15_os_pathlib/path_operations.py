# os & pathlib
# Basic path operations

from pathlib import Path

file_path = Path("security_reports/scan_report.txt")

print("Full Path:", file_path)
print("File Name:", file_path.name)
print("File Name Without Extension:", file_path.stem)
print("File Extension:", file_path.suffix)
print("Parent Directory:", file_path.parent)
