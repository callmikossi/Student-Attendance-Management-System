students = []

def add_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "name": name,
        "matric": matric,
        "department": department
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students available.\n")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Matric Number: {student['matric']}")
        print(f"Department: {student['department']}")
        print("-------------------------")

def search_student():
    matric = input("Enter matric number to search: ")
    for student in students:
        if student["matric"] == matric:
            print("Student Found:")
            print(student)
            return
    print("Student not found.\n")

def main():
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
