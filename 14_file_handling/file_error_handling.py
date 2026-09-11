# File Handling
# Handling file errors


try:
    with open("security_log.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: security_log.txt was not found.")
