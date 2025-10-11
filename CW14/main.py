
from api import BookManager
api = "https://68e8e9fef2707e6128ccbf93.mockapi.io/books"
manager = BookManager(api)


def main():
    while True:
        print("------Menu------")
        print("1.Get")
        print("2.Add")
        print("3.Update")
        print("4.Search")
        print("5.Exit")

        choice = input("Enter (1-5):")
        if choice == "5":
            print("Goodby!")
        break


if __name__ == "__main__":
    main()
