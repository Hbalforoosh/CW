from datetime import datetime
import pickle
import Validator


class User:
    def __init__(self, username, password, email, phone):
        self.username = username
        self.__password = password
        self.email = email
        self.phone = phone
        self.tasks = []

    def check_username(self):
        if not Validator.validator_username(self.username):
            raise ValueError("Username error")

    def check_email(self):
        if not Validator.validator_email(self.email):
            raise ValueError("Email error")

    def check_password(self):
        if not Validator.validator_password(self.__password):
            raise ValueError("Password error")

    def check_phone(self):
        if not Validator.validator_phone(self.phone):
            raise ValueError("Phone error")


class Task:
    def __init__(self, title, description, start_date, end_date):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = "ToDo"
        self.change = []

    def check_end_date(self):
        if self.end_date > self.start_date:
            raise ValueError("End date is before start date.")

    def change_status(self):
        pass

    def log_changes(self):
        pass


class TaskManagerApp:

    def __init__(self):
        self.users = {}
        self.tasks = []

    def signup(self, username, password):

        signed_users = {}

        if username and password not in signed_users:
            signed_users[username] = password

        else:
            print("there is no users.")

        return signed_users

    def check_add_task(self):
        pass

    def login(self, username, password):
        if username not in self.users:
            raise ValueError

    def add_task(self):
        pass

    def remove_task(self):
        pass

    def show_task(self):
        pass

    def edit_task(self):
        pass

    def search_task(self):
        pass

    def filter_task(self):
        pass

    def save_data(self):
        with open(self.file, "wb") as f:
            pickle.dump({"users": self.users, "tasks": self.tasks}, f)

    def load_data(self):
        with open(self.file, "rb") as f:


p1 = User.signup("user1", "Ariyan", "ariyan8354")

print(p1)
