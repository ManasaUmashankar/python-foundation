# 🐍 Python Intermediate: Advanced Functions

##  Objective

The objective of Day 1 is to strengthen Python function concepts and learn how to design **flexible, reusable, and well-structured functions** for real-world and cybersecurity-related programs.

---

# Topics Covered

1. Parameters vs Arguments
2. Default Parameters
3. Keyword Arguments
4. `*args`
5. `**kwargs`
6. Scope and LEGB
7. Multiple Return Values and Unpacking
8. Functions as Objects
9. Lambda Functions
10. Reusable Function Design
11. Mini Cybersecurity Project — Password Security Checker

---

# 1. Parameters vs Arguments

##  Definition

A **parameter** is a variable defined in a function definition.

An **argument** is the actual value passed to the function when it is called.

##  Explanation

Parameters act as placeholders for the data that a function needs.
When the function is called, actual values are supplied as arguments.

##  Syntax
```python
def function_name(parameter):
    # function body
    pass

function_name(argument)
🔹 Code Example
def introduce(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


introduce("Manasa", 19, "BCA")
```

# Expected Output
Name: Manasa
Age: 19
Course: BCA

Here:

name, age, course → Parameters

"Manasa", 19, "BCA" → Arguments

# Cybersecurity Connection

Parameters allow cybersecurity functions to work with different inputs instead of using hard-coded values.

For example:
def check_ip(ip):
    # validate IP address
    pass

The same function can be used for different IP addresses.

2. Default Parameters
Definition:- A default parameter is a parameter that already has a value assigned to it.
If the caller does not provide a value, Python uses the default value.

# Explanation
Default parameters make functions more flexible because the caller does not always need to provide every argument.

# Syntax
def function_name(parameter=default_value):
 ...

# Code Example
```

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price

print("Default discount:", calculate_discount(1000))
print("20% discount:", calculate_discount(1000, 20))
```

# Expected Output
Default discount: 900.0
20% discount: 800.0

In the first call, discount becomes 10 automatically.

# Cybersecurity Connection
Default parameters can be useful when a security function needs a standard setting.

Example:
def check_port(port, protocol="TCP"):
    print("Checking", protocol, "port:", port)

The function can use TCP by default while still allowing another protocol to be provided.


3. Keyword Arguments
# Definition:- A keyword argument passes a value to a function using the parameter name.

# Explanation
With positional arguments, the order matters.
With keyword arguments, the parameter name tells Python where each value belongs.

3 Syntax
function_name(parameter=value)
🔹 Code Example
```
def account(username, email, role):
    print("Username:", username)
    print("Email:", email)
    print("Role:", role)


account(
    email="example@gmail.com",
    role="SOC Analyst",
    username="mns123"
)
```
# Expected Output
Username: mns123
Email: example@gmail.com
Role: SOC Analyst

The order does not matter because the parameter names are specified.

# Cybersecurity Connection
Keyword arguments are useful when security functions have several configuration options.

#Example:

def scan_target(ip, port=443, protocol="TCP"):
    ...

A caller can clearly specify:

scan_target(
    ip="192.168.1.10",
    protocol="TCP"
)

4. *args
Definition :- *args allows a function to accept an arbitrary number of positional arguments.

# Explanation

Normally, a function expects a fixed number of arguments.

With *args, we can pass any number of positional values.

Inside the function, the values are stored as a tuple.

#Syntax
def function_name(*args):
    ...
# Code Example
def add_numbers(*numbers):
    return sum(numbers)


print(add_numbers(10, 20, 30))
print(add_numbers(5, 10, 15, 20))
# Expected Output
60
50

The values collected by *numbers are stored as a tuple.

Conceptually:

(10, 20, 30)
Cybersecurity Connection

*args can be useful when a security function needs to process a variable number of items.

For example, a function could receive multiple log entries, ports, or security events.
```
def analyze_events(*events):
    for event in events:
        print("Analyzing:", event)
```
5. **kwargs
 Definition :- **kwargs allows a function to accept an arbitrary number of keyword arguments.

Explanation
The values passed through **kwargs are stored as a dictionary.
Each keyword becomes a dictionary key.

# Syntax
def function_name(**kwargs):
    ...
# Code Example
```
def user_profile(**details):
    print(details)


user_profile(
    name="mns",
    role="SOC Analyst",
    age=22,
    location="Germany"
)
```
# Expected Output
{'name': 'mns', 'role': 'SOC Analyst', 'age': 22, 'location': 'Germany'}

The information is stored approximately like:

{
    "name": "mns",
    "role": "SOC Analyst",
    "age": 22,
    "location": "Germany"
}

# Cybersecurity Connection

**kwargs can be useful when handling flexible security information or configuration settings.

For example:

def security_event(**details):
    print(details)

It could accept information such as:

username
IP address
event type
status
timestamp

6. Scope and LEGB
 Definition :- Scope determines where a variable can be accessed within a Python program.
Python searches for variables using the LEGB rule.

# LEGB
L — Local
E — Enclosing
G — Global
B — Built-in
{Python searches in this order}

# Local Scope

## A variable created inside a function normally belongs to that function.
```
def show_name():
    name = "Manasa"
    print(name)


show_name()

 Global Scope :- A variable created outside a function has global scope.

name = "Manasa"


def show_name():
    print(name)


show_name()

# Code Example
name = "Global"


def test():
    name = "Local"
    print("Inside:", name)


test()

print("Outside:", name)
```
# Expected Output
Inside: Local
Outside: Global
The local variable does not replace the global variable.

