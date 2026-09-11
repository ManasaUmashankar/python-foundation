# Day 1 - Mini Cybersecurity Project
# Password Security Checker


def check_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_number(password):
    return any(char.isdigit() for char in password)


def has_special_character(password):
    special_characters = "!@#$%^&*"
    return any(char in special_characters for char in password)


def check_password(password):
    score = 0

    if check_length(password):
        score += 1

    if has_uppercase(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    return score


def security_level(score):
    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


# Get password from the user

password = input("Enter your password: ")

score = check_password(password)
level = security_level(score)

print("Score:", score, "/ 5")
print("Security Level:", level)
