# os & pathlib
# Joining file paths

import os

folder = "security_reports"
file_name = "scan_report.txt"

file_path = os.path.join(folder, file_name)

print("Complete File Path:")
print(file_path)
