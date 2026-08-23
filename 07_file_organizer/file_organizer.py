# File Organizer
# Python Foundation - Project 07

import os
import shutil

folder = input("Enter the folder path: ")

files = os.listdir(folder)

for file in files:

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            folder_name = "Images"

        elif extension in [".pdf", ".doc", ".docx", ".txt"]:
            folder_name = "Documents"

        elif extension in [".mp3", ".wav"]:
            folder_name = "Audio"

        elif extension in [".mp4", ".mkv", ".avi"]:
            folder_name = "Videos"

        else:
            folder_name = "Others"

        destination = os.path.join(folder, folder_name)

        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully! 📁")
