# os & pathlib
# Checking whether a path is a file or directory

import os

file_path = "sample.txt"
directory_path = "security_reports"

if os.path.isfile(file_path):
    print(file_path, "is a file.")

if os.path.isdir(directory_path):
    print(directory_path, "is a directory.")
