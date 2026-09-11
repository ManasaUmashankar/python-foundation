# File Handling
# Understanding file modes


# Read mode
with open("sample.txt", "r") as file:
    content = file.read()

print("Read mode:")
print(content)


# Append mode
with open("output.txt", "a") as file:
    file.write("New security event recorded.\n")

print("\nAppend mode:")
print("New data added to output.txt")
