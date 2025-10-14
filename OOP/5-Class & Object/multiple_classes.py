class Student:
    def __init__(self, name, c_class, id) -> None:
        self.name = name
        self.c_class = c_class
        self.id = id

    def __repr__(self) -> str:
        return f"Name: {self.name}, class: {self.c_class} and id: {self.id}"


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f"Name: {self.name}, subject: {self.subject} and id: {self.id}"


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def hire(self, name, subject):
        id = len(self.teachers) + 100
        newTeacher = Teacher(name, subject, id)
        self.teachers.append(newTeacher)

    def enroll(self, name, c_class):
        id = len(self.students) + 1
        newStudent = Student(name, c_class, id)
        self.students.append(newStudent)

    def __repr__(self) -> str:
        print(f"Welcome to {self.name}")
        print("-----------OUR TEACHERS-----------")
        for teacher in self.teachers:
            print(teacher)
        print("-----------OUR STUDENTS-----------")
        for student in self.students:
            print(student)

        return (
            f"Total: {len(self.teachers)} Teachers and "
            f"{len(self.students)} Students"
        )


phitron = School("Phitron")

phitron.hire("Jhankar Mahabub", "OOP")
phitron.hire("Rifat Vai", "DSA")

phitron.enroll("Arnab Saha", "SDT")

print(phitron)
