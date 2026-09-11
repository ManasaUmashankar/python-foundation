# Day 4 - File Handling
# Reading file lines with line numbers


with open("sample.txt", "r") as file:
    lines = file.readlines()

for number, line in enumerate(lines, start=1):
    print(number, ":", line.strip())
