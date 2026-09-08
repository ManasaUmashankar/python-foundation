 Python Intermediate: Functions

## 🎯 Objective

Strengthen Python functions and learn how to write flexible,
reusable functions for real-world and cybersecurity-related programs.

---

## 📚 Topics Covered

### 1. Parameters vs Arguments

**Parameter:** A variable defined inside a function.

**Argument:** The actual value passed to the function.

```python
def introduce(name, age, course):
    print(name, age, course)

introduce("Manasa", 19, "BCA")
2. Default Parameters

A default parameter has a value that is automatically used
when no argument is provided.

def calculate_discount(price, discount=10):
    return price - (price * discount / 100)

print(calculate_discount(1000))
print(calculate_discount(1000, 20))
3. Keyword Arguments

Keyword arguments pass values using parameter names.

def account(username, email, role):
    print(username, email, role)

account(
    email="example@gmail.com",
    role="SOC analyst",
    username="mns123"
)

The order does not matter when using keyword arguments.

4. *args

*args allows a function to accept multiple positional arguments.

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(10, 20, 30, 40))

args is stored as a tuple.

5. **kwargs

**kwargs allows a function to accept multiple keyword arguments.

def user_profile(**kwargs):
    print(kwargs)

user_profile(
    name="mns",
    role="SOC analyst",
    age=22,
    location="Germany"
)

kwargs is stored as a dictionary.

6. Scope & LEGB

Python searches for variables using the LEGB rule:

L — Local
E — Enclosing
G — Global
B — Built-in

Understanding scope helps prevent unexpected variable behaviour.

7. Multiple Return Values

A function can return multiple values.

def security_info():
    username = "mns123"
    role = "SOC analyst"
    return username, role

name, role = security_info()

print(name)
print(role)
8. Functions as Objects

Functions can be stored in variables and passed to other functions.

def greet():
    return "Hello"

message = greet

print(message())
9. Lambda Functions

Lambda functions are small anonymous functions.

square = lambda x: x * x

print(square(5))
🔐 Cybersecurity Connection

Functions are essential when building cybersecurity tools.

They can be used to create reusable components for:

Log analysis
IP address validation
Password checking
File scanning
Port scanning
Hash generation
Security automation
Alert processing

Example:

def check_status(status="unknown"):
    return f"System status: {status}"

print(check_status("secure"))
🧪 Practice Tasks
Task 1 — Default Parameter
Create:
def calculate_discount(price, discount=10):
Test it:With a discount
        Without a discount

Task 2 — *args
Create a function that accepts multiple numbers
and returns their total.

Task 3 — **kwargs
Create a function that accepts:
username
role
IP address
status
Print all collected information.

Task 4 — Mini Challenge
Create a reusable function:
def security_profile(...):
It should display a user's basic security profile.
