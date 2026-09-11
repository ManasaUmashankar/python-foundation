# Mini Project
# File-Based Notes System


def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()

        if notes:
            print("\nYour Notes:")
            print("-----------")
            print(notes)
        else:
            print("No notes found.")

    except FileNotFoundError:
        print("No notes file found.")


def main():
    print("File-Based Notes System")
    print("-----------------------")
    print("1. Add Note")
    print("2. View Notes")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
