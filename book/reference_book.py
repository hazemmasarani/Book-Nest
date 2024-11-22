from book.book import Book

class ReferenceBook(Book):
    
    def __init__(self, title, decription, author):
        super().__init__(title, decription, author)