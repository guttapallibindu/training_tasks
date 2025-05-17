class Student:
    def __init__(self, student_id, name, course, marks):
        self.__student_id = student_id #encapsulating
        self.__name = name
        self.__course = course
        self.__marks = marks

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def __str__(self):
        return f"ID: {self.__student_id} | Name: {self.__name}| Course: {self.__course}| Marks: {self.__marks}"


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.get_id()] = student
        print("Student added successfully.")
        print("\nCurrent Student Records:")
        for stud in self.students.values():
            print(stud)

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    def update_student(self, student_id, name=None, course=None, marks=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student.set_name(name)
            if course:
                student.set_course(course)
            if marks is not None:
                student.set_marks(marks)
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def view_all_students(self):
        if not self.students:
            print("No student records available.")
        else:
            print("\n--- All Student Records ---")
            for student in self.students.values():
                print(student)


class main(StudentManager):
    def run(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. View All Students")
            print("6. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                sid = input("Enter ID: ")
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                marks = int(input("Enter Marks: "))
                student = Student(sid, name, course, marks)
                self.add_student(student)

            elif choice == "2":
                sid = input("Enter ID to view: ")
                self.view_student(sid)

            elif choice == "3":
                sid = input("Enter ID to update: ")
                name = input("New Name (press enter to skip): ")
                course = input("New Course (press enter to skip): ")
                marks_input = input("New Marks (press enter to skip): ")
                marks = int(marks_input) if marks_input else None
                self.update_student(sid, name or None, course or None, marks)

            elif choice == "4":
                sid = input("Enter ID to delete: ")
                self.delete_student(sid)

            elif choice == "5":
                self.view_all_students()

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main = main()
    main.run()