# 🧠 Quiz Game

A beginner-friendly Python quiz game based on basic computer science, Linux, networking, and cybersecurity concepts.

## 📌 Features

- Multiple-choice questions
- Five questions
- Automatic score calculation
- Percentage calculation
- Instant feedback
- Final performance message
- Menu-free command-line interface

## 🧠 Concepts Used

- Functions
- Lists
- Dictionaries
- Nested data structures
- `for` loops
- `if / elif / else`
- `input()`
- `enumerate()`
- `len()`
- String methods
- Arithmetic operations
- f-strings

## 📂 Data Structure

The questions are stored inside a list of dictionaries:

```python
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit"],
        "answer": "A"
    }
]

Each question contains:

The question
Multiple options
The correct answer
▶️ How to Run

Run the program using:

python quiz_game.py
🧪 Example
🧠 CYBERSECURITY BASICS QUIZ
-----------------------------

Question 1: What does CPU stand for?

A. Central Processing Unit
B. Computer Personal Unit
C. Central Program Utility
D. Control Processing Unit

Your answer: A

Correct! ✅

At the end:

🎯 QUIZ COMPLETE!
Your score: 4/5
Percentage: 80%
Good job! 👍
🔍 How It Works

The program stores all questions in a list.

A for loop goes through each question:

for number, question in enumerate(questions, start=1):

The user's answer is converted to uppercase:

user_answer = input("Your answer: ").upper()

The answer is then compared with the correct answer:

if user_answer == question["answer"]:

If the answer is correct, the score increases:

score += 1

Finally, the program calculates the percentage:

percentage = (score / len(questions)) * 100
🎯 What I Learned
How to store structured data using lists and dictionaries
How to create a quiz using Python
How to use enumerate()
How to calculate scores
How to calculate percentages
How to use loops and conditions together
How to create reusable functions
How to provide feedback based on a user's score
🔐 Cybersecurity Connection

The questions in this project introduce basic concepts related to:

Linux
Networking
Computer systems
Cybersecurity fundamentals

This project also demonstrates how Python can be used to create simple interactive security-learning tools.
