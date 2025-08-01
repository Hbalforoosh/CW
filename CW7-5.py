from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def pay(self):
        pass

    def __repr__(self):
        return f"Name is: {self.name}, ID is: {self.id}"


class HourlyEmployee(Employee):
    def __init__(self, name, id, total_hours, hourly_salary):
        super().__init__(name, id)
        self.total_hours = total_hours
        self.hourly_salary = hourly_salary

    def pay(self):
        return self.total_hours * self.hourly_salary


class SalariedEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def pay(self):
        return self.monthly_salary


class Manager(SalariedEmployee):
    def __init__(self, name, id, monthly_salary, bonus, right_mission):
        super().__init__(name, id, monthly_salary)
        self.bonus = bonus
        self.right_mission = right_mission

    def pay(self):
        return self.monthly_salary + self.bonus + self.right_mission


class Executive(Manager):
    def __init__(self, name, id, monthly_salary, bonus, right_mission, right_attraction):
        super().__init__(name, id, monthly_salary, bonus, right_mission)
        self.right_attraction = right_attraction

    def pay(self):
        return super().pay() + self.right_attraction


class Compony:
    def __init__(self):
        self.employees_list = []

    def hire_employee(self, employee):
        self.employees_list.append(employee)
        return f"The {employee.name} was hired"

    def fire_employee(self, id):
        for employee in self.employees_list:
            if employee.id == id:
                self.employees_list.remove(employee)
                return f" The {employee.name} was fired"
            return

    def raise_employee(self, id, value_raise):
