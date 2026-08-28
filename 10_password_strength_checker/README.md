# 🔐 Password Strength Checker

A beginner-friendly Python program that checks the strength of a password based on its length and character types.

## 📌 Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Calculates a strength score
- Classifies passwords as Weak, Medium, or Strong

## 🧠 Concepts Used

- Functions
- `if / elif / else`
- `len()`
- `any()`
- String methods
- `for` loops
- `import`
- `string.punctuation`
- Boolean conditions

## 🔍 How It Works

The program gives one point for each condition satisfied:

| Condition | Point |
|---|---:|
| At least 8 characters | 1 |
| Contains uppercase letter | 1 |
| Contains lowercase letter | 1 |
| Contains a number | 1 |
| Contains a special character | 1 |

The final score determines the password strength.

```text
0–2 points → Weak ❌
3–4 points → Medium ⚠️
5 points   → Strong ✅
▶️ How to Run

Run the program using:

python password_strength_checker.py

The program will ask:

🔐 PASSWORD STRENGTH CHECKER
----------------------------
Enter your password:
🧪 Example

Using a test password:

Enter your password: Hello123

Password strength: Medium ⚠️

Another example:

Enter your password: Hello@12345

Password strength: Strong ✅
🔐 Cybersecurity Connection

Password security is an important cybersecurity fundamental.

Weak passwords can be easier to guess or crack, while stronger passwords generally provide better resistance against common password attacks.

This project helped me understand how Python can be used to perform basic password-strength checks.

⚠️ Never enter your real password into a learning project or upload passwords to GitHub. Use test passwords only.

🎯 What I Learned
How to create and use functions
How to check string characteristics
How to use any()
How to use string.punctuation
How to combine multiple conditions
How to calculate a score
How to classify results based on conditions
How Python can be applied to basic cybersecurity concepts
