## File Handling

Overview
File handling allows Python programs to store, retrieve, update, and process information outside the running program.Until now, most of our programs stored data temporarily in variables. Once the program stopped, that data was lost.
File handling allows us to make data persistent by storing it in files such as:
.txt
.log
.csv
.json

File handling is especially important in cybersecurity because security tools frequently work with:
Security logs
System reports
Configuration files
Scan results
Incident notes
Backup data
Investigation records

1. Opening Files
Explanation
Before Python can read from or write to a file, the file must be opened.
Python provides the built-in open() function for this.

Definition
open() creates a connection between the Python program and a file.

Syntax
```
file = open("filename.txt", "mode")
```
The first argument is the file name or path.
The second argument specifies what we want to do with the file.

Common File Modes
Mode	Meaning
r	Read
w	Write; creates or overwrites
a	Append
r+	Read and write
x	Create a new file
Cybersecurity Connection

Security programs often need to open files containing logs, reports, configuration information, or investigation data.

2. Reading a File
   
Explanation
The read() method reads the contents of an opened file.

Definition
read() returns the contents of the file as a string.

Code Example
```
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

Expected Output
Cybersecurity is about protecting systems and data.
Python can automate many security tasks.

Important Point
When a file is opened manually, it should be closed using:
```
file.close()
```
This releases the file resource.

## **Cybersecurity Connection**

Reading files is the foundation of many security tasks, especially log analysis and processing security reports.

3. Using with open()
Explanation
Python provides a safer and cleaner way to work with files using the with statement.

Definition
A context manager automatically handles the file resource and closes the file when the with block finishes.

#Code Example
```
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```
The file is automatically closed after the block finishes.

Why Is It Better?
Using with open():

Automatically closes the file
Reduces resource leaks
Makes code easier to read
Safely handles cleanup when errors occur
Cybersecurity Connection

Security scripts may process many files. Automatically closing files helps prevent resource problems during automation.

4. Writing to a File
   
Explanation
The w mode allows Python to write data into a file.
If the file does not exist, Python creates it.
If the file already exists, its previous contents are overwritten.

Code Example
```
with open("output.txt", "w") as file:
    file.write("Security analysis started.\n")
    file.write("No threats detected.\n")

print("File written successfully.")
```
Expected Output
File written successfully.

The resulting output.txt contains:

Security analysis started.
No threats detected.
Important Warning

w mode can overwrite existing information.

For example:
```
with open("security.log", "w") as file:
```
could erase previously stored log information.

Cybersecurity Connection

Accidentally overwriting logs or investigation data can cause data loss, so choosing the correct file mode is important.

5. Appending to a File
6. 
Explanation
The a mode adds new data to the end of an existing file.
It does not remove the previous contents.

#Code Example
```
with open("output.txt", "a") as file:
    file.write("Security scan completed.\n")

print("Data appended successfully.")
```
Expected Output
Data appended successfully.
The new line is added after the existing contents.

## **Cybersecurity Connection**

Appending is extremely useful for logs.
Security events usually need to be added over time instead of replacing previous events.

For example:
Login attempt detected.
Failed login detected.
Security scan completed.

6. Reading a File Line by Line
Explanation
Instead of reading an entire file at once, Python can process it one line at a time.
This is especially useful when working with large files.

Code Example
```
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
```
Definition
Iterating over a file processes each line individually.

What Does strip() Do?
strip() removes unnecessary whitespace from the beginning and end of a string.
It also removes the newline character at the end of a line.

## **Cybersecurity Connection**

Security logs can contain thousands or millions of lines.
Processing them line by line allows a program to search for:

Failed login attempts
Suspicious IP addresses
Authentication events
Error messages
Potential attack indicators

7. Reading Lines Using readlines()
Explanation
The readlines() method reads all lines from a file and stores them in a list.

Code Example
```
with open("sample.txt", "r") as file:
    lines = file.readlines()

for number, line in enumerate(lines, start=1):
    print(number, ":", line.strip())
