class Student:
    def __init__(self, name: str, age: int, address: str, marks: int):
        self.name = name
        self.age = age
        self.address = address  # fixed typo: 'adress' to 'address'
        self.marks = marks


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Invalid input! Age and marks must be numbers.")
            return

        student = Student(name, age, address, marks)
        self.students.append(student)
        print("Student successfully added.\n")
        return student

    def view_students(self):
        if not self.students:
            print("⚠️ No students found.\n")
            return

        view_type = input("View all students or one student? (all/one): ").strip().lower()

        if view_type == "all":
            for student in self.students:
                self.display_student(student)

        elif view_type == "one":
            name = input("Enter the name of the student you want to see: ").strip()
            for student in self.students:
                if student.name.lower() == name.lower():
                    self.display_student(student)
                    return
            print("Student not found.\n")
        else:
            print("Invalid option. Please choose 'all' or 'one'.\n")

    def delete_student(self):
        name = input("Enter the name of the student you want to delete: ").strip()
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print("🗑️ Student successfully deleted.\n")
                return
        print("Student not found.\n")

    def update_student(self):
        name = input("Enter the name of the student you want to update: ").strip()
        for student in self.students:
            if student.name.lower() == name.lower():
                student.name = input("Enter new name: ")
                try:
                    student.age = int(input("Enter new age: "))
                    student.address = input("Enter new address: ")
                    student.marks = int(input("Enter new marks: "))
                except ValueError:
                    print("Invalid input! Age and marks must be numbers.")
                    return
                print("Student successfully updated.\n")
                return
        print("Student not found.\n")

    def display_student(self, student):
        print(f"\nName: {student.name}")
        print(f"Age: {student.age}")
        print(f"Address: {student.address}")
        print(f"Marks: {student.marks}\n")


def show_menu():
    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Student(s)")
    print("5. Exit")
    print("===============================================\n")


# Main program loop
system = StudentManagementSystem()

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number (1-5).\n")
        continue

    if choice == 1:
        system.add_student()
    elif choice == 2:
        system.delete_student()
    elif choice == 3:
        system.update_student()
    elif choice == 4:
        system.view_students()
    elif choice == 5:
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
