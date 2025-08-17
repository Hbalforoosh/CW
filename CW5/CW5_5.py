class Employee:
    total_employees = 0
    list_of_total_employees = []

    def __init__(self, name, age, salary):
        if self.validate_name(name):
            print("name invalid")
        self.name = name
        self.age = age
        self.salary = salary
        Employee.total_employees += 1

    def give_raise(self, value):
        if value > 0:
            self.salary += value

    @classmethod
    def give_raise_to_all(cls, value):
        if value > 0:
            for i in cls.list_of_total_employees:
                i.salary += value
            return value

    @classmethod
    def average_salary(cls):
        total_salary = sum(i.salary for i in cls.list_of_total_employees)
        return total_salary / cls.total_employees

    @staticmethod
    def validate_name(name):
        return name.isalpha()


employ1 = Employee("hosein", 700, 1800)
employ2 = Employee("matin", 750, 1900)
employ3 = Employee("mehdi", 50, 5000)
