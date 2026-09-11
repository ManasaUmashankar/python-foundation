# Custom Exception


class WeakPasswordError(Exception):
    pass


def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must contain at least 8 characters.")

    return "Password is acceptable."


try:
    password = input("Enter a password: ")

    result = check_password(password)

except WeakPasswordError as error:
    print("Security Error:", error)

else:
    print(result)
