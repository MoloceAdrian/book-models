from datetime import datetime

from book_models.models.author import Author
from book_models.models.book import Book


def test_book():
    author = Author("Daniel Keyes", datetime(year=1927, month=8, day=9))
    book = Book(author, "Flowers for Algernon", datetime(year=1959, month=4, day=0))

    assert book.get_author().get_name() == 'Daniel Keyes'
    assert book.get_publication_date().year == 1927
    assert book.get_title() == "Flowers for Algernon"

    book.set_publication_date(datetime.now())
    assert book.get_publication_date().year == 2019


def test_author():
    author = Author("Daniel Keyesee", datetime(year=1927, month=8, day=9))
    book = Book(author, "Flowers for Algernon", datetime(year=1959, month=4, day=0))

    assert author.get_name() == "Daniel Keyesee"
    assert author.get_date_of_birth().year == 1927

    author.set_name("Daniel Keyes")
    assert author.get_name() == "Daniel Keyes"

    author.set_date_of_birth(datetime.now())
    assert author.get_date_of_birth().year == 2019

    assert len(author.get_books()) == 0
    author.add_book(book)
    assert len(author.get_books()) == 1
