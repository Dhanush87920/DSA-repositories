#chatgpt ai
import os

def display_menu():
    print("\nNotes Organizer")
    print("1. Create a New Note")
    print("2. View Notes")
    print("3. Delete a Note")
    print("4. Exit")

def create_note():
    title = input("Enter note title: ") + ".txt"
    content = input("Enter your note: ")
    with open(title, 'w') as file:
        file.write(content)
    print(f"Note '{title}' saved successfully!")

def view_notes():
    notes = [f for f in os.listdir() if f.endswith(".txt")]
    if not notes:
        print("No notes found.")
        return
    print("\nYour Notes:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    choice = int(input("Enter note number to read (0 to go back): "))
    if choice > 0 and choice <= len(notes):
        with open(notes[choice - 1], 'r') as file:
            print("\n" + file.read())

def delete_note():
    notes = [f for f in os.listdir() if f.endswith(".txt")]
    if not notes:
        print("No notes to delete.")
        return
    print("\nYour Notes:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    choice = int(input("Enter note number to delete (0 to cancel): "))
    if choice > 0 and choice <= len(notes):
        os.remove(notes[choice - 1])
        print("Note deleted successfully!")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
