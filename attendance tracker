#chatgpt ai
import csv
from datetime import datetime

def mark_attendance():
    name = input("Enter student name: ")
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    
    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time])
    
    print(f"Attendance marked for {name} on {date} at {time}")

def view_attendance():
    try:
        with open('attendance.csv', 'r') as file:
            reader = csv.reader(file)
            print("\nAttendance Records:")
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No attendance records found.")

def main():
    while True:
        print("\nAttendance Tracker")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
