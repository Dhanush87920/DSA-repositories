#chatgpt ai
def calculate_gpa(grades, credits):
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits if total_credits != 0 else 0

def get_grade_point(grade):
    grade_scale = {
        'A+': 4.0, 'A': 3.7, 'A-': 3.5,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }
    return grade_scale.get(grade.upper(), 0.0)

def main():
    num_courses = int(input("Enter the number of courses: "))
    grades = []
    credits = []
    
    for i in range(num_courses):
        grade = input(f"Enter grade for course {i + 1} (A+, A, B+, etc.): ")
        credit = float(input(f"Enter credit hours for course {i + 1}: "))
        grades.append(get_grade_point(grade))
        credits.append(credit)
    
    gpa = calculate_gpa(grades, credits)
    print(f"\nYour GPA is: {round(gpa, 2)}")

if __name__ == "__main__":
    main()
