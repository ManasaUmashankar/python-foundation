# Python Foundation 2

A structured revision and documentation of the Python fundamentals learned through my beginner projects.

---

# Logic, Strings, Lists, Dictionaries & Loops

## Topics Covered

- Strings
- String indexing
- String slicing
- String methods
- Lists
- List indexing and slicing
- List methods
- Dictionaries
- Dictionary keys and values
- `for` loops
- `while` loops
- `break`
- `continue`
- Practical application in beginner projects

---

# 1. Strings

A **string** is a sequence of characters used to represent text.

Strings can be written using single or double quotation marks.

```python
name = "Manasa"
message = 'Hello World'

Both are valid.

print(name)
print(message)
2. String Indexing

Each character in a string has a position called an index.

Python uses zero-based indexing, meaning the first character is at index 0.

Example:

name = "Python"

The indexes are:

 P   y   t   h   o   n
 0   1   2   3   4   5

We can access individual characters:

print(name[0])

Output:

P
print(name[3])

Output:

h
3. Negative Indexing

Python also supports negative indexing.

 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1

Example:

name = "Python"

print(name[-1])

Output:

n

Negative indexing is useful when accessing characters from the end of a string.

4. String Slicing

Slicing allows us to extract a portion of a string.

Syntax:

string[start:end]

The end index is not included.

Example:

text = "Python"

print(text[0:3])

Output:

Pyt

Another example:

print(text[2:6])

Output:

thon
String Slicing with Steps

Syntax:

string[start:end:step]

Example:

text = "Python"

print(text[::2])

This selects every second character.

Reversing a String

A string can be reversed using slicing:

text = "Python"

print(text[::-1])

Output:

nohtyP

This technique is useful when working with palindrome-related logic.

5. Common String Methods

Python provides many built-in string methods.

upper()

Converts a string to uppercase.

text = "hello"

print(text.upper())

Output:

HELLO
lower()

Converts a string to lowercase.

text = "HELLO"

print(text.lower())

Output:

hello
strip()

Removes leading and trailing whitespace.

text = "   hello   "

print(text.strip())

Output:

hello
replace()

Replaces part of a string.

text = "I like Java"

text = text.replace("Java", "Python")

print(text)

Output:

I like Python
find()

Finds the position of a substring.

text = "Python Programming"

print(text.find("Programming"))
count()

Counts how many times a substring appears.

text = "banana"

print(text.count("a"))

Output:

3
startswith()

Checks whether a string starts with specific characters.

text = "Python"

print(text.startswith("Py"))

Output:

True
endswith()

Checks whether a string ends with specific characters.

text = "Python"

print(text.endswith("on"))

Output:

True
6. Useful String Functions
len()

Returns the number of characters.

text = "Python"

print(len(text))

Output:

6

This is useful for:

Password length checking
Text analysis
Input validation
Data processing
7. Lists

A list is a collection that can store multiple values.

Lists are created using square brackets:

numbers = [10, 20, 30, 40]

A list can contain different data types:

data = ["Manasa", 20, True, 10.5]
8. List Indexing

Lists use zero-based indexing.

fruits = ["apple", "banana", "orange"]

Indexes:

apple    → 0
banana   → 1
orange   → 2

Example:

print(fruits[0])

Output:

apple
9. List Slicing

Lists can also be sliced.

numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])

Output:

[2, 3, 4]
10. Modifying Lists

Lists are mutable, which means their contents can be changed.

Example:

fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)

Output:

['apple', 'mango', 'orange']
11. Common List Methods
append()

Adds an item to the end of a list.

fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
insert()

Adds an item at a specific position.

fruits = ["apple", "orange"]

fruits.insert(1, "banana")

print(fruits)
remove()

Removes a specific item.

fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)
pop()

Removes an item using its index.

fruits = ["apple", "banana", "orange"]

fruits.pop(1)

print(fruits)
sort()

Sorts a list.

numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)

Output:

[1, 2, 5, 8]
reverse()

Reverses the order of a list.

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
12. Dictionaries

A dictionary stores data in key-value pairs.

Dictionaries are created using curly brackets:

student = {
    "name": "Manasa",
    "age": 20,
    "course": "BCA"
}

Here:

name   → Manasa
age    → 20
course → BCA
13. Accessing Dictionary Values

Values can be accessed using their keys.

print(student["name"])

Output:

Manasa

Another example:

print(student["course"])

Output:

BCA
14. Adding and Updating Dictionary Values

A new key-value pair can be added:

student["city"] = "Bangalore"

An existing value can be updated:

student["age"] = 21
15. Removing Dictionary Values

The pop() method can remove an item.

student.pop("city")

The del keyword can also be used:

del student["age"]
16. Useful Dictionary Methods
keys()

Returns all keys.

print(student.keys())
values()

Returns all values.

print(student.values())
items()

Returns key-value pairs.

print(student.items())
17. Why Lists and Dictionaries Matter

Lists and dictionaries are extremely useful for storing and organizing data.

Lists

Useful when we have a collection of similar or ordered items.

Example:

ports = [22, 80, 443]
Dictionaries

Useful when information has meaningful labels.

Example:

user = {
    "username": "admin",
    "role": "administrator",
    "active": True
}

These structures will become very important when working with cybersecurity data.

18. Loops

A loop allows a block of code to execute repeatedly.

Python commonly uses:

for
while

Loops are useful when working with collections, processing data, and automating repetitive tasks.

19. for Loop

A for loop is used to iterate through a sequence.

Example:

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

Output:

apple
banana
orange

The loop processes each item one at a time.

20. for Loop with range()

The range() function generates a sequence of numbers.

for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5

The ending value is not included.

21. while Loop

A while loop continues executing while a condition is true.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

The variable must eventually change so that the condition becomes false.

Otherwise, the loop can continue indefinitely.

22. break

The break statement immediately stops a loop.

Example:

for number in range(1, 10):

    if number == 5:
        break

    print(number)

Output:

1
2
3
4
23. continue

The continue statement skips the current iteration and moves to the next one.

Example:

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

Output:

1
2
4
5
24. Nested Loops

A loop can be placed inside another loop.

Example:

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)

Nested loops are useful when working with structured or multi-dimensional data.

25. Looping Through Dictionaries

Dictionaries can be processed using loops.

student = {
    "name": "Manasa",
    "age": 20,
    "course": "BCA"
}

for key, value in student.items():
    print(key, ":", value)

Output:

name : Manasa
age : 20
course : BCA
26. Strings + Loops

Loops can also process individual characters in a string.

text = "Python"

for character in text:
    print(character)

Output:

P
y
t
h
o
n

This is useful for text processing and analysis.

27. Lists + Loops

A list can be processed item by item.

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

We can also perform calculations:

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)

Output:

100
28. Practical Example — Password Character Analysis

Strings, loops and conditions can work together to analyze a password.

Example:

password = "Python123"

letters = 0
digits = 0

for character in password:

    if character.isalpha():
        letters += 1

    elif character.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)

Output:

Letters: 6
Digits: 3

This demonstrates how basic Python concepts can be combined for security-related tasks.

29. Practical Example — Finding a Value

A loop can be used to search through a list.

ports = [21, 22, 80, 443]

for port in ports:

    if port == 443:
        print("HTTPS port found")

Output:

HTTPS port found

This type of logic becomes useful when working with networking and cybersecurity data.

30. Connection to My Beginner Projects

The concepts covered here connect directly to several of my beginner projects.

Password Generator

The Password Generator uses strings and collections of characters.

Concepts involved include:

Strings
Lists
Loops
Random selection
String operations
Palindrome Checker

The Palindrome Checker uses string manipulation.

For example:

text = "madam"

if text == text[::-1]:
    print("Palindrome")

The string is reversed using:

text[::-1]

and then compared with the original.

Prime Number Checker

The Prime Number Checker uses loops and conditional logic.

Example:

number = 7
is_prime = True

for i in range(2, number):

    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

This demonstrates:

Variables
Loops
Conditions
Comparison operators
Modulus operator
break
31. Python Data Structure Overview

The main structures learned so far can be visualized as:

Python Data
    |
    ├── String
    │     └── Text
    |
    ├── List
    │     └── Ordered Collection
    |
    └── Dictionary
          └── Key-Value Data

These structures allow Python programs to store and process information efficiently.

32. Cybersecurity Connection

Strings, lists, dictionaries and loops are heavily used in cybersecurity programming.

Strings

Useful for:

Log analysis
URL processing
File content analysis
Pattern detection
Password analysis
Lists

Useful for:

IP addresses
Port numbers
File names
Suspicious domains
Network data

Example:

suspicious_ports = [21, 23, 445, 3389]
Dictionaries

Useful for structured security information.

user = {
    "username": "admin",
    "role": "administrator",
    "failed_attempts": 3
}
Loops

Useful for processing large amounts of information automatically.

Data
 ↓
Loop
 ↓
Analyze each item
 ↓
Check conditions
 ↓
Generate result
33. Important Concepts to Remember
Strings
text[0]
text[-1]
text[1:4]
text[::-1]
Lists
items[0]
items.append()
items.remove()
items.pop()
Dictionaries
data["key"]
data.keys()
data.values()
data.items()
Loops
for item in collection:
    ...
while condition:
    ...
Loop Control
break
continue
🧠 What I Learned

I learned how Python can work with collections of information and process data repeatedly.

Key concepts:

Strings store text
Strings support indexing and slicing
String methods simplify text processing
Lists store ordered collections
Lists are mutable
Dictionaries store key-value pairs
for loops iterate through collections
while loops repeat code while a condition remains true
break stops a loop
continue skips an iteration
Loops can be combined with conditions to process data
🧪 Practice Programs

I practiced writing small programs using today's concepts.

1. Count Characters
text = input("Enter text: ")

print("Length:", len(text))
2. Reverse a String
text = input("Enter text: ")

print("Reversed:", text[::-1])
3. Find the Largest Number
numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest:", largest)
4. Count Even Numbers
numbers = [1, 2, 3, 4, 5, 6]

count = 0

for number in numbers:

    if number % 2 == 0:
        count += 1

print("Even numbers:", count)
5. Dictionary Information
user = {
    "username": "admin",
    "role": "user",
    "active": True
}

for key, value in user.items():
    print(key, ":", value)
📌 Foundation Progress
Core Python
    ↓
Variables & Data Types
    ↓
Input & Output
    ↓
Operators
    ↓
Conditions
    ↓
Strings
    ↓
Lists
    ↓
Dictionaries
    ↓
Loops

These concepts form the foundation required for functions, modules, file handling and automation.
