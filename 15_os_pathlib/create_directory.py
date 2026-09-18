# os & pathlib
# Creating a directory

import os

directory_name = "security_reports"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print("Directory created successfully.")
else:
    print("Directory already exists.")
