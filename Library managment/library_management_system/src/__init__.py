from library import Library, Book

# Create a library instance
library = Library()

# Add a book
book = Book(isbn="12345", title="Test Book", author="Author A", year=2021)
library.add_book(book)

# Borrow a book
library.borrow_book("12345")

# Return a book
library.return_book("12345")

# View available books
available_books = library.view_available_books()
print(available_books)
