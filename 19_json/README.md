# Python Intermediate: JSON

## Objective

Learn how to work with **JSON (JavaScript Object Notation)** in Python and use it to store, read, modify, and exchange structured data.

By the end of this topic, you will be able to:

* Understand JSON structure
* Read JSON files
* Write data to JSON files
* Convert JSON strings into Python objects
* Convert Python objects into JSON strings
* Update JSON data
* Use JSON for cybersecurity-related data

---

## Topics Covered

1. JSON Basics
2. Reading JSON Files — `json.load()`
3. Writing JSON Files — `json.dump()`
4. JSON Strings to Python — `json.loads()`
5. Python Objects to JSON Strings — `json.dumps()`
6. Updating JSON Data
7. Security Log Data with JSON
8. JSON Security Considerations

---

# 1. JSON Basics

## Definition

**JSON (JavaScript Object Notation)** is a lightweight text-based format used to store and exchange structured data.

JSON commonly uses:

* Objects
* Arrays
* Strings
* Numbers
* Booleans
* `null`

## Explanation

A JSON object stores data using **key-value pairs**.

Example:

```text
{
    "username": "admin",
    "status": "failed"
}
```

JSON is widely used by APIs, applications, configuration files, and security tools.

## Syntax

```python
import json
```

## Code Example

```python
import json

data = {
    "username": "admin",
    "status": "failed"
}

print(json.dumps(data, indent=4))
```

## Expected Output

```text
{
    "username": "admin",
    "status": "failed"
}
```

## Cybersecurity Connection

JSON is commonly used to represent:

* Security events
* API responses
* Configuration data
* Threat-intelligence information
* SIEM data

---

# 2. Reading JSON Files — `json.load()`

## Definition

`json.load()` reads JSON data directly from a file and converts it into a Python object.

## Syntax

```python
json.load(file)
```

## Code Example

```python
import json

with open("security_log.json", "r") as file:
    data = json.load(file)

print(data)
```

## Expected Output

```text
{'username': 'admin', 'status': 'failed'}
```

## Cybersecurity Connection

Security applications can store logs in JSON files and Python can read them for automated analysis.

---

# 3. Writing JSON Files — `json.dump()`

## Definition

`json.dump()` writes a Python object directly into a JSON file.

## Syntax

```python
json.dump(data, file, indent=4)
```

## Code Example

```python
import json

data = {
    "username": "admin",
    "status": "failed"
}

with open("security_log.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully.")
```

## Expected Output

```text
JSON file created successfully.
```

## Cybersecurity Connection

Security scripts can automatically save:

* Detection results
* Security alerts
* Scan reports
* Incident information

as JSON files.

---

# 4. JSON Strings to Python — `json.loads()`

## Definition

`json.loads()` converts a JSON-formatted **string** into a Python object.

The `s` stands for **string**.

## Syntax

```python
json.loads(json_string)
```

## Code Example

```python
import json

json_data = '{"username": "admin", "status": "failed"}'

data = json.loads(json_data)

print(data)
print(data["username"])
```

## Expected Output

```text
{'username': 'admin', 'status': 'failed'}
admin
```

## Cybersecurity Connection

APIs often return JSON data as text. `json.loads()` allows Python security tools to convert that response into usable Python data.

---

# 5. Python Objects to JSON Strings — `json.dumps()`

## Definition

`json.dumps()` converts a Python object into a JSON-formatted string.

The `s` stands for **string**.

## Syntax

```python
json.dumps(data)
```

## Code Example

```python
import json

data = {
    "ip": "192.168.1.25",
    "status": "suspicious"
}

json_string = json.dumps(data, indent=4)

print(json_string)
```

## Expected Output

```text
{
    "ip": "192.168.1.25",
    "status": "suspicious"
}
```

## Cybersecurity Connection

JSON strings are useful when sending structured security information to:

* APIs
* Security platforms
* Monitoring systems
* Web applications

---

# 6. Updating JSON Data

## Definition

JSON data can be loaded into Python, modified, and then written back to a JSON file.

## Explanation

The general process is:

**JSON file → Python object → Modify → JSON file**

## Code Example

```python
import json

with open("security_log.json", "r") as file:
    data = json.load(file)

data["status"] = "investigated"

with open("security_log.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON data updated.")
```

## Expected Output

```text
JSON data updated.
```

## Cybersecurity Connection

Security automation tools can update records as an investigation progresses.

For example:

`failed` → `investigating` → `resolved`

---

# 7. Security Log Data with JSON

## Definition

JSON can represent structured security events in a format that is easy for programs to process.

## Example

```python
security_event = {
    "timestamp": "2026-09-22 10:30",
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event": "failed_login",
    "severity": "medium"
}
```

## Code Example

```python
import json

security_event = {
    "timestamp": "2026-09-22 10:30",
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event": "failed_login",
    "severity": "medium"
}

print(json.dumps(security_event, indent=4))
```

## Expected Output

```text
{
    "timestamp": "2026-09-22 10:30",
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event": "failed_login",
    "severity": "medium"
}
```

## Cybersecurity Connection

Structured JSON security events can be processed by monitoring and security-analysis systems.

This is particularly relevant to **SOC and SIEM workflows**.

---

# 8. JSON Security Considerations

## Definition

JSON itself is a data format, but applications processing JSON still need appropriate security controls.

## Important Considerations

* Validate data before processing it.
* Do not store passwords or secrets in plain-text JSON.
* Avoid exposing sensitive information.
* Handle malformed JSON safely.
* Be careful when processing JSON received from untrusted sources.
* Use appropriate access permissions for sensitive JSON files.

---

# Mini Project

## Security Log JSON Manager

Build a small Python program that stores security events in JSON format.

### Features

The project will:

* Create security-event data
* Save events to JSON
* Read JSON data
* Display security events
* Update event information

### Example Event

```text
{
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event": "failed_login",
    "severity": "medium"
}
```

### Cybersecurity Connection

This project demonstrates how Python can manage structured security information and prepares you for working with **APIs, SIEM-style data, and security automation**.

---

