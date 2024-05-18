class Student:
    def __init__(self, name, id, year):
        self.name = name
        self.id = id
        self.year = year
        self.attendance = {}

    def mark_attendance(self, date):
        self.attendance[date] = True

    def display_attendance(self):
        print("Attendance for", self.name)
        for date, present in self.attendance.items():
            print(date, ": Present" if present else ": Absent")
        print()


class StudentOperation:
    def __init__(self):
        self.students = []

    def registration(self):
        name = input("Please Enter Name: ")
        id = input("Please Enter A Id: ")
        year = int(input("Please Enter Student Year: "))
        student = Student(name, id, year)
        self.students.append(student)
        print("One student is inserted. Now total students are:", len(self.students))
        print()

    def mark_attendance(self):
        id = input("Please Enter Student ID: ")
        date = input("Please Enter Attendance Date (): ")
        for student in self.students:
            if student.id.lower() == id.lower():
                student.mark_attendance(date)
                print("Attendance marked for", student.name)
                return
        print("No student found with the given ID.")

    def search_by_id(self):
        id = input("Please Enter A Valid Id: ")
        for student in self.students:
            if id.lower() == student.id.lower():
                self.display(student)
                return
        print("No student found.")

    def search_by_year(self):
        year = int(input("Please Enter A Valid Year: "))
        print("Searching student... Year: ")
        for student in self.students:
            if student.year == year:
                self.display(student)

    def delete(self):
        id = input("Please Enter A Valid Id: ")
        for student in self.students:
            if id.lower() == student.id.lower():
                self.display(student)
                self.students.remove(student)
                print("Removed successfully, total students are:", len(self.students))
                return
        print("No student found.")

    def display(self, student):
        print("Name:", student.name)
        print("Id:", student.id)
        print("Year:", student.year)
        student.display_attendance()


class Teacher:
    def __init__(self, name, id, initial):
        self.name = name
        self.id = id
        self.initial = initial


class TeacherOperation:
    def __init__(self):
        self.teachers = []

    def registration(self):
        name = input("Please Enter Name: ")
        id = input("Please Enter A Valid Id: ")
        initial = input("Please Enter Teacher Initial: ")
        teacher = Teacher(name, id, initial)
        self.teachers.append(teacher)
        print("One teacher is inserted. Now total teachers are:", len(self.teachers))
        print()

    def search_by_id(self):
        id = input("Please Enter A Valid Id: ")
        for teacher in self.teachers:
            if id.lower() == teacher.id.lower():
                self.display(teacher)
                return
        print("No teacher found.")

    def search_by_initial(self):
        initial = input("Please Enter Teacher Initial: ")
        for teacher in self.teachers:
            if initial.lower() == teacher.initial.lower():
                self.display(teacher)
                return
        print("No teacher found with the given initial.")

    def delete(self):
        id = input("Please Enter A Valid Id: ")
        for teacher in self.teachers:
            if id.lower() == teacher.id.lower():
                self.display(teacher)
                self.teachers.remove(teacher)
                print("Removed successfully, total teachers are:", len(self.teachers))
                return
        print("No teacher found.")

    def display(self, teacher):
        print("Name:", teacher.name)
        print("Id:", teacher.id)
        print("Initial:", teacher.initial)
        print()


if __name__ == "__main__":
    print("Welcome to management system")
    student_operation = StudentOperation()
    teacher_operation = TeacherOperation()

    while True:
        print("1 for student registration")
        print("2 for student search by id")
        print("3 for remove student by id")
        print("4 for search student by year")
        print("5 for mark student attendance")
        print("6 for teacher registration")
        print("7 for teacher search by id")
        print("8 for teacher search by initial")
        print("9 for remove teacher by id")
        print("0 for exit the system")

        choice = int(input())

        if choice == 1:
            student_operation.registration()
        elif choice == 2:
            student_operation.search_by_id()
        elif choice == 3:
            student_operation.delete()
        elif choice == 4:
            student_operation.search_by_year()
        elif choice == 5:
            student_operation.mark_attendance()
        elif choice == 6:
            teacher_operation.registration()
        elif choice == 7:
            teacher_operation.search_by_id()
        elif choice == 8:
            teacher_operation.search_by_initial()
        elif choice == 9:
            teacher_operation.delete()
        elif choice == 0:
            break

    print("Thank you for using our system")
