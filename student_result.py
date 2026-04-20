student={}

while True:
    print("_\n ----STUDENT MANAGER APP----")
    print("1. Add Student")
    print("2. view Students")
    print("3. Check Result")
    print("4. exit")

    choice = input("enter your choice:")
    # add student 
    if choice == "1":
        name = input("Enter Students name:")
        marks = int(input("Enter marks:"))
        student[name] = marks
        print(f"{name} successfully added!")
    elif choice == "2":
        if not student:
            print("No Student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
    elif choice == "3":
        name = input("Enter Student name:")
        if name in student:
            marks = student[name]
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("STUDENT NOT Found")
    elif choice == "4":
        print("Exiting......!")
        break
    else:
        print("Invalid input")
