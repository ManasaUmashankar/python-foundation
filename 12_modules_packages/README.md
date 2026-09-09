
# Modules & Packages 🐍

## 📌 Overview

Day 2 focuses on **Modules and Packages in Python**.

Modules and packages help organize Python code into separate, reusable components instead of keeping everything inside one large file.

These concepts are especially useful when building larger projects and cybersecurity tools.

---

## 🎯 Learning Objectives

By the end of Day 2, I will understand:

- What Python modules are
- How to import modules
- How to import specific functions
- How to use aliases
- How to create custom modules
- What Python packages are
- How to organize code using packages
- How `__name__ == "__main__"` works
- How modules and packages improve project structure

---

## 📚 Topics Covered

### 1. What is a Module?

A module is a Python file containing reusable code such as:

- Functions
- Variables
- Classes
- Statements

Example:

```python
# math_utils.py

def add(a, b):
    return a + b

The module can then be imported into another Python file.

2. Importing a Module
import math_utils

result = math_utils.add(10, 5)

print(result)

Output:

15

The import statement allows us to reuse code from another Python file.

3. Importing Specific Functions

Instead of importing the entire module:

from math_utils import add

print(add(10, 5))

This imports only the add() function.

4. Importing Multiple Functions
from math_utils import add, subtract

print(add(10, 5))
print(subtract(10, 5))
5. Using Aliases

An alias gives a module a shorter or more convenient name.

import math_utils as mu

print(mu.add(10, 5))

Here:

math_utils → mu
6. Creating Custom Modules

Python allows us to create our own modules.

Example project structure:

11_modules_packages/
│
├── math_utils.py
└── main.py

math_utils.py:

def add(a, b):
    return a + b

main.py:

import math_utils

print(math_utils.add(10, 5))
7. What is a Package?

A package is a directory used to organize multiple Python modules.

Example:

security_tools/
│
├── __init__.py
├── password.py
├── hashing.py
└── logs.py

Each .py file can contain related functionality.

Packages make larger projects easier to maintain.

8. __name__ == "__main__"

Python provides the special variable:

__name__

When a Python file is executed directly, its value is:

__main__

Example:

def greet():
    print("Hello!")


if __name__ == "__main__":
    greet()

This allows us to control which code runs when a file is executed directly versus imported as a module.

🛡️ Cybersecurity Connection

Modules and packages are important for cybersecurity projects because security tools usually contain multiple components.

For example:

cybersecurity_toolkit/
│
├── main.py
│
├── password_utils.py
├── hash_utils.py
├── log_utils.py
├── ip_utils.py
└── file_utils.py

Each module can perform a specific security-related task.

This makes the project:

Easier to understand
Easier to test
Easier to maintain
Easier to reuse
Easier to expand#
