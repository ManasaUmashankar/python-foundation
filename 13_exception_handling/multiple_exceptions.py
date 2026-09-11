# Handling multiple exceptions


try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
