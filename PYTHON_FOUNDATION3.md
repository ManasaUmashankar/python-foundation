#PYTHON FOUNDATION 3
------

# Functions, Modules & Python Libraries

## 1. Functions

A function is a reusable block of code that performs a specific task.

Functions help make programs:

- Easier to read
- Easier to maintain
- Reusable
- More organized

### Basic Function

```python
def greet():
    print("Hello!")
    
greet()
Function with Parameters
def greet(name):
    print("Hello", name)

greet("Manasa")
Multiple Parameters
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
return

The return statement sends a value back from a function.

def square(number):
    return number * number

result = square(5)
print(result)

Output:

25
2. Parameters vs Arguments

A parameter is the variable defined inside the function.

An argument is the actual value passed to the function.

def greet(name):   # name → parameter
    print("Hello", name)

greet("Manasa")    # "Manasa" → argument
3. Why Functions Matter in Cybersecurity

Functions are extremely useful when building security tools.

For example, instead of writing password validation code repeatedly:

def check_password(password):
    if len(password) >= 8:
        return True
    return False

The function can then be reused whenever password validation is required.

Functions are commonly used in:

Password checkers
Log analysis tools
Network scanners
File analysis scripts
Automation tools
Security utilities
Modules
4. What is a Module?

A module is a Python file containing code that can be reused in another Python program.

Python also provides many built-in modules.

Instead of writing everything from scratch, we can import existing functionality.

Example
import math

print(math.sqrt(25))

Output:

5.0
5. Importing Specific Functions

Instead of importing the entire module:

from math import sqrt

print(sqrt(25))
Useful Python Modules

Some modules that are especially useful for my learning path are:

Module	Purpose
math	Mathematical operations
random	Random values and selections
string	String constants and character sets
os	Operating system interaction
shutil	File and directory operations
datetime	Date and time
re	Regular expressions
json	Working with JSON data
Random Module

The random module is useful when generating random values.

import random

number = random.randint(1, 10)

print(number)

This generates a random integer between 1 and 10.

Random Choice
import random

items = ["red", "blue", "green"]

choice = random.choice(items)

print(choice)

This concept was useful in my:

Password Generator

and

Number Guessing Game

projects.

String Module

The string module provides useful character sets.

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

These can be combined when creating random passwords.

Example:

import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(12):
    password += random.choice(characters)

print(password)

This connects directly to my Password Generator project.

OS Module

The os module allows Python to interact with the operating system.

Example:

import os

print(os.getcwd())

This displays the current working directory.

Listing Files
import os

files = os.listdir()

print(files)

This can be useful for automation and file analysis.

Shutil Module

The shutil module provides higher-level file operations.

For example:

import shutil

shutil.copy("file.txt", "backup.txt")

It can be used for:

Copying files
Moving files
Removing directories
Creating backups
File organization

This connects directly to my File Organizer project.

File Handling

Python can read from and write to files.

Reading a File
file = open("example.txt", "r")

content = file.read()

print(content)

file.close()

A better approach is using with:

with open("example.txt", "r") as file:
    content = file.read()

print(content)

The file is automatically closed after the block finishes.

Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello Python!")
Appending to a File
with open("example.txt", "a") as file:
    file.write("\nNew line")

Common file modes:

Mode	Purpose
r	Read
w	Write
a	Append
x	Create a new file
Python + Log Analysis

File handling becomes especially useful in cybersecurity.

Security systems generate logs containing information about:

Login attempts
Errors
Network activity
Authentication events
System activity

Python can read these files and search for suspicious patterns.

Example:

with open("log.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print(line)

This is a simple example of automated log analysis.

Error Handling

Programs can encounter errors while running.

Python allows us to handle expected errors using try and except.

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")

This prevents the program from crashing when the user enters invalid input.

Why Error Handling Matters

In real applications, unexpected input and failures are common.

Error handling helps make programs:

More reliable
More user-friendly
Easier to debug
Safer to run
Functions + Modules + File Handling

These concepts can be combined to create more useful programs.

Example:

import os

def show_files():
    files = os.listdir()

    for file in files:
        print(file)

show_files()

This combines:

Functions
Modules
Loops
Operating system interaction
Cybersecurity Connection

Python becomes much more powerful when these concepts are combined.

Example Workflow
Python Basics
      ↓
Functions
      ↓
Modules
      ↓
File Handling
      ↓
Automation
      ↓
Log Analysis
      ↓
Security Tools

Python can eventually be used for:

Log analysis
File monitoring
Network programming
Automation
Data processing
API interaction
Security scripting
Vulnerability assessment tools
Incident-response utilities
Practice Programs

I practiced the following concepts:

1. Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(10, 5))
print(subtract(10, 5))
2. Password Generator Using Modules

Use:

random
string
Functions
Loops
3. File Counter

Create a program that counts the number of files in a directory.

4. Log Analyzer

Read a text file and count how many lines contain:

failed
error
warning
5. Backup Script

Create a simple Python script that copies a file to a backup location using shutil.

Concepts I Can Now Use
Functions
Parameters
Arguments
return
Modules
import
Built-in Python modules
random
string
os
shutil
File reading
File writing
File appending
try / except
Basic automation
Basic log analysis
Connection to My Projects
Project	Concepts Used
Password Generator	Functions, random, string, loops
File Organizer	os, shutil, conditions
Text Analyzer	Strings, loops, functions
Contact Book	Functions, dictionaries, file handling
Quiz Game	Functions, conditions, loops
Password Strength Checker	Functions, strings, conditions
My Python Progression
Basic Syntax
      ↓
Variables & Data Types
      ↓
Input & Output
      ↓
Operators
      ↓
Conditions
      ↓
Loops
      ↓
Strings
      ↓
Lists & Dictionaries
      ↓
Functions
      ↓
Modules & Libraries
      ↓
File Handling
      ↓
Automation
      ↓
Cybersecurity Applications
What I'm Building Toward

The goal is not just to learn Python syntax.

I want to use Python as a practical tool for cybersecurity.

My next step is to move from basic Python programs toward:

More advanced Python
Object-Oriented Programming
Exception handling
Regular expressions
Working with JSON
APIs
Networking with Python
Automation
Security-focused scripting

These concepts will form the foundation for my future cybersecurity projects.


### Next after this

Your **next Python section** should be **Object-Oriented Programming (OOP)** — classes, objects, constructors, methods, inheritance, etc.

That’s a good point where your **Intermediate Python** phase starts on **September 7**. 🚀
