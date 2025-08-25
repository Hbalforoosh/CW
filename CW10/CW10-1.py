from datetime import datetime
import pickle
import Validator
import logging


class User:
    def __init__(self, username, password, email, phone):
        self.username = username
        self.__password = password
        self.email = email
        self.phone = phone
        self.tasks = []
        self.validate_email()
        self.validate_password()
        self.validate_username()
        self.validate_phone()

    def validate_username(self):
        if not Validator.validator_username(self.username):
            raise ValueError("Username error")

    def validate_email(self):
        if not Validator.validator_email(self.email):
            raise ValueError("Email error")

    def validate_password(self):
        if not Validator.validator_password(self.__password):
            raise ValueError("Password error")

    def validate_phone(self):
        if not Validator.validator_phone(self.phone):
            raise ValueError("Phone error")

    def check_password(self, input_password):
        return self.__password == input_password


class Task:
    def __init__(self, title, description, start_date, end_date, priority, urgency):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.urgency = urgency
        self.status = "ToDo"
        self.change_history = []

    def check_end_date(self):
        if self.end_date > self.start_date:
            raise ValueError("End date is before start date.")

    def change_status(self):
        date_of_the_day = datetime.now().date()
        if date_of_the_day < self.start_date:
            self.status = "ToDo"
        elif self.start_date <= date_of_the_day <= self.end_date:
            self.status = "In Progress"
        else:
            self.status = "Expired"
        self.log_changes()

    def log_changes(self):
        logging.info(f'Task {self.title} change to {self.status}')


class TaskManagerApp:

    def __init__(self):
        self.users = {}
        self.tasks = []

    def sign_up(self, username, password, email, phone):
        if username in self.users:
            raise ValueError("This user already exists")
        new_user = User(username, password, email, phone)
        self.users[username] = new_user
        logging.info(f'{username} signed_up')

    def sign_in(self, username, password):
        if username not in self.users:
            raise ValueError("this username not found")
        user = self.users[username]
        if not user.check_password(password):
            raise ValueError("password is incorrect")
        logging.info(f'{username} signed in')
        return username

    def add_task(self, user, title, description, start_date, end_date, priority, urgency):
        if user not in self.users:
            raise ValueError("this user not found")
        task_user = Task(title, description, start_date,
                         end_date, priority, urgency)
        self.users[user].tasks.append(task_user)
        self.tasks.append(task_user)
        logging.info(f"Task {title} add for {user}")

    def check_add_task(self, start_date, end_date):
        if end_date <= start_date:
            raise ValueError("End date must be after start date")

    def remove_task(self, user, title):
        if user not in self.users:
            raise ValueError("this user not found")
        for task in self.users[user].tasks:
            if task.title == title:
                self.users[user].tasks.remove(task)
                self.tasks.remove(task)
                logging.info(f"Task {title} from task's list {user} removed")
                return
        raise ValueError("this title not found")

    def show_task(self, user):
        if user not in self.users:
            raise ValueError("this user not found")
        elif not self.users[user].task:
            return f'{user} The user has no tasks to display.'
        else:
            for i, task in enumerate(self.users[user].tasks, 1):
                print(f'{i}. |Title : {task.title}')
                print(f'     |Start_date : {task.satrt_date}')
                print(f'     |End_date : {task.End_date}')
                print(f'     |Status: {task.status}')
                print(f'     |Priority: {task.priority}')
                print(f'     |Urgency: {task.urgency}')

    def edit_task(self, user, old_title, **new_task):
        if user not in self.users:
            raise ValueError("this user not found")
        for task in self.users[user].tasks:
            if task.title == old_title:
                task.title = new_task["title"]
                task.description = new_task["description"]
                task.start_date = new_task["start_date"]
                task.end_date = new_task["end_date"]
                task.priority = new_task["priority"]
                task.urgency = new_task["urgency"]
                task.change_status()
                logging.info(f'{old_title} updated')
            else:
                return

        raise ValueError("this task not found")

    def search_task(self, user, word):
        result = []
        if user not in self.users:
            raise ValueError("this user not found")
        for task in self.users[user].tasks:
            if word in task.title or word in task.description or word in task.priority or word in task.urgency:
                result.append(word)
        return result

    def filter_task(self, user, filter_type, filter_value):
        filter_indicator = ["priority", "urgency",
                            "status", "start_date", "end_date"]
        if user not in self.users:
            raise ValueError("this user not found")
        if filter_type not in filter_indicator:
            raise ValueError("the filter type invalid")
        results_of_filtering = []
        for task in self.users[user].task:
            if filter_type == "priority" and filter_value == task.priority:
                results_of_filtering.append(task)

            elif filter_type == "urgency" and filter_value == task.urgency:
                results_of_filtering.append(task)

            elif filter_type == "status" and filter_value == task.status:
                results_of_filtering.append(task)

            elif filter_type == "start_date" and filter_value == task.start_date:
                results_of_filtering.append(task)

            elif filter_type == "end_date" and filter_value == task.end_date:
                results_of_filtering.append(task)
        return results_of_filtering

    def save_data(self, file="TaskManagerApp.pk"):
        try:
            with open(file, "wb") as f:
                pickle.dump({"users": self.users, "tasks": self.tasks}, f)
                logging.info("Data saved successfully")
        except Exception as e:
            ValueError({e})

    def load_data(self, file="TaskManagerApp.pk"):
        try:
            with open(file, "rb") as f:
                data = pickle.load(f)
                self.users = data["users"]
                self.tasks = data["tasks"]
                logging.info("Data saved successfully")
        except FileNotFoundError:
            FileNotFoundError("No data found")
        except Exception as e:
            ValueError({e})


#####################################################################
app = TaskManagerApp()
app.sign_up("Hosein", "Hosein1371", "Hbal@gmail.com", "09210827018")
# app.sign_up("Ali", "Ali1375", "Ali@gmail.com", "09365265878")
print("sigh_up")
