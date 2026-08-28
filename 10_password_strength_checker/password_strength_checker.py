# Password Strength Checker
# Python Foundation - Project 10

import string


def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score == 3 or score == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


print("🔐 PASSWORD STRENGTH CHECKER")
print("----------------------------")

password = input("Enter your password: ")

strength = check_password(password)

print("Password strength:", strength)
