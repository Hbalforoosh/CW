class Book:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price


class Printed_Book(Book):
    def __init__(self, id, title, price, page_count):
        super().__init__(id, title, price)
        self.page_count = page_count

    def show(self):
        return super().sh


class E_Book(Book):
    def __init__(self, id, title, price, file_size):
        super().__init__(id, title, price)
        self.file_size = file_size

    def show(self):
        return


class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_author(self):
        return f"Author: {self.name} & Email: {self.email}"
