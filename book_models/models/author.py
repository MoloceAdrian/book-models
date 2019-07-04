import datetime
from typing import List

from book_models.models.book import Book


class Author:
    """Basic model for an Author."""
    def __init__(self, name: str, date_of_birth: datetime, books=None):
        self._name = name
        self._date_of_birth = date_of_birth
        if books:
            self._books = books
        else:
            self._books = []

    def get_name(self) -> str:
        """Return the name of the author."""
        return self._name

    def set_name(self, value: str):
        """Set the name of the author.

        Args:
            value: str - value to replace the name with.
        """
        self._name = value

    def get_date_of_birth(self):
        """Return the birth date of the author."""
        return self._date_of_birth

    def set_date_of_birth(self, value: datetime):
        """Set the birth date of the author."""
        self._date_of_birth = value

    def get_books(self) -> List[Book]:
        """Return a list of books written by the author."""
        return self._books

    def add_book(self, book: Book):
        """Add a book to the list of written books.

        Args:
            book: Book - book written by author.
        """
        self._books.append(book)
