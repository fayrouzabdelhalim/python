students_data = []

while True:  
    # Specifying inputs
    std_name = input("Enter student name: ")
    sbj = input("Subject name: ")
    
    try:
        mark = int(input("Your grade is: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value for the grade.")
        continue  # Restart the loop if the input is invalid

    # Marking grades
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"{std_name} has a grade {grade}")

    # Creating dictionary
    student_dict = {
        "name": std_name,
        "subject": sbj,
        "marks": mark,
        "grade": grade
    }

    students_data.append(student_dict)  # Store data correctly

    # Printing all stored student data
    print("\nCurrent Student Data:")
    for student in students_data:
        print(student)  # Print each stored student dictionary

    # Asking if the user wants to continue
    another = input("Do you want to enter details for another student? (yes/no): ").strip().lower()
    if another != "yes":
        print("\nFinished, Goodbye!")
        print("\nAll Student Data:")
        for student in students_data:
            print(student)  # Print all collected data before exiting
        break
