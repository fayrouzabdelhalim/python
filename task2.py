# Define the student data
students = [
    {"Student Name": "Maher", "Subject": "English", "Degree": 45},
    {"Student Name": "Madeh", "Subject": "Arabic", "Degree": 95},
    {"Student Name": "Fayrouz", "Subject": "Math", "Degree": 75},
    {"Student Name": "Basmala", "Subject": "History", "Degree": 85},
    {"Student Name": "Aml", "Subject": "English", "Degree": 65},
    {"Student Name": "Nadine", "Subject": "Math", "Degree": 61},
]

# Write the data to a text file
with open("students.txt", "w") as file:
    file.write("Student Name | Subject  | Degree | Grade\n")
    file.write("-" * 40 + "\n")  # Separator line
    for student in students:
        # Assign grade based on marks
        if student["Degree"] >= 90:
            grade = "A"
        elif student["Degree"] >= 80:
            grade = "B"
        elif student["Degree"] >= 60:
            grade = "C"
        else:
            grade = "Fail"

        file.write(f"{student['Student Name']:12} | {student['Subject']:8} | {student['Degree']:6} | {grade}\n")

print("File 'students.txt' has been created successfully.")

# Updated system 

# Function to load student data from file
def load_students(filename):
    students = {}  # Dictionary to store student data
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header line
            next(file)  # Skip separator line
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    name, subject, marks, grade = parts
                    students[name.strip()] = {
                        "subject": subject.strip(),
                        "marks": int(marks.strip()),
                        "grade": grade.strip()
                    }
    except FileNotFoundError:
        print(f"Warning: {filename} not found. A new file will be created.")
    return students

# Function to assign grades
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

# Function to save student data to file
def save_students(filename, students):
    with open(filename, "w") as file:
        file.write("Student Name | Subject  | Degree | Grade\n")  # Header
        file.write("-" * 40 + "\n")
        for name, data in students.items():
            file.write(f"{name:12} | {data['subject']:8} | {data['marks']:6} | {data['grade']}\n")

# File where student records are stored
students_file = "students.txt"
students_data = load_students(students_file)

print("Hi! This is a student management system to help you.")
print("In case you want to leave, enter 'Exit'.")

while True:
    choice = input("\nDo you want to add a new student or view grades? (view/add): ").strip().lower()

    if choice == "exit":
        print("Goodbye! Saving data...")
        save_students(students_file, students_data)
        break

    elif choice == "add":
        while True:
            std_name = input("Enter student name: ").strip()
            if std_name.lower() == "exit":
                break

            sbj = input("Enter subject: ").strip()

            try:
                mark = int(input("Enter marks: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value for marks.")
                continue

            # Assign grade based on marks
            grade = assign_grade(mark)

            students_data[std_name] = {"subject": sbj, "marks": mark, "grade": grade}
            print(f"Student {std_name} added successfully with grade {grade}!")

            more = input("Do you want to add another student? (yes/no): ").strip().lower()
            if more != "yes":
                break

    elif choice == "view":
        std_name = input("Enter student name: ").strip()
        if std_name in students_data:
            print(f"{std_name} - Subject: {students_data[std_name]['subject']}, Marks: {students_data[std_name]['marks']}, Grade: {students_data[std_name]['grade']}")
        else:
            print("Student not found!")

    else:
        print("Invalid choice! Please enter 'view' or 'add'.")
