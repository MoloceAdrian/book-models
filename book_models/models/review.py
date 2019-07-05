"""This module encapsulates the Review class."""
from uuid import uuid4

from book_models.models.book import Book
from book_models.models.user import User


class Review:
    """A review made by an user for a book."""

    def __init__(self, text: str, book: Book, critic: User):
        """Initializer.

        Args:
            text: str - The actual review
            book: Book - refers to the book being reviewed
            critic: User - refers to the person making the review
        """
        self._review_id = uuid4()
        self.text = text
        self.book = book
        self.critic = critic

    def add_review_for_book(self, text: str, book_id: uuid4, critic_id: uuid4):
        """Make a review for a book.

        Args:
            text: str - the review text
            book_id: uuid4 - the book the review was made for
            critic_id: uuid - the id of the critic

        Returns:
            Review: a new Review made by the user.
        """
        # We'll come back to this soon as it's static and may live elsewhere.
        return Review(
            text,
            book_id,
            critic_id
        )
