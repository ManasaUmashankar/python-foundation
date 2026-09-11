# File Handling
# Reading a file using with open()

with open("sample.txt", "r") as file:
    content = file.read()

print(content)
