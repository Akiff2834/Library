class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        self.patrons.remove(patron)

    def list_books(self):
        return [str(book) for book in self.books]

    def list_patrons(self):
        return [str(patron) for patron in self.patrons]

