from datetime import datetime

from book_models.models.author import Author

# Questions:
# should I import these and risk circular dependencies for type annotating?
# Are these 2 classes too tightly coupled? But how should they be then? It made sense for me, but I can see obvious
# flaws.
class Book:
    """Basic model for a book."""
    def __init__(self, author, title, publication_year):
        self._author = author
        self._title = title
        self._publication_year = publication_year

    def get_author(self) -> Author:
        """Return the Author which wrote the book."""
        return self._author

    def get_title(self) -> str:
        """Return the title of the book."""
        return self._title

    def get_publication_date(self) -> datetime:
        """Return the year of publication."""
        return self._publication_year

    def set_publication_date(self, value: datetime):
        """Set the year in which the book was published.

        Args:
            value: datetime - date to replace the publication year with.
        """
        self._publication_year = value
