## Security Utility Toolkit

from security_tools.password_utils import check_password_strength
from security_tools.hash_utils import generate_sha256


def display_security_report(checks):
    print("\nPassword Security Check")
    print("-----------------------")

    for check, result in checks.items():
        print(check + ":", result)


def main():
    password = input("Enter a password to check: ")

    checks = check_password_strength(password)

    display_security_report(checks)

    print("\nSHA-256 Hash")
    print("------------")

    password_hash = generate_sha256(password)

    print(password_hash)


if __name__ == "__main__":
    main()
