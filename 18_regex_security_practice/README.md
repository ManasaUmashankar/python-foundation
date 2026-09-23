# Python Intermediate: Regex Security Practice

## Objective

Apply Regular Expressions to practical **cybersecurity-related text analysis**.

In this topic, you will use Python and the `re` module to extract and detect useful information from security-style data.

By the end, you will be able to:

* Extract IP addresses
* Extract email addresses
* Extract URLs
* Detect failed login attempts
* Identify suspicious patterns
* Analyze security logs using Regex
* Build a basic security log analyzer

---

## Topics Covered

1. IP Address Extraction
2. Email Extraction
3. URL Extraction
4. Failed Login Detection
5. Suspicious Pattern Detection
6. Security Log Analysis
7. Security Log Analyzer — Mini Project

---

# 1. IP Address Extraction

## Definition

IP address extraction means identifying IPv4-style addresses from a text string.

## Explanation

An IPv4 address contains four numerical sections separated by dots.

Example:

`192.168.1.25`

A basic Regex pattern can be used to locate IP addresses inside logs.

## Syntax

```python
r"\d+\.\d+\.\d+\.\d+"
```

## Code Example

```python
import re

text = "Connection received from 192.168.1.25"

ip = re.search(r"\d+\.\d+\.\d+\.\d+", text)

if ip:
    print("IP Address:", ip.group())
```

## Expected Output

```text
IP Address: 192.168.1.25
```

## Cybersecurity Connection

IP addresses are commonly found in:

* Firewall logs
* Authentication logs
* Web-server logs
* Network monitoring data

They can be extracted for further investigation.

> Note: This basic Regex identifies IPv4-like patterns; it does not validate every possible IPv4 value.

---

# 2. Email Extraction

## Definition

Email extraction means finding email-address-like patterns inside text.

## Explanation

A basic email pattern can identify a username, `@` symbol, domain, and extension.

## Syntax

```python
r"[\w.-]+@[\w.-]+\.\w+"
```

## Code Example

```python
import re

text = "Contact security@example.com for more information."

email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)

if email:
    print("Email:", email.group())
```

## Expected Output

```text
Email: security@example.com
```

## Cybersecurity Connection

Email extraction can be useful when analyzing:

* Security reports
* Phishing-related text
* Incident reports
* Log files
* Security notifications

---

# 3. URL Extraction

## Definition

URL extraction means identifying web addresses inside text.

## Explanation

Regex can locate URLs that begin with protocols such as `http://` or `https://`.

## Syntax

```python
r"https?://\S+"
```

## Code Example

```python
import re

text = "Visit https://example.com/security for more information."

url = re.search(r"https?://\S+", text)

if url:
    print("URL:", url.group())
```

## Expected Output

```text
URL: https://example.com/security
```

## Cybersecurity Connection

URL extraction is useful in:

* Phishing analysis
* Threat intelligence
* Web-log analysis
* Incident response

Extracted URLs can later be analyzed using other security tools.

---

# 4. Failed Login Detection

## Definition

Failed login detection means identifying authentication attempts that contain indicators of unsuccessful login activity.

## Explanation

Security logs often contain phrases such as:

`Failed login`

Regex can search for these patterns automatically.

## Syntax

```python
r"Failed login"
```

## Code Example

```python
import re

log = "2026-09-21 Failed login for admin"

result = re.search(r"Failed login", log)

if result:
    print("Failed login detected.")
```

## Expected Output

```text
Failed login detected.
```

## Cybersecurity Connection

Repeated failed login attempts can be important indicators during authentication monitoring.

A real security monitoring system can combine failed-login detection with:

* Username
* IP address
* Timestamp
* Number of attempts

---

# 5. Suspicious Pattern Detection

## Definition

Suspicious pattern detection involves searching text for predefined patterns that may require further investigation.

## Explanation

For example, a security script can look for words such as:

* `failed`
* `denied`
* `unauthorized`
* `blocked`

## Code Example

```python
import re

log = "Access denied for user admin"

patterns = r"failed|denied|unauthorized|blocked"

result = re.search(patterns, log, re.IGNORECASE)

if result:
    print("Suspicious event:", result.group())
```

## Expected Output

```text
Suspicious event: denied
```

## Cybersecurity Connection

This is a basic form of **rule-based detection**, similar to the idea behind simple security monitoring rules.

A real detection system would need more context before classifying an event as malicious.

---

# 6. Security Log Analysis

## Definition

Security log analysis involves examining log entries to extract useful information and identify events that may require investigation.

## Explanation

A log entry might contain:

* Timestamp
* Username
* IP address
* Event
* Status

Regex can extract these fields from predictable log formats.

## Code Example

```python
import re

log = "2026-09-21 10:30 Failed login for admin from 192.168.1.25"

username = re.search(r"for (\w+)", log)
ip_address = re.search(r"\d+\.\d+\.\d+\.\d+", log)

if username:
    print("Username:", username.group(1))

if ip_address:
    print("IP Address:", ip_address.group())
```

## Expected Output

```text
Username: admin
IP Address: 192.168.1.25
```

## Cybersecurity Connection

Log parsing is an important foundation for:

* SOC monitoring
* Incident response
* Threat detection
* Security automation
* SIEM-related workflows

---

# 7. Security Log Analyzer — Mini Project

## Objective

Build a Python program that analyzes security-style log entries using Regex.

## Features

The project will:

* Extract IP addresses
* Extract usernames
* Detect failed login attempts
* Identify suspicious keywords
* Display useful security information

## Example Input

```text
2026-09-21 10:30 Failed login for admin from 192.168.1.25
```

## Example Output

```text
Security Log Analyzer
---------------------
Event: Failed login
Username: admin
IP Address: 192.168.1.25
Status: Investigation Required
```

## Cybersecurity Connection

This project demonstrates the foundation of a simple **rule-based security log analyzer**.

It is not a replacement for a SIEM or professional detection system, but it introduces the same basic idea of extracting and analyzing security events programmatically.

---

# Security Considerations

When analyzing security data:

* Do not assume every matched pattern is malicious.
* Validate extracted information.
* Basic Regex patterns may produce false positives.
* Avoid storing sensitive information unnecessarily.
* Do not expose real credentials or private data in test logs.
* Use synthetic data for learning and GitHub projects.

---
