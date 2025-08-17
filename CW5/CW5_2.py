class Bank_Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, rial):
        if self.check_deposit(rial):
            self.balance += rial
            print(f"mojodi: {self.balance}")
        else:
            print("enter positive number")

    def withdraw(self, rial):
        if self.check_deposit(rial):
            if rial > self.balance:
                print("mojodi kafi nist")
        else:
            self.balance -= rial
            print("mojodi1: ", rial)

    def check(self):
        return self.balance

    @staticmethod
    def check_deposit(value):
        if value > 0:
            return True
        else:
            return False


acc = Bank_Account(1000)
acc.check()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
acc.check()