##  **Cybersecurity Connection**
Understanding scope is important when writing security tools because large programs often contain many variables and functions.

Good scope management helps prevent:
Accidental variable modification
Unexpected behaviour
Conflicts between different parts of a program

7. Multiple Return Values and Unpacking
 Definition :-A Python function can return multiple values.these values can then be unpacked into separate variables.

Explanation
When multiple values are returned using commas, Python groups them together, typically as a tuple.

# Code Example
```
def security_info():
    username = "mns123"
    role = "SOC Analyst"

    return username, role


name, role = security_info()

print("Username:", name)
print("Role:", role)
```
## Expected Output
Username: mns123
Role: SOC Analyst

The returned values are unpacked:

("mns123", "SOC Analyst")
        ↓
 name             role


##  **Cybersecurity Connection**
Security functions often need to return multiple pieces of information.

## For example:
def analyze_ip(ip):
    return ip, "Private", True

The result could contain:

IP address
IP classification
Validation status

8. Functions as Objects
Definition

In Python, functions are first-class objects.

This means functions can be:

Stored in variables
Passed as arguments
Returned from other functions

## Code Example
```
def greet():
    return "Hello"


message = greet

print(message())
```
## Expected Output
Hello

Notice:
message = greet

does not call the function immediately.
It stores a reference to the function.

We use:
message()
to call it.

# Passing a Function as an Argument
def add(a, b):
    return a + b


def calculate(operation, a, b):
    return operation(a, b)


print(calculate(add, 10, 5))

# Expected Output
15

# Cybersecurity Connection

This concept is useful when building flexible security processing systems.
For example, a log analyzer could receive different processing functions:

def process_logs(operation, logs):
    return operation(logs)

Different functions could then perform different types of analysis.

9. Lambda Functions
 Definition :- A lambda function is a small anonymous function written in a single expression.

## Explanation

Lambda functions are useful for short operations where defining a full function with def may be unnecessary.

## Syntax
lambda arguments: expression
# Code Example
square = lambda x: x * x

print(square(5))
## Expected Output
25

The equivalent normal function is:
```
def square(x):
    return x * x
## Another Example
add = lambda a, b: a + b

print(add(10, 20))
```
Output:
30

## ** Cybersecurity Connection**

Lambda functions can be useful for short filtering, sorting, or transformation operations when processing security data.
For example:

events = [
    {"severity": 2},
    {"severity": 5},
    {"severity": 3}
]

events.sort(key=lambda event: event["severity"])

This can help when working with structured security events.

10. Reusable Function Design
# Definition:- Reusable function design means creating functions that can be used multiple times with different inputs.

## Principles

A good reusable function should generally:

Have one clear responsibility
Accept appropriate parameters
Avoid unnecessary hard-coded values
Return useful results
Be easy to understand
Be reusable in different parts of a program

## Example
```
def calculate_discount(price, discount):
    return price - (price * discount / 100)

The same function can be reused:

print(calculate_discount(1000, 20))
print(calculate_discount(500, 10))
print(calculate_discount(2000, 30))
```
##  Expected Output
800.0
450.0
1400.0

## Single Responsibility

A function should generally have one main job.

Instead of:

def security_tool():
    # check password
    # analyze logs
    # scan files
    # validate IP
    # generate hash

we can separate the responsibilities:
```
def check_password(password):
    ...


def analyze_logs(logs):
    ...


def validate_ip(ip):
    ...


def generate_hash(data):
    ...
```
This makes the program easier to understand, test, debug, and maintain.

 Cybersecurity Connection
real cybersecurity applications are often divided into many small reusable functions.
For example:

Security Tool
     │
     ├── Password Checker
     ├── IP Validator
     ├── Log Analyzer
     ├── File Scanner
     └── Hash Generator

Each component can be developed and tested separately.

## Mini Project — Password Security Checker
## Objective

Build a basic password security checker using the function concepts learned throughout Day 1.
The program evaluates a password using five basic requirements.

## Security Checks
The program checks whether the password contains:

At least 8 characters
An uppercase letter
A lowercase letter
A number
A special character

Each successful requirement adds 1 to the score.

## Scoring System
0–2 → Weak
3–4 → Medium
5   → Strong

## Project Code
```
def check_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_number(password):
    return any(char.isdigit() for char in password)


def has_special_character(password):
    special_characters = "!@#$%^&*"
    return any(char in special_characters for char in password)


def check_password(password):
    score = 0

    if check_length(password):
        score += 1

    if has_uppercase(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    return score


def security_level(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter your password: ")

score = check_password(password)
level = security_level(score)

print("Score:", score, "/ 5")
print("Security Level:", level)
```

## Example Output

For:
Enter your password: Hello@123

Output:
Score: 5 / 5
Security Level: Strong

For:
Enter your password: hello
Output:
Score: 1 / 5
Security Level: Weak

## Cybersecurity Connection
This project demonstrates how basic Python functions can be combined to create a security-related utility.
The project uses:
User Input
    ↓
Password
    ↓
Individual Security Checks
    ↓
Score
    ↓
Security Level
    ↓
Result

The important programming concept is not simply checking the password.

The project demonstrates how a larger problem can be divided into small, reusable functions, each with a specific responsibility.

Note: This is an educational password-strength checker. It is not a complete measure of real-world password security and does not test passwords against breached-password databases or password-cracking models.
