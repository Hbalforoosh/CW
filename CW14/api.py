
import requests
import json
api = "https://68e8e9fef2707e6128ccbf93.mockapi.io/books"


class BookManager:
    try:
        def __init__(self, base_url):
            self.base_url = base_url

        def get(self):
            response = requests.get(self.base_url)
            if response.status_code == 200:
                books = response.json()
                return books
            else:
                print(response.status_code)
                return None
    except Exception as e:
        print(f"Error : {e}")

    def add(self, book_data):
        response = requests.post(self.base_url, json=book_data)
        if response.status_code == 201:
            print("Adding book is successfully")
            return response.json()
        else:
            print(response.status_code)
            return None

    def update(self, book_id, update_data):
        book_url = f"{self.base_url}/{book_id}"
        response = requests.patch(book_url, json=update_data)
        if response.status_code == 200:
            print("update data was successfully.")
            return None
        else:
            print(response.status_code)

    def search(self, title):
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                books = response.json()
                for book in books:
                    if book.get("title") == title:
                        print(f"ID: {book['id']}")

        except Exception as e:
            print(f"Error : {e}")


# title = input("Enter your title: ")
# manager = BookManager(api)
# manager.search(title)
# # books = manager.get()
# if books:
#     for book in books:
#         print(book)

# book_data = {
#     "title": input("enter title: "),
#     "author": input("enter author: "),
#     "year": int(input("enter year: ")),
#     "category": input("enter category: "),
#     "summary": input("enter summury: ")
# }

# result = manager.add(book_data)
# # if book_data:
# #     for key, Value in book_data.items():
# #         print(key, Value)
# if result:
#     print("Successfully")
#     print(f"{result['id']}")
# else:
#     print("error!!!!")
