"""Core model for the users of the application."""
from uuid import uuid4


class User:
    """Main class to interact with the application.
    Main methods:
        - review
    """
    def __init__(self, name, username, password):
        """Initializer.

        Args:
            name: str - name of the user
            username: str - a custom unique username
            password: str - password set by user
        """
        self._user_id = uuid4()
        self.name = name
        self.username = username
        self.__password = password

    @property
    def password(self):
        """Return the password, naively unencrypted."""
        return self.__password

    @password.setter
    def password(self, value):
        """Set the new password to the given value.

        Args:
            value: str - new password.
        """
        self.__password = value