```
Definition
readlines() returns a list where each element represents one line from the file.
enumerate()
enumerate() allows us to access both:

The position/number
The value
Expected Output
1 : Cybersecurity is about protecting systems and data.
2 : Python can automate many security tasks.
Cybersecurity Connection

Line numbers can be useful during log investigation because they help identify the exact location of suspicious information.

8. File Modes

The mode determines how Python interacts with a file.

Read Mode — r

Used to read an existing file.

with open("sample.txt", "r") as file:
    print(file.read())
Write Mode — w

Used to create or overwrite a file.

with open("output.txt", "w") as file:
    file.write("New data")
Append Mode — a

Used to add data to the end of a file.

with open("output.txt", "a") as file:
    file.write("Additional data")
Exclusive Creation — x

Creates a new file and raises an error if it already exists.

with open("new_file.txt", "x") as file:
    file.write("Created successfully")
Security Consideration

Choosing the wrong file mode can cause unintended data loss.

For example, opening a security log with w can overwrite historical records.

9. Working with File Paths
Explanation
A file may not always be located in the same directory as the Python program.
A path tells Python where a file is located.
Python's pathlib module provides an object-oriented way to work with paths.

Code Example
```
from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists():
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
else:
    print("File not found.")
```

Definitions
Path represents a filesystem path.
exists() checks whether the path exists.

## **Cybersecurity Connection**

Security automation often needs to locate:

System logs
Application logs
Configuration files
Scan reports
Backup directories



10. Handling File Errors
Explanation
Files can be missing or inaccessible.
Python provides exceptions for these situations.
One common exception is FileNotFoundError.

Code Example
try:
```
    with open("security_log.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: security_log.txt was not found.")
```
Expected Output
Error: security_log.txt was not found.

Definition
FileNotFoundError occurs when Python cannot find the requested file or directory.

## **Cybersecurity Connection**

A security automation script should handle missing logs or configuration files in a controlled way instead of crashing unexpectedly.

11. Mini Project — File-Based Notes System
Explanation
The Day 4 mini project combines the file-handling concepts learned throughout the day.

The program can:
Add a note
Save the note to a file
View saved notes
Handle a missing notes file

#Code Example
```
def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()

        if notes:
            print("\nYour Notes:")
            print("-----------")
            print(notes)
        else:
            print("No notes found.")

    except FileNotFoundError:
        print("No notes file found.")


def main():
    print("File-Based Notes System")
    print("-----------------------")
    print("1. Add Note")
    print("2. View Notes")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
```
##  **Cybersecurity Connection**

This demonstrates persistent storage.
The same concepts can later be used for:

Security event storage
Incident notes
Scan results
Security reports
Backup automation
Log processing


12. Important File-Handling Concepts
read() = Reads the entire file as a string.

content = file.read()
readlines()

Reads all lines and returns them as a list.

lines = file.readlines()
write()

Writes data into a file.

file.write("Hello\n")
strip()

Removes surrounding whitespace.

line.strip()
close()

Closes a manually opened file.

file.close()
with

Automatically handles file cleanup.

with open("file.txt", "r") as file:
    content = file.read()
    
13. File Handling vs Memory
    
Explanation
A variable stores information temporarily while the program is running.

For example:
```
note = "Security scan completed."
```
Once the program ends, the variable is gone.

A file provides persistent storage:

with open("notes.txt", "w") as file:
    file.write("Security scan completed.")

The information remains in the file after the program exits.

## **Cybersecurity Connection**

Security applications need persistent data because logs, reports, scan results, and investigation records must survive after a program closes.

14. Cybersecurity Applications of File Handling
Log Analysis
Read authentication or system logs and search for suspicious activity.

Security Reports
Save scan results and findings to files.

Incident Response
Store investigation notes and collected information.

File Integrity
Read files and later calculate hashes to detect modifications.

Automation
Process, organize, and back up large numbers of files.

Configuration Management
Read configuration information used by security tools.

15. Security Considerations
Avoid Accidental Overwriting

-Be careful when using w mode
-Validate File Paths
-Do not blindly trust paths supplied by users.
-Handle Missing Files
-Use appropriate exception handling.
-Protect Sensitive Information
-Do not unnecessarily store passwords, API keys, or other secrets in plain text.
-Be Careful With Logs
-Logs can contain usernames, IP addresses, timestamps, system details, and other sensitive information.
-Use Appropriate Permissions
-Security-sensitive files should not automatically be accessible to everyone.
