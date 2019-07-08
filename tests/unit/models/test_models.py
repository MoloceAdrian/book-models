from datetime import datetime

from book_models.models.book import Book
from book_models.models.user import User


def test_book():
    book = Book(
        ["Daniel Keyes"],
        "Flowers for Algernon",
        genre="Drama",
        publication_date=datetime(year=1959, month=4, day=1)
    )

    assert book.list_of_authors == ['Daniel Keyes']
    assert book.publication_date.year == 1959
    assert book.title == "Flowers for Algernon"

    book.publication_date = datetime.now()
    assert book.publication_date.year == 2019


def test_user():
    user = User("Adrian", "TheBoss", "secret")

    assert user.name == "Adrian"
    user.name = "Adrian M."
    assert user.name == "Adrian M."

    assert user.password == "secret"
    user.password = "amuitatparola"
    assert user.password == "amuitatparola"
