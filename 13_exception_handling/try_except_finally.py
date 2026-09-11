# try, except, and finally


try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input. Please enter a number.")

finally:
    print("Program execution completed.")
