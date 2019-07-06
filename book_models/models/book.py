"""This module encapsulates models regarding the a book object."""
from datetime import datetime
from typing import Optional
from uuid import uuid4


class Book:
    """Basic model for a book."""
    def __init__(
            self,
            author: str,
            title: str,
            genre: Optional[str] = None,
            publisher: Optional[str] = None,
            publication_date: Optional[datetime] = None
    ):
        """Initializer.

        Args:
            author: User - the author of the book
            title: str - title of the book
            genre: str - the genre of the book
            publisher: str - The name of the publishing unit
            publication_date: datetime - the date when the book was published
        """
        self._book_id = uuid4()
        self.author = author
        self.title = title
        self.genre = genre
        self.publisher = publisher
        self.publication_date = publication_date
