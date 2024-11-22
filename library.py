
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.__users = []
        self.__books = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        self.__users.remove(user)

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def search_for_book(self, book_title):
        res = []
        for b in self.__books:
            if book_title in b.title:
                res.append(b)
        return res

