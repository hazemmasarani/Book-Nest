from user.user import User
from user.librarian import Librarian
from user.library_user import LibraryUser

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def add_librarian(self, first_name, last_name, library):
        library.add_user(Librarian(first_name, last_name))

    def remove_librarian(self, library, librarian):
        library.remove_user(librarian)

    def add_library_user(self, library, first_name, last_name):
        library.add_user(LibraryUser(first_name, last_name))

    def remove_library_user(self, library, library_user):
        library.remove(library_user)

