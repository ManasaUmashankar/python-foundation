Modules and Packages

from security_tools.password_utils import check_password_length
from security_tools.hash_utils import generate_sha256


def main():
    password = "Cyber123"

    # Password utility
    is_valid = check_password_length(password)

    print("Password has 8+ characters:", is_valid)

    # Hash utility
    password_hash = generate_sha256(password)

    print("SHA-256:", password_hash)


if __name__ == "__main__":
    main()
