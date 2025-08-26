from datetime import datetime
import Validator
import logging


class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.__password = password
        self.role = None
        self.validate_email()
        self.validate_password()

    def validate_email(self):
        if not Validator.validator_email(self.email):
            raise ValueError("Email error")

    def validate_password(self):
        if not Validator.validator_password(self.__password):
            raise ValueError("Password error")

    def check_password(self, input_password):
        return self.__password == input_password


class Customer(User):
    def __init__(self, email, password, name, phone) -> None:
        super().__init__(email, password)
        self.name = name
        self.phone = phone
        self.role = "customer"
        self.list_cars_customer = []

    def rental(self, car, start_date, end_date):
        if not car.availabity:
            raise ValueError("this car not available")
        rental_days = (end_date - start_date).days
        rental_fee = rental_days * car.daily_rental_fee
        new_rental = Rental(self, car, start_date, end_date, rental_fee)
        self.list_cars_customer.append(new_rental)
        car.availability = False
        logging.info(f'{new_rental} was registered')

    def delivery_car(self, rental, return_date):
        if rental not in self.list_cars_customer:
            raise ValueError("this rental not found")
        rental.car.availabity = True
        rental.return_date = return_date
        logging.info(f'{rental} Delivered successfully.')

    def __str__(self):
        return f"""
    #Customer Information:
    1. Name: {self.name}
    2. Email: {self.email}
    3. Phone: {self.phone}
    4. Number of rentals : {len(self.list_cars_customer)}
---------------------------------------------------------
"""


class Admin(User):
    def __init__(self, email, password, admin_id) -> None:
        super().__init__(email, password)
        self.admin_id = admin_id
        self.role = "admin"

    def receive_car(self):
        pass


class CarRentalSystem:
    def __init__(self) -> None:
        self.users = {}
        self.cars = []
        self.available_cars = []
        self.rentals = []

    def sign_up_admin(self, email, password, admin_id):
        if email in self.users:
            raise ValueError("email already exist")
        new_admin = Admin(email, password, admin_id)
        self.users[email] = new_admin

    def sign_up_customer(self, email, name, phone, password):
        if email in self.users:
            raise ValueError("email already exist")
        new_customer = Customer(email, name, phone, password)
        self.users[email] = new_customer

    def sign_in(self, email, password):
        if email not in self.users:
            raise ValueError("this user not found")
        user = self.users[email]
        if not user.check_password(password):
            raise ValueError("Password Incorrect")
        return user


class Car:
    def __init__(self, brand, model, year, daily_rental_fee, car_id, availablity=True) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rental_fee = daily_rental_fee
        self.car_id = car_id
        self.availabity = availablity

    def show_info(self):
        pass


class Rental:
    def __init__(self, customer, car, start_date, end_date, rental_fee):
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.rental_fee = rental_fee

    def rental_cost(self):
        number_of_day = (self.end_date - self.start_date).days
        return number_of_day * self.car.daily_rental_fee
