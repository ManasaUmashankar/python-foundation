# Day 3 - Exception Handling
# Using raise


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
