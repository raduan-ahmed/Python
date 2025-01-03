from abc import ABC, abstractmethod
import hashlib
from datetime import datetime, timedelta

# Abstract Class - Library Item
class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Encapsulation - Book class
class Book(LibraryItem):
    def __init__(self, title, author, published_year, price, copies):
        self.__title = title
        self.__author = author
        self.__published_year = published_year
        self.__price = price
        self.__copies = copies

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def published_year(self):
        return self.__published_year

    @property
    def price(self):
        return self.__price

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        if value < 0:
            raise ValueError("Copies cannot be negative.")
        self.__copies = value

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.published_year}, Price: ${self.price}, Copies Available: {self.copies}")

# Member Class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}

    def borrow_book(self, book: Book):
        if book.copies > 0:
            book.copies -= 1
            due_date = datetime.now() + timedelta(days=14)  # 14-day borrow period
            self.borrowed_books[book.title] = due_date
            print(f"{self.name} borrowed '{book.title}'. Due date: {due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book: Book):
        if book.title in self.borrowed_books:
            due_date = self.borrowed_books[book.title]
            book.copies += 1
            del self.borrowed_books[book.title]

            # Calculate late fee if any
            return_date = datetime.now()
            if return_date > due_date:
                late_days = (return_date - due_date).days
                late_fee = late_days * 1  # $1 per day late fee
                print(f"{self.name} returned '{book.title}' late by {late_days} days. Late fee: ${late_fee}")
            else:
                print(f"{self.name} returned '{book.title}' on time.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for title, due_date in self.borrowed_books.items():
                print(f"  - {title}, Due Date: {due_date.strftime('%Y-%m-%d')}")
        else:
            print("No books borrowed.")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def search_book(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)

    def display_all_books(self):
        for book in self.books:
            book.display_info()

# Authentication Class
class UserAuth:
    def __init__(self):
        self.users = {  # Predefined users
            "raduan": self.hash_password("raduan123"),
            "user": self.hash_password("password")
        }
        self.last_login = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_up(self, username, password, retype_password):
        if password != retype_password:
            print("Passwords do not match. Please try again.")
            return False

        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return False
        else:
            self.users[username] = self.hash_password(password)
            print("User signed up successfully!")
            return True

    def sign_in(self, username, password):
        if username in self.users and self.users[username] == self.hash_password(password):
            print("Sign-in successful. Welcome!")
            self.last_login[username] = datetime.now()
            return True
        else:
            print("Invalid username or password.")
            return False

# Contact Us Function
def contact_us():
    print("\n** Contact Us **")
    print("---------------------")
    print("For any issues or queries, please contact:")
    contacts = [
        {"Name": "Md.Raduan Ahamed", "Designation": "Manager", "Phone": "01785566224", "Email": "raduan@1234.com"},
        {"Name": "Rawnok Jahan Riddi", "Designation": "Assistant Manager", "Phone": "01785522441", "Email": "riddi@1234.com"},
        {"Name": "Wahid Tawsif Somoy", "Designation": "Librarian", "Phone": "01785566332", "Email": "somoy@1234.com"},
        {"Name": "Sajib Hossain", "Designation": "Assistant Librarian", "Phone": "01789988554", "Email": "sajib@1234.com"},
        {"Name": "Hafijur Rahman", "Designation": "Assistant Auditor", "Phone": "01789981245", "Email": "hafizur@1234.com"},
    ]
    for contact in contacts:
        print(f"{contact['Name']} - {contact['Designation']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}\n")

def main():
    auth = UserAuth()
    library = Library()

    # Add default books and members
    library.add_book(Book("1984", "George Orwell", 1949, 9.99, 5))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, 7.99, 3))
    library.add_member(Member("raduan", "M001"))
    library.add_member(Member("ahamed", "M002"))

    logged_in = False

    while True:
        print("\n** WELCOME TO OUR LIBRARY MANAGEMENT SYSTEM **")
        print("---------------------------------------------------")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        print("---------------------------------------------------")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                retype_password = input("Retype password: ")
                auth.sign_up(username, password, retype_password)

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in = auth.sign_in(username, password)

                if logged_in:
                    last_login = auth.last_login.get(username, None)
                    if last_login:
                        print(f"\nLast login: {last_login.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    else:
                        print("\nWelcome! This is your first login.\n")
                    break

            elif choice == "3":
                print("Exiting the Library Management System. Goodbye!")
                return

            else:
                print("Invalid choice. Please try later.")

        except Exception as e:
            print(f"An error occurred: {e}")

    # Logged-in menu
    while logged_in:
        print("\n** LIBRARY MANAGEMENT MENU **")
        print("-----------------------------------")
        print("1. Add a Book")
        print("2. Add a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Search for a Book")
        print("6. Sort Books by Title")
        print("7. Display All Books")
        print("8. Contact Us")
        print("9. Log Out")
        print("-----------------------------------")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                published_year = int(input("Enter published year: "))
                price = float(input("Enter book price: "))
                copies = int(input("Enter number of copies: "))
                library.add_book(Book(title, author, published_year, price, copies))
                print("Book added successfully!")

            elif choice == "2":
                name = input("Enter member name: ")
                member_id = input("Enter member ID: ")
                library.add_member(Member(name, member_id))
                print("Member added successfully!")

            elif choice == "3":
                member_id = input("Enter member ID: ")
                title = input("Enter book title: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                if member and book:
                    member.borrow_book(book)
                else:
                    print("Invalid member ID or book title.")

            elif choice == "4":
                member_id = input("Enter member ID: ")
                title = input("Enter book title: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                if member and book:
                    member.return_book(book)
                else:
                    print("Invalid member ID or book title.")

            elif choice == "5":
                title = input("Enter book title to search: ")
                results = library.search_book(title)
                if results:
                    print("Search Results:")
                    for book in results:
                        book.display_info()
                else:
                    print("No books found with that title.")

            elif choice == "6":
                library.sort_books()
                print("Books sorted by title.")

            elif choice == "7":
                if library.books:
                    library.display_all_books()
                else:
                    print("No books available in the library.")

            elif choice == "8":
                contact_us()

            elif choice == "9":
                print("Logging out...")
                logged_in = False

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()