Python Intermediate: File & Directory Inspector
Objective

Learn how to inspect files and directories using Python and apply filesystem concepts to basic cybersecurity tasks.

By the end of this topic, you will be able to:

List files and directories
Identify files and directories
Check file properties
Filter files by extension
Search for specific files
Inspect directory contents
Build a basic filesystem inspection tool
Topics Covered
Listing Files and Directories
Identifying Files and Directories
File Properties
Filtering Files
Finding Files
Directory Inspection
File & Directory Inspector — Mini Project
1. Listing Files and Directories
Definition

Listing files and directories means displaying the contents of a particular directory.

Python can perform this using os.listdir() or Path.iterdir().

Explanation

Directory listing is one of the basic filesystem operations.

It allows a program to see what files and folders are present in a location.

Syntax
import os

os.listdir("path")

Using pathlib:

from pathlib import Path

Path("path").iterdir()
Code Example
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():
    print(item)
Expected Output
README.md
list_files.py
filter_files.py
find_files.py

The output depends on the contents of the directory.

Cybersecurity Connection

Security tools often inspect directories to locate:

Log files
Configuration files
Reports
Suspicious files
Evidence files
2. Identifying Files and Directories
Definition

A filesystem path can represent either a file or a directory.

Python provides methods to determine which type it is.

Explanation

With pathlib, we can use:

.is_file() → checks for a file
.is_dir() → checks for a directory
Syntax
path.is_file()
path.is_dir()
Code Example
from pathlib import Path

path = Path("sample.txt")

if path.is_file():
    print("This is a file.")
elif path.is_dir():
    print("This is a directory.")
Expected Output
This is a file.
Cybersecurity Connection

A security scanner needs to distinguish between files and directories before processing them.

3. File Properties
Definition

File properties are pieces of information about a file, such as its size.

Explanation

pathlib provides .stat() to retrieve filesystem information.

For example:

path.stat().st_size

returns the file size in bytes.

Syntax
properties = path.stat()
properties.st_size
Code Example
from pathlib import Path

file = Path("sample.txt")

print("File:", file.name)
print("Size:", file.stat().st_size, "bytes")
Expected Output
File: sample.txt
Size: 96 bytes

The actual size depends on the file contents.

Cybersecurity Connection

File properties can help identify unusual files during security investigations, such as unexpectedly large files or files that have changed.

4. Filtering Files
Definition

Filtering files means selecting files that match a particular condition, such as a specific extension.

Explanation

For example, a program can select only:

.log files
.txt files
.csv files
.py files
Syntax
if item.suffix == ".log":
Code Example
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():
    if item.is_file() and item.suffix == ".log":
        print(item)
Expected Output
security.log
access.log
Cybersecurity Connection

Filtering is useful when a security analyst wants to inspect only specific types of files, especially log files.

5. Finding Files
Definition

Finding files means searching a directory for files that match a particular name or pattern.

Explanation

pathlib provides .glob() for pattern-based searches.

Syntax
directory.glob("*.log")
Code Example
from pathlib import Path

directory = Path(".")

for file in directory.glob("*.log"):
    print(file)
Expected Output
security.log
access.log
system.log
Cybersecurity Connection

Searching for files is useful for locating:

Security logs
Configuration files
Reports
Potentially suspicious files
6. Directory Inspection
Definition

Directory inspection means examining the contents and basic properties of files and folders within a directory.

Explanation

A directory inspector can combine several concepts:

Directory listing
File/directory identification
File size
File extension
Code Example
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():

    if item.is_file():
        print(
            "FILE:",
            item.name,
            "| Size:",
            item.stat().st_size,
            "bytes"
        )

    elif item.is_dir():
        print("DIR:", item.name)
Expected Output
FILE: README.md | Size: 2500 bytes
FILE: list_files.py | Size: 300 bytes
DIR: security_logs
DIR: reports
Cybersecurity Connection

Directory inspection is a basic technique used in:

Filesystem analysis
Incident response
Log investigation
Security automation
7. File & Directory Inspector — Mini Project
Objective

Build a Python program that scans a directory and displays useful information about its contents.

Features

The program will:

List files
Identify directories
Display file sizes
Display file extensions
Provide a simple filesystem overview
Cybersecurity Connection

This project introduces the foundation of automated filesystem inspection, which can later be extended into security monitoring and investigation tools.
