#PYTHON FOUNDATION 4
------

# File Handling & Error Handling

## 1. File Handling

Python can work with files stored on a computer.

File handling is useful for:

- Reading data
- Writing information
- Storing program data
- Processing logs
- Creating reports
- Automating file operations

---

## 2. Opening a File

Python uses the `open()` function to open files.

```python
file = open("example.txt", "r")

The second argument specifies the file mode.

Common File Modes
Mode	Purpose
r	Read
w	Write
a	Append
x	Create a new file
3. Reading a File
with open("example.txt", "r") as file:
    content = file.read()

print(content)

Using with automatically closes the file after the operation.

4. Reading Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line)

Reading line by line is useful when working with large files such as log files.

5. Writing to a File
with open("example.txt", "w") as file:
    file.write("Python is useful for cybersecurity.")

The w mode creates the file if it does not exist.

Important: w can overwrite existing content.

6. Appending to a File

The a mode adds new content without removing existing content.

with open("example.txt", "a") as file:
    file.write("\nNew information")
7. File Handling + Cybersecurity

File handling is especially useful in cybersecurity because security systems generate many files and logs.

Python can be used to:

Search logs
Detect suspicious activity
Extract important information
Count failed login attempts
Process security reports
Monitor files
Automate backups

Example:

with open("security.log", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print(line)

This is a simple example of detecting failed events in a log.

Error Handling
8. Why Error Handling?

Programs can encounter unexpected situations.

For example:

A user enters invalid input
A file does not exist
A number is divided by zero
A required resource is unavailable

Python provides try and except to handle errors.

9. try and except
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")

If the user enters something that cannot be converted into an integer, the program handles the error instead of crashing.

10. Handling File Errors
try:
    with open("example.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")

This is useful when working with files that may not exist.

11. Multiple Exceptions

Different errors can be handled separately.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
12. finally

The finally block runs whether an error occurs or not.

try:
    print("Running program")

except Exception:
    print("An error occurred")

finally:
    print("Program finished")
Python + Cybersecurity

Python is especially valuable in cybersecurity because it can automate repetitive tasks and process large amounts of information.

Some common applications include:

Log Analysis

Python can read and analyze system and security logs.

File Analysis

Python can inspect files and directories for specific patterns.

Automation

Python can automate repetitive administrative and security tasks.

Network Programming

Python can communicate with network services and work with sockets.

Data Processing

Python can process large amounts of structured or unstructured data.

Security Tools

Python can be used to create educational security tools and utilities.

My 10 Beginner Projects

I applied my Python fundamentals by building 10 beginner projects.

#	Project	Main Concepts
1	Calculator	Variables, input, operators, conditions
2	Number Guessing Game	Loops, conditions, random
3	Password Generator	Strings, loops, random
4	Palindrome Checker	Strings, conditions
5	Prime Number Checker	Loops, conditions
6	Text Analyzer	Strings, dictionaries, loops
7	File Organizer	os, shutil, conditions
8	Contact Book	Dictionaries, functions
9	Quiz Game	Lists, dictionaries, loops, conditions
10	Password Strength Checker	Strings, conditions, functions
What I Learned From These Projects

Building projects helped me understand how individual Python concepts work together.

For example:

Variables
    ↓
Conditions
    ↓
Loops
    ↓
Strings & Data Structures
    ↓
Functions
    ↓
Modules
    ↓
File Handling
    ↓
Practical Programs

Instead of only learning syntax, I used these concepts to build working programs.

What I Can Do Now

After completing my Python fundamentals, I can:

Write basic Python programs
Use variables and different data types
Take user input
Use operators
Write conditional statements
Use for and while loops
Work with strings
Work with lists and dictionaries
Create and use functions
Import Python modules
Work with files
Handle basic errors
Automate simple tasks
Build beginner-level command-line applications
Understand how Python can be applied to cybersecurity
Python Skills Checklist
 Python syntax
 Variables
 Data types
 Input and output
 Type conversion
 Operators
 Conditional statements
 Loops
 Strings
 Lists
 Dictionaries
 Functions
 Modules
 random
 string
 os
 shutil
 File handling
 Basic error handling
 Basic automation
 Beginner projects
Python → Cybersecurity

My learning goal is to gradually connect Python programming with cybersecurity.

Python Fundamentals
        ↓
Intermediate Python
        ↓
Automation
        ↓
File & Log Analysis
        ↓
Networking with Python
        ↓
Security Scripting
        ↓
Cybersecurity Projects

Python will become a supporting skill alongside my learning in:

Networking
Linux
Cybersecurity fundamentals
Problem solving
Security tools and labs
What I'm Learning Next

The next stage is Intermediate Python.

Topics I plan to explore include:

Object-Oriented Programming
Advanced functions
Lambda functions
List, set and dictionary comprehensions
Exception handling
Regular expressions
Working with JSON
APIs
Virtual environments
Python packages
Networking with Python
Automation
More advanced projects

The goal is to move from writing small beginner programs to building more structured and practical applications.

Final Foundation Summary

I started with basic Python syntax and gradually progressed toward practical programming.

I have now built 10 beginner projects and developed a foundation in programming concepts that I can apply to future cybersecurity work.

Learn
  ↓
Practice
  ↓
Build
  ↓
Document
  ↓
Apply to Cybersecurity
  ↓
Keep Improving
