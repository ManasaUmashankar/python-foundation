# File Handling
# Appending to a file


with open("output.txt", "a") as file:
    file.write("Security scan completed.\n")

print("Data appended successfully.")
