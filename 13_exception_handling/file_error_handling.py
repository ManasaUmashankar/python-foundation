# Handling file errors


file_path = input("Enter the file path: ")

try:
    with open(file_path, "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

else:
    print("File read successfully.")
    print(content)

finally:
    print("File operation completed.")
