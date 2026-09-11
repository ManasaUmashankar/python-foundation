# Complete try-except-else-finally example


try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Number cannot be negative.")

except ValueError as error:
    print("Error:", error)

else:
    print("Valid number:", number)

finally:
    print("Validation completed.")
