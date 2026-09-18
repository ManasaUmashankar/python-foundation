#os & pathlib🐍


##Objective
The objective of this topic is to learn how Python interacts with the operating system and filesystem, and how to work efficiently with files, directories, and paths using the os and pathlib modules.
These concepts are useful for building automation scripts, file-management tools, system utilities, and cybersecurity-related programs.

#Topics Covered
os Module Basics
Current Working Directory
Listing Files and Folders
Creating Directories
Checking Path Existence
Checking Files and Directories
Joining Paths
pathlib Basics
Checking Paths with pathlib
Listing Contents with pathlib
Creating Directories with pathlib
File Properties
Path Operations
os vs pathlib
Mini Project — Directory & File Inspector

#1. os Module Basics
Definition:- The os module is a built-in Python module that provides functions for interacting with the operating system.

Explanation:- The os module can be used to work with:
                       * Files
                       * Directories
                       * Paths
                       * Operating-system information
                       * Environment information

It allows Python programs to perform operations that interact with the computer's filesystem.

Syntax
```
import os
Code Example
import os

print("Operating System:", os.name)
print("Current Directory:", os.getcwd())
```
## Expected Output
On Windows, the output may look like:

Operating System: nt

Current Directory: C:\Users\Username\Python\15_os_pathlib

The exact directory depends on where the program is executed.

Cybersecurity Connection

Cybersecurity scripts often need to identify the operating system and current location before performing filesystem operations.

# 2. Current Working Directory
Definition :- The Current Working Directory (CWD) is the directory from which a Python program is currently running.

Explanation:-Python provides os.getcwd() to find the current working directory.
Knowing the current directory is useful when a program needs to locate files or folders relative to its current location.

Syntax:-
```
os.getcwd()
Code Example
import os

current_directory = os.getcwd()

print("Current Working Directory:")
print(current_directory)
```
Expected Output
The program displays the current working directory.

For example:
C:\Users\Username\Python\15_os_pathlib

The exact path depends on the system and execution location.

~~~ Cybersecurity Connection
Security scripts may need to locate logs, configuration files, reports, or other security-related resources from the current directory.
~~~

##3. Listing Files and Folders
Definition

os.listdir() returns the names of files and directories contained inside a specified directory.

Explanation
A program can use os.listdir() to inspect the contents of a directory.
. represents the current directory.

##Syntax
```
os.listdir(path)
Code Example
import os

items = os.listdir(".")

for item in items:
    print(item)
```
Expected Output:-
The output depends on the files and folders in the directory.

For example:
-README.md
-os_basics.py
-current_directory.py
-sample.txt

~~~Cybersecurity Connection
Listing directory contents can help security tools inspect systems for logs, configuration files, reports, and potentially suspicious files.
~~~

# 4. Creating Directories
Definition:- os.mkdir() creates a new directory at the specified location.

Explanation:- Python can create directories automatically instead of requiring the user to create them manually.
If the directory already exists, os.mkdir() raises a FileExistsError.

##Syntax
```
os.mkdir("directory_name")
Code Example
import os

os.mkdir("security_reports")

print("Directory created successfully.")
```
Expected Output:

Directory created successfully.

A directory named security_reports will be created.

Cybersecurity Connection

Security automation programs can create directories for:

Security reports
Scan results
Investigation data
Backups
Logs

#5. Checking Path Existence
Definition:- os.path.exists() checks whether a specified file or directory exists.

Explanation:- The function returns a Boolean value:

True — path exists
False — path does not exist

Checking a path before accessing it can prevent unexpected errors.

Syntax
```
os.path.exists(path)
Code Example
import os

path = "sample.txt"

if os.path.exists(path):
    print("Path exists.")
else:
    print("Path does not exist.")
```
Expected Output
If sample.txt exists:
Path exists.
Otherwise:
Path does not exist.

~~~Cybersecurity Connection
Security scripts can check whether important log files, reports, or configuration files exist before processing them.
~~~

#6. Checking Files and Directories
Definition:-Python provides separate functions to determine whether a path represents a file or a directory.

os.path.isfile() checks for a file.
os.path.isdir() checks for a directory.

Explanation:-A filesystem path can point to different types of objects.
These functions allow a program to identify the type before performing an operation.

