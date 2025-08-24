from datetime import datetime
import re


class CarRentalSystem:
    def __init__(self) -> None:
        self.admin = {}
        self.custumer = {}
        self.cars = []
        self.free_cars = []

    def sign_up_admin(self, email, password):
        if email in self.admin:
            raise ValueError("email already exist")
        self.admin[email] =

    def sign_in_admin()


class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password


class Customer(User):
    def __init__(self, email, password, name, phone) -> None:
        super().__init__(email, password)
        self.name = name
        self.phone = phone
        self.list_cars_customer = []

    def rental(self):

    def delivery_car(self):

    def __str__(self) -> str:
        return


class Admin(User):
    def __init__(self, email, password, admin_id) -> None:
        super().__init__(email, password)
        self.admin_id = admin_id

    def receive_car(self):


class Car:
    def __init__(self, brand, model, year, daily_rental_fee) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rental_fee = daily_rental_fee

    def show_info(self):


class Rental:
    def __init__(self, customer, car, start_date, end_date):
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date

    def rental_cost(self):
        number_of_day = (self.end_date - self.start_date).days
        return number_of_day * self.car.daily_rental_fee
