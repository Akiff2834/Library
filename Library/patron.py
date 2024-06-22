from person import Person

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name, patron_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        return super().__str__() + f", Borrowed Books: {[book.title for book in self.borrowed_books]}"

