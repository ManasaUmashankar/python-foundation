# try, except, and else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input. Please enter a number.")

else:
    print("Valid input.")
    print("You entered:", number)
