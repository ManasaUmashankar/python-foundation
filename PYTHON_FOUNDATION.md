# Python Foundation

A structured revision and documentation of the Python fundamentals learned through my beginner projects.

- What is Python?
- Variables
- Data Types
- Input and Output
- Type Conversion
- Operators
- Conditional Statements
- Application of fundamentals in beginner projects

---

## 1. What is Python?

Python is a high-level, interpreted, general-purpose programming language known for its simple and readable syntax.

Python is widely used in:

- Web Development
- Automation
- Data Analysis
- Artificial Intelligence
- Machine Learning
- Software Development
- Cybersecurity
- Scripting

### Why Python is useful in Cybersecurity

Python is particularly useful in cybersecurity because it makes it easy to automate tasks and process information.

It can be used for:

- Log analysis
- File processing
- Network programming
- Automation
- API interaction
- Data processing
- Security scripting
- Building security tools

---

# 2. Variables

A variable is a name used to store a value in a program.

### Example

```python
name = "Manasa"
age = 20

Here:

name stores a string
age stores an integer

Python does not require us to explicitly declare the variable type.

Example
username = "admin"
attempts = 5
is_logged_in = True

Variables can also be changed during program execution.

score = 10
score = 20

The value of score is now 20.

3. Data Types

A data type defines the kind of value stored in a variable.

Common Python Data Types
Data Type	Example	Description
str	"Hello"	Text
int	10	Whole numbers
float	10.5	Decimal numbers
bool	True	Boolean value
list	[1, 2, 3]	Collection of values
dict	{"name": "John"}	Key-value pairs
Checking the data type

Python provides the type() function.

age = 20

print(type(age))

Output:

<class 'int'>

Understanding data types is important because different types support different operations.

4. Input and Output
Output

The print() function is used to display information.

print("Hello World")

We can also print variables.

name = "Manasa"

print(name)

Multiple values can be printed together.

name = "Manasa"
age = 20

print(name, age)
Input

The input() function allows a program to receive information from the user.

name = input("Enter your name: ")

print("Hello", name)
Important Concept

The value returned by input() is normally a string.

For example:

age = input("Enter your age: ")

If the user enters:

20

Python initially treats it as:

"20"

not:

20

Therefore, numerical input usually needs type conversion.

5. Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions
int()
float()
str()
bool()
String to Integer
age = int(input("Enter your age: "))
String to Float
price = float(input("Enter price: "))
Number to String
age = 20

text = str(age)
Example
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)

Type conversion is an important concept used in my Calculator project.

6. Operators

Operators are symbols or keywords used to perform operations on values.

Arithmetic Operators
Operator	Meaning	Example
+	Addition	10 + 5
-	Subtraction	10 - 5
*	Multiplication	10 * 5
/	Division	10 / 5
%	Modulus	10 % 3
**	Exponent	2 ** 3
//	Floor Division	10 // 3
Example
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
7. Comparison Operators

Comparison operators are used to compare two values.

Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
Example
age = 20

print(age >= 18)

Output:

True

Comparison operators are heavily used when making decisions in a program.

8. Logical Operators

Logical operators are used to combine or modify conditions.

and

Returns True when both conditions are true.

age = 20
has_id = True

print(age >= 18 and has_id)
or

Returns True when at least one condition is true.

is_admin = False
is_owner = True

print(is_admin or is_owner)
not

Reverses a Boolean value.

logged_in = True

print(not logged_in)

Logical operators are especially useful when creating security-related conditions.

9. Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

if

The if statement executes code when a condition is true.

age = 20

if age >= 18:
    print("Adult")
if-else

The else block executes when the if condition is false.

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
if-elif-else

Multiple conditions can be checked using elif.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")

Conditional statements are one of the most important foundations of programming because they allow programs to make decisions.

10. Conditional Logic in Cybersecurity

Conditional statements can also be used to identify potentially suspicious activity.

Example
failed_attempts = 5

if failed_attempts >= 5:
    print("Possible suspicious activity")
else:
    print("Activity appears normal")

This is a simplified example, but the same type of logic can later be used in:

Log analysis
Intrusion detection
Authentication systems
Security monitoring
Alert generation
11. Connection to My Beginner Projects

The concepts learned today were already used in my first two Python projects.

Project 1 — Calculator

The Calculator combines several fundamental concepts:

User Input
    ↓
Type Conversion
    ↓
Variables
    ↓
Operators
    ↓
Conditional Statements
    ↓
Output

Example:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
Concepts used
Variables
input()
print()
Type conversion
Arithmetic operators
Comparison operators
if
elif
12. Project 2 — Number Guessing Game

The Number Guessing Game introduces decision-making through comparisons.

Basic logic:

User enters a guess
        ↓
Compare guess with secret number
        ↓
 ┌──────┼──────┐
 ↓      ↓      ↓
High   Low   Correct

Example:

guess = int(input("Enter your guess: "))

if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("Correct!")
Concepts used
Variables
User input
Type conversion
Comparison operators
Conditional statements
Boolean logic
Decision making
13. What I Learned Today

By completing Day 1, I strengthened my understanding of the basic building blocks of Python.

I can now explain:
What Python is
What variables are
Basic Python data types
How input() works
How print() works
Why type conversion is needed
Arithmetic operators
Comparison operators
Logical operators
Conditional statements
How these concepts are applied in real programs
14. Practice Programs

To reinforce today's concepts, I practiced writing small programs from scratch.

1. Greeting Program
name = input("Enter your name: ")

print("Hello", name)
2. Addition Program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
3. Temperature Conversion
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
4. Positive, Negative or Zero
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
5. Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
15. Day 1 Summary

Today's learning established the basic structure of a Python program:

Variables
    ↓
Data Types
    ↓
Input / Output
    ↓
Type Conversion
    ↓
Operators
    ↓
Conditions
    ↓
Decision Making

These fundamentals form the foundation for more advanced Python concepts such as:

Loops
    ↓
Strings
    ↓
Lists & Dictionaries
    ↓
Functions
    ↓
Modules
    ↓
File Handling
    ↓
Automation
    ↓
Cybersecurity Applications