#Syntax
```
os.path.isfile(path)
os.path.isdir(path)
Code Example
import os

if os.path.isfile("sample.txt"):
    print("sample.txt is a file.")

if os.path.isdir("security_reports"):
    print("security_reports is a directory.")
```
Expected Output
If both exist:
sample.txt is a file.
security_reports is a directory.

~~~Cybersecurity Connection
Security tools often need to distinguish between files and directories before scanning or processing them.
~~~

#7. Joining Paths
Definition:os.path.join() combines multiple path components into a valid filesystem path.

Explanation:-Different operating systems use different path separators.

For example:

-Windows uses \
-Linux and macOS commonly use /

-os.path.join() automatically uses the appropriate separator for the operating system.

Syntax:
```
os.path.join(path1, path2)
Code Example
import os

folder = "security_reports"
filename = "scan.txt"

file_path = os.path.join(folder, filename)

print(file_path)
```
Expected Output

On Windows:
security_reports\scan.txt

On Linux/macOS:
security_reports/scan.txt

##Cybersecurity Connection

Proper path construction makes cybersecurity scripts more portable across different operating systems.

#8. pathlib Basics

Definition:-pathlib is a built-in Python module that provides an object-oriented approach to working with filesystem paths.

Explanation:-Unlike traditional path handling where paths are often treated as strings, pathlib provides a Path object.
This makes many filesystem operations easier to read and manage.

Syntax:
```
from pathlib import Path
Code Example
from pathlib import Path

file_path = Path("sample.txt")

print(file_path)
```

Expected Output:
sample.txt

#Cybersecurity Connection:-
pathlib provides a clean approach for developing cybersecurity utilities that work with files and directories.

#9. Checking Paths with pathlib
Definition:-A Path object provides methods to determine whether a path exists and whether it represents a file or directory.

Important methods include:
```
exists()
is_file()
is_dir()
Explanation
```
These methods perform similar checks to the os.path functions, but they are called directly on a Path object.

Syntax:-
```
path.exists()
path.is_file()
path.is_dir()
Code Example
from pathlib import Path

path = Path("sample.txt")

if path.exists():
    print("Path exists.")

if path.is_file():
    print("It is a file.")
```
Expected Output:-
Path exists.
It is a file.

#Cybersecurity Connection:-
These checks can be used to verify that security logs, reports, configuration files, or investigation files are available before processing them.

##10. Listing Contents with pathlib
Definition:- Path.iterdir() returns the contents of a directory as Path objects.

Explanation:-iterdir() allows us to loop through files and directories inside a folder.
It is similar to os.listdir(), but it works directly with Path objects.

Syntax
```
path.iterdir()
Code Example
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():
    print(item)
```
Expected Output

The program displays the paths of files and directories inside the current directory.

#For example:

15_os_pathlib\README.md

15_os_pathlib\os_basics.py

15_os_pathlib\current_directory.py

##Cybersecurity Connection

iterdir() can be used as the foundation for tools that inspect and process filesystem contents automatically.

#11. Creating Directories with pathlib
Definition:-Path.mkdir() creates a new directory.

Explanation:-pathlib provides a cleaner way to create directories using a Path object.

The exist_ok=True argument prevents an error if the directory already exists.

Syntax:-
```
path.mkdir(exist_ok=True)
Code Example
from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

print("Reports directory is ready.")
```

#Expected Output:-
Reports directory is ready.

##Cybersecurity Connection

Security programs can automatically create folders for:

-Reports
-Logs
-Scan results
-Backups
-Investigation files

#12. File Properties
Definition

Path.stat() returns information about a filesystem object.

One commonly used property is st_size, which represents the file size in bytes.

Explanation:- File properties can provide useful information about a file without opening and reading its contents.

Syntax
```
path.stat()
Code Example
from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists():
    information = file_path.stat()

    print("File Size:", information.st_size, "bytes")
```

Expected Output:-
The exact size depends on the contents of sample.txt.

For example:

-File Size: 95 bytes

##Cybersecurity Connection
File metadata can be useful during security investigations and filesystem monitoring.

#13. Path Operations
Definition:- pathlib provides properties that allow us to access different components of a filesystem path.

Important properties include:

-name
-parent
-suffix
-stem

Explanation:-These properties allow a program to work with parts of a path without manually manipulating strings.

-name
Returns the complete file or directory name.

-parent
Returns the directory containing the path.

-suffix
Returns the file extension.

-stem
Returns the filename without its extension.

