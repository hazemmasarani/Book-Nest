import sys
from user.user import User
from user.librarian import Librarian
from user.library_user import LibraryUser
from user.admin import Admin
from book.book import Book
from library import Library

def print_menu():
    print("\nLibrary Management System")
    print("1. Admin Login")
    print("2. Librarian Login")
    print("3. Library User Login")
    print("4. Exit")

def admin_menu(admin, library):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Librarian")
        print("2. Remove Librarian")
        print("3. Add Library User")
        print("4. Remove Library User")
        print("5. View All Users")
        print("6. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            admin.add_librarian(first_name, last_name, library)
            print(f"Librarian {first_name} {last_name} added.")
        elif choice == '2':
            first_name = input("Enter first name of librarian to remove: ")
            last_name = input("Enter last name: ")
            librarian = Librarian(first_name, last_name)
            admin.remove_librarian(library, librarian)
            print(f"Librarian {first_name} {last_name} removed.")
        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            admin.add_library_user(library, first_name, last_name)
            print(f"Library User {first_name} {last_name} added.")
        elif choice == '4':
            first_name = input("Enter first name of user to remove: ")
            last_name = input("Enter last name: ")
            library_user = LibraryUser(first_name, last_name)
            admin.remove_library_user(library, library_user)
            print(f"Library User {first_name} {last_name} removed.")
        elif choice == '5':
            print("Users in library:")
            for user in library._Library__users:
                print(f"{user.first_name} {user.last_name}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def librarian_menu(librarian, library):
    while True:
        print("\nLibrarian Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            description = input("Enter book description: ")
            author = input("Enter book author: ")
            librarian.add_a_book(title, description, author, library)
            print(f"Book '{title}' added.")
        elif choice == '2':
            title = input("Enter book title to remove: ")
            book = next((b for b in library._Library__books if b.title == title), None)
            if book:
                librarian.remove_book(book, library)
                print(f"Book '{title}' removed.")
            else:
                print("Book not found.")
        elif choice == '3':
            print("Books in library:")
            for book in library._Library__books:
                print(f"Title: {book.title}, Status: {book.status}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def library_user_menu(library_user, library):
    while True:
        print("\nLibrary User Menu:")
        print("1. Search for Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Borrowed Books")
        print("5. Search for Book")
        print("6. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            book_title = input("Enter book title to search: ")
            books = library_user.search_for_book(library, book_title)
            if books:
                print("Found books:")
                for book in books:
                    print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")
            else:
                print("No books found.")
        elif choice == '2':
            book_title = input("Enter book title to borrow: ")
            book = next((b for b in library._Library__books if b.title == book_title and b.status == "Active"), None)
            if book:
                library_user.borrow_book(book)
                print(f"Book '{book_title}' borrowed.")
            else:
                print("Book not available for borrowing.")
        elif choice == '3':
            book_title = input("Enter book title to return: ")
            book = next((b for b in library_user.borrowed_books if b.title == book_title), None)
            if book:
                library_user.return_book(book)
                print(f"Book '{book_title}' returned.")
            else:
                print("You haven't borrowed this book.")
        elif choice == '4':
            print("Borrowed Books:")
            for book in library_user.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}")
        elif choice == '5':
            book_title = input("Enter book title to search: ")
            print("Books Found:")
            for book in library_user.search_for_book(library ,book_title):
                print(f"Title: {book.title}, Author: {book.author}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    library_name = input("Enter library name: ")
    library = Library(library_name)

    admin = Admin("Admin", "Admin")

    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            admin_menu(admin, library)
        elif choice == '2':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            librarian = Librarian(first_name, last_name)
            librarian_menu(librarian, library)
        elif choice == '3':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            library_user = LibraryUser(first_name, last_name)
            library_user_menu(library_user, library)
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
