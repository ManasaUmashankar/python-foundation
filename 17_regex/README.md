Python Intermediate: Regular Expressions
Objective

Learn how to use Regular Expressions (Regex) in Python to search, match, extract, and analyze text patterns.

By the end of this topic, you will be able to:

Understand regex syntax
Use the Python re module
Search for patterns in text
Match patterns
Extract multiple matches
Use character classes
Use quantifiers
Work with regex groups
Apply regex to cybersecurity-related text
Topics Covered
Regex Basics
re.search()
re.match()
re.findall()
re.finditer()
Character Classes
Quantifiers
Regex Groups
Practical Regex Pattern Searching
1. Regex Basics
Definition

A Regular Expression (Regex) is a pattern used to search, match, and extract specific text from a string.

Python provides the built-in re module for working with regular expressions.

Explanation

Regex allows us to describe patterns instead of searching for exact text.

For example:

\d → digit
\w → word character
\s → whitespace
. → any character
Syntax
import re

pattern = r"\d+"
Code Example
import re

text = "User123 logged in."

result = re.findall(r"\d+", text)

print(result)
Expected Output
['123']
Cybersecurity Connection

Regex is widely used in cybersecurity for identifying patterns in:

Logs
IP addresses
Usernames
URLs
Email addresses
Error messages
2. re.search()
Definition

re.search() searches the entire string for the first occurrence of a pattern.

Explanation

If a match is found, it returns a match object. Otherwise, it returns None.

Syntax
re.search(pattern, string)
Code Example
import re

text = "Login failed for user admin."

result = re.search(r"failed", text)

if result:
    print("Pattern found.")
else:
    print("Pattern not found.")
Expected Output
Pattern found.
Cybersecurity Connection

A security log analyzer can use re.search() to detect keywords such as:

failed
denied
error
unauthorized
3. re.match()
Definition

re.match() checks whether a pattern matches from the beginning of a string.

Explanation

Unlike re.search(), it does not search throughout the entire string.

Syntax
re.match(pattern, string)
Code Example
import re

text = "ERROR: Login failed."

result = re.match(r"ERROR", text)

if result:
    print("Pattern matched at the beginning.")
else:
    print("No match.")
Expected Output
Pattern matched at the beginning.
Cybersecurity Connection

re.match() can be useful when log entries follow a fixed format and important information appears at the beginning of each line.

4. re.findall()
Definition

re.findall() returns all non-overlapping matches of a pattern.

Explanation

Instead of stopping at the first match, findall() collects every matching value.

Syntax
re.findall(pattern, string)
Code Example
import re

text = "User123 connected from IP 192.168.1.10."

numbers = re.findall(r"\d+", text)

print(numbers)
Expected Output
['123', '192', '168', '1', '10']
Cybersecurity Connection

findall() is useful for extracting multiple pieces of information from logs, such as numbers, usernames, or IP-address components.

5. re.finditer()
Definition

re.finditer() returns an iterator containing match objects for every match.

Explanation

Unlike findall(), finditer() provides detailed match information, including positions.

Syntax
re.finditer(pattern, string)
Code Example
import re

text = "Login failed. Login successful."

matches = re.finditer(r"Login", text)

for match in matches:
    print(match.group(), match.start())
Expected Output
Login 0
Login 15
Cybersecurity Connection

Match positions can be useful when analyzing large text files or security logs where the exact location of a suspicious pattern matters.

6. Character Classes
Definition

Character classes allow regex to match specific types or sets of characters.

Common Character Classes
Pattern	Meaning
\d	Digit
\D	Non-digit
\w	Word character
\W	Non-word character
\s	Whitespace
\S	Non-whitespace
[abc]	a, b, or c
[A-Z]	Uppercase letters
[0-9]	Digits
Code Example
import re

text = "User123"

result = re.findall(r"[A-Z]", text)

print(result)
Expected Output
['U']
Cybersecurity Connection

Character classes can help identify specific patterns in:

Usernames
Password rules
IDs
Log entries
Network data
7. Quantifiers
Definition

Quantifiers specify how many times a pattern should occur.

Common Quantifiers
Quantifier	Meaning
+	One or more
*	Zero or more
?	Zero or one
{n}	Exactly n
{n,m}	Between n and m
Code Example
import re

text = "User12345"

result = re.findall(r"\d{3}", text)

print(result)
Expected Output
['123']
Cybersecurity Connection

Quantifiers are useful when detecting structured patterns such as:

IDs
Port numbers
Numeric codes
Log timestamps
IP address components
8. Regex Groups
Definition

Groups allow us to capture specific parts of a matched pattern.

Parentheses () are used to create a capturing group.

Syntax
(pattern)
Code Example
import re

text = "User: admin"

result = re.search(r"User:\s(\w+)", text)

if result:
    print(result.group(1))
Expected Output
admin
Cybersecurity Connection

Groups are useful for extracting specific information from structured security data.

For example, a log parser could separately capture:

Username
IP address
Event type
Timestamp
9. Practical Regex Pattern Searching
Definition

Practical regex searching combines different regex concepts to extract useful information from real-world text.

Code Example
import re

log = "Failed login for admin from 192.168.1.25"

username = re.search(r"for (\w+)", log)
ip_address = re.search(r"\d+\.\d+\.\d+\.\d+", log)

if username:
    print("Username:", username.group(1))

if ip_address:
    print("IP Address:", ip_address.group())
Expected Output
Username: admin
IP Address: 192.168.1.25
Cybersecurity Connection

This is the foundation of security log parsing.

A SOC analyst or security automation script can use regex to extract useful indicators from large amounts of log data.

Mini Project
Regex Log Pattern Analyzer

Build a small Python program that analyzes a security log and extracts:

Usernames
IP addresses
Failed-login messages
Numeric values
Other suspicious patterns

This project will prepare you for more advanced security log analysis.

Security Considerations

When using regex for security analysis:

Validate extracted data.
Don't assume every match is malicious.
Regex patterns should be tested carefully.
Complex regex can become difficult to maintain.
Avoid processing untrusted input without proper validation.
Use structured log formats when available.
