# File Handling
# Writing to a file


with open("output.txt", "w") as file:
    file.write("Security analysis started.\n")
    file.write("No threats detected.\n")

print("File written successfully.")
