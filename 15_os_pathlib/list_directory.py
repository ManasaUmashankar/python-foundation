# os & pathlib
# Listing files and folders

import os


items = os.listdir(".")

print("Files and Folders:")
print("------------------")

for item in items:
    print(item)
