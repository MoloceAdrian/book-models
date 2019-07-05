"""This module encapsulates models regarding the a book object."""
from datetime import datetime
from uuid import uuid4

from book_models.models.user import User


class Book:
    """Basic model for a book."""
    def __init__(self, author: User, title: str, genre: str, publication_date: datetime):
        """Initializer.

        Args:
            author: User - the author of the book
            title: str - title of the book
            genre: str - the genre of the book
            publication_date: datetime - the date when the book was published
        """
        self._book_id = uuid4()
        self.author = author
        self.title = title
        self.genre = genre
        self.publication_date = publication_date
