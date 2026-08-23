# 📁 File Organizer

A beginner Python program that automatically organizes files into folders based on their file extensions.

## 📌 Features

- Scans files inside a selected folder
- Detects file extensions
- Creates folders automatically
- Organizes files into categories
- Moves files using Python

## 📂 Categories

The program currently organizes files into:

- **Images** → `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents** → `.pdf`, `.doc`, `.docx`, `.txt`
- **Audio** → `.mp3`, `.wav`
- **Videos** → `.mp4`, `.mkv`, `.avi`
- **Others** → Other file types

## 🧠 Concepts Used

- `os` module
- `shutil` module
- `os.listdir()`
- `os.path.join()`
- `os.path.isfile()`
- `os.path.splitext()`
- `os.makedirs()`
- `shutil.move()`
- `if / elif / else`
- Lists
- Loops

## ▶️ How to Run

Run the program using:

bash
python file_organizer.py

Enter the path of the folder you want to organize.

💻 Example

Before:

test_folder/
├── photo.jpg
├── notes.txt
├── song.mp3
└── movie.mp4

After:

test_folder/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.txt
├── Audio/
│   └── song.mp3
└── Videos/
    └── movie.mp4
🔍 How It Works

The program first gets the files inside the selected folder:

files = os.listdir(folder)

It then checks whether each item is a file:

if os.path.isfile(file_path):

The file extension is extracted using:

extension = os.path.splitext(file)[1].lower()

The appropriate folder is selected based on the extension.

If the folder doesn't exist, it is created:

os.makedirs(destination, exist_ok=True)

Finally, the file is moved:

shutil.move(file_path, os.path.join(destination, file))
⚠️ Note

This program actually moves files.

For testing, it is recommended to use a test folder containing copies of files rather than important personal files.

🎯 Purpose

This project was created to practice Python's interaction with the operating system and to understand basic file automation.
