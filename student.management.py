class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


students = []

while True:
    print("\n- STUDENT MANAGEMENT SYSTEM -")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update student's details")
    print("5. Delete student")
    print("6. Save to file")
    print("7. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        roll = int(input("Enter roll number = "))
        name = input("Enter name = ")
        marks = int(input("Enter marks = "))

        s = Student(roll, name, marks)
        students.append(s)

        print("Student added successfully ")

    elif choice == 2:
        if not students:
            print("No students found ")
        else:
            for s in students:
                print("Roll:", s.roll, "Name:", s.name, "Marks:", s.marks)

    elif choice == 3:
        r = int(input("Enter roll number to search = "))
        found = False

        for s in students:
            if s.roll == r:
                print("Student Found ")
                print("Roll:", s.roll)
                print("Name:", s.name)
                print("Marks:", s.marks)
                found = True
                break

        if not found:
            print("Student not found ")
            
    elif choice == 4:
        r = int(input("Enter student's roll number ="))
        found = False
        for s in students :
            if s.roll == r :
                print("Current name =", s.name)
                print("Current marks =", s.marks)
                s.name = input("Enter new name =")
                s.marks = int(input("Enter new marks ="))
                print("Student's details updated")
                found = True
                break
        if not found :
                print("Student not found")
    elif choice == 5 :
        r = int(input("Enter student's roll number ="))
        found = False
        for s in students :
            if s.roll == r :
                students.remove(s)
                print("Student deleted")
                found = True
                break
        if not found:
                print("Student not found")
    elif choice == 6 :
        with open("student.txt","w") as file:
            for s in students :
                file.write(f"{s.roll} , {s.name} , {s.marks} \n")
        print("Data saved successfully")

    elif choice == 7:
        print("Exiting program ")
        break

    else:
        print("Invalid choice ")