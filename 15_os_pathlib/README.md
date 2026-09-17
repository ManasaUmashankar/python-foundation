The os Module
----------------


Explanation

The os module provides functions for interacting with the operating system.

It can be used to work with:

Files
Directories
Paths
Environment information
Operating-system functionality
Definition

os is a built-in Python module that provides an interface for interacting with operating-system features.

Importing os
import os
Cybersecurity Connection

Cybersecurity scripts often need to inspect files and directories, locate logs, check system information, and automate repetitive filesystem tasks.

2. Operating System Information
Explanation

Python can identify the operating-system family using os.name.

Code Example
import os

print("Operating System:", os.name)
Expected Output

On Windows:

Operating System: nt

On Linux:

Operating System: posix
Definition

os.name provides a simple identifier for the operating-system family.

Cybersecurity Connection

Security tools sometimes need to behave differently depending on whether they are running on Windows, Linux, or another operating-system family.

3. Current Working Directory
Explanation

The current working directory, or CWD, is the directory from which Python is currently executing the program.

Python can find it using os.getcwd().

Code Example
import os

current_directory = os.getcwd()

print("Current Directory:", current_directory)
Definition

os.getcwd() returns the current working directory.

Cybersecurity Connection

A security script may need to know its current location before searching for logs, configuration files, reports, or other resources.

4. Listing Files and Folders
Explanation

The os.listdir() function returns the files and directories inside a specified location.

Code Example
import os

items = os.listdir(".")

for item in items:
    print(item)
Definition

os.listdir() returns the names of files and directories in a given directory.

. means the current directory.

Cybersecurity Connection

Directory listing is useful when creating tools that inspect a system for files, logs, configuration files, or other resources.

5. Creating a Directory
Explanation

Python can create a new directory using os.mkdir().

Code Example
import os

os.mkdir("security_reports")

print("Directory created successfully.")
Expected Output
Directory created successfully.

A new directory called security_reports will be created.

Definition

os.mkdir() creates a single new directory.

Important Point

If the directory already exists, Python raises a FileExistsError.

Cybersecurity Connection

Automation tools can create directories for:

Scan reports
Logs
Backups
Investigation data
Security results
6. Checking Whether a File or Directory Exists
Explanation

Before accessing a file or directory, it is often useful to check whether it exists.

The os.path.exists() function can do this.

Code Example
import os

if os.path.exists("sample.txt"):
    print("File or directory exists.")
else:
    print("File or directory does not exist.")
Definition

os.path.exists() returns True if the specified path exists and False otherwise.

Cybersecurity Connection

Checking existence prevents scripts from blindly trying to access resources that may not be available.

7. Checking Files and Directories Separately
Explanation

Sometimes we need to know whether a path points specifically to a file or a directory.

Python provides:

os.path.isfile()
os.path.isdir()
Code Example
import os

if os.path.isfile("sample.txt"):
    print("It is a file.")

if os.path.isdir("security_reports"):
    print("It is a directory.")
Definitions

os.path.isfile() checks whether a path points to a file.

os.path.isdir() checks whether a path points to a directory.

Cybersecurity Connection

Security tools often need to distinguish between files and directories when scanning or processing filesystem data.

8. Joining File Paths
Explanation

Paths can be different on different operating systems.

Instead of manually writing path separators, Python provides os.path.join().

Code Example
import os

folder = "security_reports"
filename = "scan.txt"

file_path = os.path.join(folder, filename)

print(file_path)
Expected Output

On Windows, it may look like:

security_reports\scan.txt

On Linux/macOS, it may look like:

security_reports/scan.txt
Definition

os.path.join() combines path components into a valid filesystem path.

Cybersecurity Connection

Using proper path handling makes security scripts more portable across different operating systems.

9. The pathlib Module
Explanation

pathlib provides a modern and convenient way to work with filesystem paths.

Instead of treating paths only as strings, pathlib represents them as Path objects.

Definition

pathlib is a Python module that provides object-oriented tools for working with filesystem paths.

Importing Path
from pathlib import Path
Creating a Path
from pathlib import Path

file_path = Path("sample.txt")

print(file_path)
Cybersecurity Connection

pathlib makes filesystem automation cleaner and easier to maintain, which is useful when building security utilities.

10. Checking Paths with pathlib
Explanation

A Path object provides methods such as:

exists()
is_file()
is_dir()
Code Example
from pathlib import Path

path = Path("sample.txt")

if path.exists():
    print("Path exists.")

if path.is_file():
    print("It is a file.")
Expected Output
Path exists.
It is a file.
Cybersecurity Connection

These checks can be used when verifying whether security logs, reports, or configuration files are available before processing them.

11. Listing Directory Contents with pathlib
Explanation

Path.iterdir() allows us to iterate through the contents of a directory.

Code Example
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():
    print(item)
Definition

iterdir() returns the files and directories contained inside a directory.

Cybersecurity Connection

This can form the basis of a filesystem inspection tool that identifies and processes files automatically.

12. Creating Directories with pathlib
Explanation

Path.mkdir() can create directories.

Code Example
from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

print("Reports directory is ready.")
Definition

mkdir() creates a directory.

exist_ok=True prevents an error if the directory already exists.

Cybersecurity Connection

Security automation scripts can automatically prepare directories for reports, logs, or scan results.

13. Getting File Information
Explanation

Python can retrieve basic information about files using Path.stat().

Code Example
from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists():
    information = file_path.stat()

    print("File Size:", information.st_size, "bytes")
Definition

stat() returns information about a filesystem object.

st_size represents the file size in bytes.

Cybersecurity Connection

File properties can be useful when investigating files or monitoring changes in a filesystem.

14. os vs pathlib

Both modules can work with files and directories.

os	pathlib
Older and widely used	Modern path interface
Uses functions	Uses Path objects
os.path.exists()	Path.exists()
os.path.isfile()	Path.is_file()
os.path.isdir()	Path.is_dir()
os.listdir()	Path.iterdir()
os.mkdir()	Path.mkdir()
os.path.join()	/ or Path operations
Example

Using os:

import os

path = os.path.join("reports", "scan.txt")

Using pathlib:

from pathlib import Path

path = Path("reports") / "scan.txt"

Both approaches are valid.

For new Python projects, pathlib is often more convenient for path-related operations
