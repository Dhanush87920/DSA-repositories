#chatgpt ai
import datetime
import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter assignment title: ")
    due_date = input("Enter deadline (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
        tasks.append({"title": title, "due_date": due_date})
        save_tasks(tasks)
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_tasks():
    if not tasks:
        print("No assignments found.")
        return
    print("\nUpcoming Assignments:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("Task removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global tasks
    tasks = load_tasks()
    while True:
        print("\nAssignment Deadline Reminder")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Remove Assignment")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
