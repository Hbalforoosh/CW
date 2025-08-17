class student:
    def __init__(self, name, grade_list):
        self.name = name
        self.grade = grade_list

    def Average(self):
        return sum(self.grade) / len(self.grade)


student1 = student("hosein", [12, 10, 11, 9.5, 5, 7.5])
print(student1.Average())
