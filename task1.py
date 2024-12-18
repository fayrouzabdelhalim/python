students_data = []
while True:  
            #specifiying inputs
            std_name=input("Enter student name : ")
            sbj= str(input ("subject name  :"))
            mark= int(input ("your grade is :"))

            #marking grades
            if mark >= 90:
               grade = "A"
               print(std_name, "has a grade",grade)
            elif mark >= 80:
              grade= "B"
              print(std_name, "has a grade",grade)
            elif mark >= 60 :
                  grade= "C"
                  print(std_name, "has a grade", grade)
            else :
                grade ="fail"
                print(std_name, grade)


            #making dictionary
            student_dict = {
                    "name": std_name,
                    "subject": sbj,
                     "marks": mark,
                     "grade": grade
                }
                students_data.append(student_dict)
                for student in students_data:
                 print(student)
                 print(student_dict())

            another = input("Do you want to enter details for another student? (yes/no): ")
            if another != "yes":
               print("finished, Goodbye!")
               #printing all students data
               print("\nAll student data:")
               
                #print(student_dict)
            
               break
           




