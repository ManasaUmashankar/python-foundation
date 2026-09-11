#  Password Utility Module


def check_password_length(password):
    """Check whether a password has at least 8 characters."""

    return len(password) >= 8


def check_password_strength(password):
    """Perform basic password security checks."""

    checks = {
        "8+ characters": len(password) >= 8,
        "Uppercase": any(char.isupper() for char in password),
        "Lowercase": any(char.islower() for char in password),
        "Number": any(char.isdigit() for char in password),
    }

    return checks
