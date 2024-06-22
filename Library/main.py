from book import Book
from patron import Patron
from librarian import Librarian
from library import Library

library = Library("University Of Warsaw Library")

book1 = Book("Don Kihote", "Miguel de Cervantes", "0000000001")
book2 = Book("Nutuk", "Mustafa Kemal Ataturk", "00000000002")

librarian = Librarian("Kenan Sahin", "L1")

patron1 = Patron("Mehmet Sahin", "P1")
patron2 = Patron("Akif Sahin", "P2")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

patron1.borrow_book(book1)
book1.available = False

print(" Books in the library:")
print(library.list_books())
 
print("\n Patrons in the library:")
print(library.list_patrons())

patron1.return_book(book1)
book1.available = True

print("\n Books in the library after returning a book:")
print(library.list_books())

