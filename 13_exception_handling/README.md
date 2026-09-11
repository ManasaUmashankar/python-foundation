## Exception Handling 🐍

Objective

Learn how to detect, handle, and control errors in Python programs without allowing unexpected situations to crash the entire application.
Exception handling is especially important in cybersecurity because security tools often process unpredictable user input, files, logs, network data, and system information.

1. Exceptions
Definition:
An exception is an event that occurs during program execution when Python encounters a situation it cannot normally continue with.

Common examples include:
ValueError
TypeError
ZeroDivisionError
FileNotFoundError
PermissionError
Explanation

For example, converting invalid text into an integer causes a ValueError.


## Cybersecurity Connection
Security programs frequently receive unexpected or invalid data. Understanding exceptions allows a program to handle these situations safely instead of crashing.

Code Example
```
number = int("hello")
```
Expected result:
ValueError

2. try and except
Definition
try contains code that might produce an exception.
except contains the code used to handle that exception.

##Explanation
Python executes the code inside try. If the specified exception occurs, Python skips the remaining try code and executes the matching except block.

## Cybersecurity Connection
This is useful when a security tool accepts user input such as ports, IP addresses, usernames, or configuration values.

Code Example
try:
```
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input. Please enter a number.")
```
Expected Output
Enter a number: hello
Invalid input. Please enter a number
.
3. Multiple Exceptions
Definition
A program can encounter different types of exceptions. Python allows different except blocks to handle each type separately.

Explanation
Each except block can respond to a specific type of error.

## Cybersecurity Connection
Different failures often require different responses in security tools. Separating exceptions makes the program easier to debug and maintain.

Code Example
try:
```
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
```
Expected Output

For zero:

Enter a number: 0
You cannot divide by zero.


4. else
Definition
The else block runs only when the try block completes successfully without raising an exception.

Explanation
It is useful for separating successful processing from error-handling logic.

## Cybersecurity Connection

The else block can contain processing logic that should happen only after input or security data has been successfully validated.

Code Example
try:
   ```
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input. Please enter a number.")

else:
    print("Valid input.")
    print("You entered:", number)
```

Expected Output
Enter a number: 25
Valid input.
You entered: 25

5. finally
Definition
The finally block always executes, whether an exception occurs or not.

Explanation
It is commonly used for cleanup operations that must happen regardless of whether an operation succeeds or fails.

## Cybersecurity Connection

Security tools may need to close files, release resources, or reset temporary state after an operation.

Code Example
try:
```
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input. Please enter a number.")

finally:
    print("Program execution completed.")
```
Expected Output
Enter a number: hello
Invalid input. Please enter a number.
Program execution completed.

6. raise
Definition
raise is used to manually trigger an exception.

Explanation
It allows the programmer to enforce custom validation rules instead of relying only on errors generated automatically by Python.

## Cybersecurity Connection
raise can enforce security rules such as invalid IP addresses, invalid ports, insufficient password length, or unauthorized actions.

Code Example
```
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    return "Access granted"


try:
    age = int(input("Enter your age: "))
    result = check_age(age)

except ValueError as error:
    print("Error:", error)

else:
    print(result)
```
Expected Output
Enter your age: 16
Error: Age must be 18 or above.

7. Combining try, except, else, finally, and raise
Definition
Python allows all five concepts to work together to create controlled error handling and validation.

Explanation
The general flow is:
```
try
 ↓
Attempt operation
 ↓
Exception?
 ├── Yes → except
 └── No  → else
 ↓
finally
```
## Cybersecurity Connection
Security applications often need to validate data, handle failures, continue safely after expected errors, and perform cleanup operations.

Code Example
try:
```
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Number cannot be negative.")

except ValueError as error:
    print("Error:", error)

else:
    print("Valid number:", number)

finally:
    print("Validation completed.")
```
Expected Output
Enter a number: -5
Error: Number cannot be negative.
Validation completed.

8. Input Validation
Definition
Input validation is the process of checking whether data provided to a program meets expected rules before processing it.

Explanation
User input should not automatically be trusted. A program should verify that input is present, correctly formatted, and appropriate for the intended operation.

## Cybersecurity Connection
Input validation is a fundamental security practice. Applications should validate data before processing it to reduce unexpected behavior and security risks.

Code Example
```
def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty.")

    if len(username) < 3:
        raise ValueError("Username must contain at least 3 characters.")

    if " " in username:
        raise ValueError("Username cannot contain spaces.")

    return True


try:
    username = input("Enter username: ")

    validate_username(username)

except ValueError as error:
    print("Invalid username:", error)

else:
    print("Username is valid.")

finally:
    print("Username validation completed.")
```
Expected Output
Enter username: admin01
Username is valid.
Username validation completed.

9. File Error Handling
Definition
File operations can generate exceptions when a file is missing or inaccessible.

Important exceptions include:
FileNotFoundError
PermissionError
Explanation

Exception handling allows a program to respond appropriately instead of terminating unexpectedly when a file operation fails.

## Cybersecurity Connection
Cybersecurity tools frequently process system logs, authentication logs, configuration files, and security reports. Handling file errors prevents the entire tool from crashing when a file is missing or inaccessible.

Code Example
```
file_path = input("Enter the file path: ")

try:
    with open(file_path, "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

else:
    print("File read successfully.")
    print(content)

finally:
    print("File operation completed.")
```

Expected Output
Enter the file path: missing.txt
Error: File not found.
File operation completed.

10. Custom Exceptions
Definition
A custom exception is an exception class created by the programmer for a specific application.
Custom exceptions normally inherit from Python's Exception class.

Explanation
Custom exceptions make application-specific errors easier to identify and handle.

## Cybersecurity Connection
Security applications can use custom exceptions to clearly distinguish between different security-related failures.

Examples include:
WeakPasswordError
InvalidIPError
InvalidLogError
UnauthorizedAccessError

Code Example
```
class WeakPasswordError(Exception):
    pass


def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    return "Password is acceptable."


try:
    password = input("Enter a password: ")

    result = check_password(password)

except WeakPasswordError as error:
    print("Security Error:", error)

else:
    print(result)
```

Expected Output
Enter a password: abc123
Security Error: Password must contain at least 8 characters.

11. Mini Project — Secure Input Validator
Definition
A secure input validator checks user-provided data against predefined rules and raises appropriate exceptions when the data is invalid.

Explanation
The project validates a username using a function and handles validation errors using exception handling.

Rules:

Username cannot be empty.
Username must contain at least 3 characters.
Username cannot contain spaces.
Cybersecurity Connection

Input validation is one of the foundations of secure application development. Data should be validated before it is processed or passed to other parts of an application.

Code Example
```
def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty.")

    if len(username) < 3:
        raise ValueError("Username must contain at least 3 characters.")

    if " " in username:
        raise ValueError("Username cannot contain spaces.")

    return True


try:
    username = input("Enter username: ")

    validate_username(username)

except ValueError as error:
    print("Invalid username:", error)

else:
    print("Username is valid.")

finally:
    print("Username validation completed.")
```
Expected Output

Valid input:
Enter username: admin01
Username is valid.
Username validation completed.

Invalid input:
Enter username: admin user
Invalid username: Username cannot contain spaces.
Username validation completed.
Key Concepts
