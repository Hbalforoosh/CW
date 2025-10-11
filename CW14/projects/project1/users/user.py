from users import Person
from requerments import exceptions, validate


class User(Person):

    def __init__(self, username, password, email, phone, balance=0):
        super().__init__(username, password)
        validate.validator_email(email)
        validate.validator_phone(phone)

        self.email = email
        self.phone = phone
        self._balance = balance
        self._tickets = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("The balance is negative!!!!")
        self._balance = value

    def add_balance(self, amount):
        if amount <= 0:
            raise ValueError("Amount added must be positive")
        self._balance += amount
        print(f"Amount {amount} Added : {self._balance}")

    def buy_ticket(self, trip):
        if self._balance < trip.price:
            raise ValueError("Not enough credit!")
        if trip.available_seats <= 0:
            raise ValueError("Trip capacity is full")
        trip.seat_reservation(1)
        self._balance -= trip.price
        self._tickets.append(trip)
        print(
            f"Ticket purchased successfully.Details : Origin:{trip.origin}, Destination:{trip.destination}"
        )

    def dashboard(self):
        print(f"---- User Dashboard ----")
        print(f"Username: {self._username}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Balance: {self._balance}")
        print(f"Number of tickets : {len(self._tickets)}")
