class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            print("ok")
        else:
            print("Error str")
        if len(value) >= 8:
            print("ok")
        else:
            print("Error chr")

        self.__password = value


User1 = User("hosein71", "bHbaljjhkjk")
user2 = User("matin", "M1")
user3 = User("matin", "M1")
print(user2.password)
print(user3.password)
