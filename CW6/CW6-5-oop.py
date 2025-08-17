class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def append_grade(self, grade):
        self.grades.append(grade)

    def Show(self):
        return f"{self.name}'s grades is: {self.grades}"


class SchoolStaff:
    def __init__(self, name, role):
        # if role != "teacher" or role != "admin":
        #     raise ValueError(
        #         'You are only allowed to choose the "teacher" and "admin" roles'
        #     )
        self.name = name
        self.role = role

    def set_grade(self, student: Student, grade):
        if self.role != "teacher":
            raise PermissionError("You do not have permission to edit")
        if grade < 0 or grade > 20:
            raise ValueError("Scores must be between 0 and 20")
        student.append_grade(grade)
        return f"{student}'s Grade is: {grade}"

    def __str__(self):
        return f"Name: {self.name} | Role: {self.role}"


S1 = SchoolStaff("Ali", "teacher")
S2 = SchoolStaff("Romina", "admin")
S3 = SchoolStaff("Mahdi", "manager")

student1 = Student("hosein")
S1.set_grade(student1, 10.5)
# S2.set_grade(student1, 20)
print(S1)
print(S2)
print(S3)
print(student1.Show())
