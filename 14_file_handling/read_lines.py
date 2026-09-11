# File Handling
# Reading a file line by line


with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
