
from users import Person


class Admin(Person):
    def __init__(self, username, password):
        super().__init__(username, password)

    def dashboard(self):
        print("--- Admin Dashboard ---")
        print("1.Adding new trip")
        print("2. delete trip")
        print("3. Show users")
        print("4. Exit")
