import pytest
from src.library import Library, Book

#  Test For adding books:
def test_add_book():
    library = Library()
    book = Book(isbn="12345", title="Test Book", author="Author A", year=2021)
    library.add_book(book)
    assert len(library.available_books) == 1
    assert library.available_books[0] == book


# For borrowing Books:
def test_borrow_book():
    library = Library()
    book = Book(isbn="12345", title="Test Book", author="Author A", year=2021)
    library.add_book(book)
    library.borrow_book(book.isbn)
    assert len(library.available_books) == 0


# Test for returning books
def test_return_book():
    library = Library()
    book = Book(isbn="12345", title="Test Book", author="Author A", year=2021)
    library.add_book(book)
    library.borrow_book(book.isbn)
    library.return_book(book.isbn)
    assert len(library.available_books) == 1
    assert len(library.borrowed_books) == 0


# Test for viewing available book:
def test_view_available_books():
    library = Library()
    book = Book(isbn="12345", title="Test Book", author="Author A", year=2021)
    library.add_book(book)
    available_books = library.view_available_books()
    assert len(available_books) == 1
    assert available_books[0] == book
