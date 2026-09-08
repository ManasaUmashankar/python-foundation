# Day 1 - Scope

name = "Global Manasa"


def show_name():
    name = "Local Manasa"
    print("Inside function:", name)


show_name()

print("Outside function:", name)


# Global variable
course = "Cybersecurity"


def show_course():
    print("Course:", course)


show_course()

----------

▶️ Expected Output
Inside function: Local Manasa
Outside function: Global Manasa
Course: Cybersecurity
🧠 What happened here ?
name = "Global Manasa" ( This is a global variable because it's outside the function)

Inside:
def show_name():
    name = "Local Manasa"

(This creates a local variable. It exists only inside show_name().)

So Python chooses:

Inside function  → Local Manasa
Outside function → Global Manasa

That's part of the LEGB rule:
L → Local
E → Enclosing
G → Global
B → Built-in
