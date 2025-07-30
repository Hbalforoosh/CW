class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Book:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
        self.authors = []

    def add_author(self, author):
        if isinstance(author, Author):
            self.authors.append(author)
        else:
            raise TypeError("Author must be an instance of Author class")

    def show_authors(self):
        return ", ".join(str(author) for author in self.authors)

    def show(self):
        return f"ID: {self.id}, Title: {self.title}, Price: {self.price}, Authors: {self.show_authors()}"


class PrintedBook(Book):
    def __init__(self, id, title, price, page_count):
        super().__init__(id, title, price)
        self.page_count = page_count

    def show(self):
        return super().show() + f", Pages: {self.page_count}"


class EBook(Book):
    def __init__(self, id, title, price, file_size):
        super().__init__(id, title, price)
        self.file_size = file_size

    def show(self):
        return super().show() + f", File Size: {self.file_size} MB"


author1 = Author("HoseinBlaforoosh", "Hbalforoosh@gmail.com")
author2 = Author("AliArian", "ali@gmail.com")

print_book = PrintedBook(1, "book1", 50000, 100)
print_book.add_author(author1)
print_book.add_author(author2)

E_book = EBook(2, "book2", 1500000, 250)
E_book.add_author(author1)

print(print_book.show())
print(E_book.show())
