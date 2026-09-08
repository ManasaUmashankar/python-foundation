# Functions as Objects

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(operation, a, b):
    return operation(a, b)


print("Addition:", calculate(add, 10, 5))
print("Subtraction:", calculate(subtract, 10, 5))

------

▶️ Expected Output
Addition: 15
Subtraction: 5

------
🛡️ Why this matters for cybersecurity

This idea becomes useful when building things like:
log-processing functions
validation utilities
filtering systems
security analysis tools
reusable automation functions
