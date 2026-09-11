

from security_tools.password_utils import check_password_strength
from security_tools.hash_utils import generate_sha256


def main():
    password = input("Enter a password to check: ")

    print("\nPassword Security Check")
    print("-----------------------")

    checks = check_password_strength(password)

    for check, result in checks.items():
        print(check + ":", result)

    print("\nSHA-256 Hash")
    print("------------")

    password_hash = generate_sha256(password)

    print(password_hash)


if __name__ == "__main__":
    main()
