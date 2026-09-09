

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

