# 📒 Contact Book

A beginner Python project that allows users to add, view, search, and delete contacts using a menu-driven program.

## 📌 Features

- Add a new contact
- View all contacts
- Search for a contact
- Delete a contact
- Exit the program
- Uses a dictionary to store contact information

## 🧠 Concepts Used

- Dictionaries
- Nested dictionaries
- Functions and program structure
- `while` loops
- `for` loops
- `if / elif / else`
- User input
- Dictionary methods
- `break`
- `del`

## 📂 Data Structure

Contacts are stored using a dictionary:

`python
contacts = {}

contacts["Rahul"] = {
    "phone": "9876543210",
    "email": "rahul@gmail.com"
}

The name is used as the key, while the phone number and email are stored as values.

▶️ How to Run

Run the program using:

python contact_book.py

The program displays a menu:

📒 CONTACT BOOK

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
🧪 Example
Enter your choice: 1

Enter name: Rahul
Enter phone number: 9876543210
Enter email: rahul@gmail.com

Contact added successfully! ✅

Searching for the contact:

Enter your choice: 3

Enter name to search: Rahul

Name: Rahul
Phone: 9876543210
Email: rahul@gmail.com
🔍 How It Works

The program starts with an empty dictionary:

contacts = {}

When a contact is added, its information is stored inside the dictionary:

contacts[name] = {
    "phone": phone,
    "email": email
}

The program uses a while loop to keep displaying the menu until the user chooses Exit.

The if / elif / else statements determine which operation the user selected.

The break statement stops the loop when the user chooses Exit.

⚠️ Current Limitation

Contacts are stored only in memory.

This means the contacts are lost when the program is closed.

Future versions can use file handling to permanently store the contacts.

🎯 What I Learned
How dictionaries can store structured information
How nested dictionaries work
How to build a menu-driven program
How to search and delete dictionary entries
How loops and conditions work together
How user input can control a program
