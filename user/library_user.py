from user.user import User

class LibraryUser(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.borrowed_books = []
    
    def search_for_book(self, library, book_title):
        return library.search_for_book(book_title)

    def borrow_book(self, book):
        book.borrow(self.id)
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book(book)
        self.borrowed_books.remove(book)