Syntax
```
path.name
path.parent
path.suffix
path.stem
Code Example
from pathlib import Path

file_path = Path("security_reports/scan.txt")

print("Name:", file_path.name)
print("Parent:", file_path.parent)
print("Suffix:", file_path.suffix)
print("Stem:", file_path.stem)
```

Expected Output:-

Name: scan.txt
Parent: security_reports
Suffix: .txt
Stem: scan

##Cybersecurity Connection:-Path operations can help security tools automatically identify and organize log files, scan reports, and other security-related files.

#14. os vs pathlib

Explanation:-Both os and pathlib can be used to work with files, directories, and paths.

os provides traditional function-based operations, while pathlib provides an object-oriented approach.

Operation	os	pathlib
Check existence	os.path.exists()	Path.exists()
Check file	os.path.isfile()	Path.is_file()
Check directory	os.path.isdir()	Path.is_dir()
List contents	os.listdir()	Path.iterdir()
Create directory	os.mkdir()	Path.mkdir()
Join paths	os.path.join()	Path() / /

Code Example — os
```
import os

path = os.path.join("reports", "scan.txt")

print(path)
Code Example — pathlib
from pathlib import Path

path = Path("reports") / "scan.txt"

print(path)
```

#Cybersecurity Connection:-Both approaches can be useful in cybersecurity automation. Understanding both helps when working with existing scripts as well as writing new Python utilities.

#15. Mini Project — Directory & File Inspector

Definition:- A Directory & File Inspector is a program that examines a directory and displays information about the files and folders it contains.

Explanation:-
The project combines:
-pathlib
-Path validation
-Directory iteration
-File identification
-Directory identification
-File properties
-Functions
-User input

**The program accepts a directory path and displays its contents.

##Features
-Accept directory path from the user
-Check whether the directory exists
-Display the absolute path
-List files and directories
-Identify files and folders
-Display file sizes

##Code Example:
```
from pathlib import Path


def inspect_directory(directory):
    path = Path(directory)

    if not path.exists():
        print("Directory not found.")
        return

    if not path.is_dir():
        print("The specified path is not a directory.")
        return

    print("Directory:", path.resolve())
    print("\nContents:")
    print("---------")

    for item in path.iterdir():

        if item.is_file():
            print("[FILE]", item.name, "-", item.stat().st_size, "bytes")

        elif item.is_dir():
            print("[DIR] ", item.name)


def main():
    directory = input("Enter directory path: ")

    inspect_directory(directory)


if __name__ == "__main__":
    main()
```

#Expected Output:

The exact output depends on the directory being inspected.

#For example:
Enter directory path: .

Directory: C:\...\15_os_pathlib

[FILE] README.md - 5000 bytes

[FILE] os_basics.py - 180 bytes

[DIR] reports

##Cybersecurity Connection
A directory inspector is a basic example of filesystem inspection and automation.

#Similar concepts are used when security tools:

-Locate security logs
-Inspect directories
-Collect file metadata
-Search for specific files
-Organize investigation data

##16. Security Considerations
Avoid Uncontrolled File Operations
Do not automatically delete, overwrite, or modify files without proper validation.

Validate Paths
Paths supplied by users should be handled carefully.

Protect Sensitive Files
Security scripts should not unnecessarily expose confidential files or information.
Use Appropriate Permissions
Filesystem operations depend on the permissions of the user running the program.
Test Automation Safely
Filesystem automation should first be tested in a safe directory before being used with important data.

##17. Project Structure

The project contains:

-README.md
-os_basics.py
-current_directory.py
-list_directory.py
-create_directory.py
-check_path.py
-check_file_directory.py
-join_paths.py
-pathlib_basics.py
-path_checks.py
-list_with_pathlib.py
-create_directory_pathlib.py
-file_properties.py
-path_operations.py
-directory_file_inspector.py

##18. What I Learned
By completing this topic, I learned how to:
~~~
-Use the os module
-Identify the operating system
-Find the current working directory
-List files and folders
-Create directories
-Check whether paths exist
-Identify files and directories
-Join filesystem paths
-Use pathlib
-Work with Path objects
-List directory contents
-Create directories using pathlib
-Get file properties
-Work with path components
-Build a Directory & File Inspector
-Apply filesystem operations to cybersecurity automation
~~~
##19. Key Takeaway

os and pathlib allow Python programs to interact with the operating system and filesystem.
These concepts form an important foundation for Python automation and cybersecurity tools, especially when working with files, directories, logs, reports, and investigation data.
