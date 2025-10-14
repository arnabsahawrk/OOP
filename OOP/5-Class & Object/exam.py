class Exam:
    exam_name = "Phitron Exam"

    def __init__(self, subject, total_marks):
        self.subject = subject
        self.total_marks = total_marks
        self.passing_marks = 30
        self.obtained_marks = 0

    def attend_exam(self, marks):
        if marks > 0 and marks <= self.total_marks:
            self.obtained_marks = marks
        else:
            print("Invalid marks.")

    def result(self):
        if self.obtained_marks >= self.passing_marks:
            print(f"Passed with {self.obtained_marks}/{self.total_marks}")
        else:
            print(f"Failed with {self.obtained_marks}/{self.total_marks}")


my_exam = Exam("OOP", 80)
my_exam.attend_exam(0)
my_exam.attend_exam(100)
my_exam.attend_exam(40)
my_exam.result()
