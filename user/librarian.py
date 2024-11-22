from user.user import User
from book.book import Book
class Librarian(User):

    def __init__(self,first_name, last_name):
        super().__init__(first_name, last_name)
    
    def add_a_book(self, title, decription, author , library):
        library.add_book(Book(title, decription, author))

    def remove_book(self, book, library):
        library.remove_book(book)
