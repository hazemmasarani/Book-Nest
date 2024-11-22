
class Book:

    __book_cntr = 0

    def __init__(self, title, decription, author):
        Book.__book_cntr += 1
        self.id = Book.__book_cntr
        self.title = title
        self.decription = decription
        self.author = author
        self.status = "Active"
        self.borrower = None
    
    def set_status(self, status):
        self.status = status
    
    def __eq__(self,other):
        if self.id == other.id:
            return True
        return False

    def borrow(self, user_id):
        self.borrower = user_id
        self.status = "borrowed"

    def return_book(self):
        self.borrower = None
        self.status = "Active"