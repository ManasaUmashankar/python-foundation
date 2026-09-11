# Secure Input Validator


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
