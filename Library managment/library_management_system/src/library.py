# For adding Book :
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __repr__(self):
        return f"Book({self.isbn}, {self.title}, {self.author}, {self.year})"


class Library:
    def __init__(self):
        self.available_books = []

    def add_book(self, book):
        self.available_books.append(book)


# For borrowing books:
class Library:

    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.available_books.append(book)

    def borrow_book(self, isbn):
        for book in self.available_books:
            if book.isbn == isbn:
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                return
        raise ValueError("Book not available")


# For return book:
class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.available_books.append(book)

    def borrow_book(self, isbn):
        for book in self.available_books:
            if book.isbn == isbn:
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                return
        raise ValueError("Book not available")

    def return_book(self, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                return
        raise ValueError("Book not borrowed")


# For viewing available book:
class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.available_books.append(book)

    def borrow_book(self, isbn):
        for book in self.available_books:
            if book.isbn == isbn:
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                return
        raise ValueError("Book not available")

    def return_book(self, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                return
        raise ValueError("Book not borrowed")

    def view_available_books(self):
        return self.available_books
