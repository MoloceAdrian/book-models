"""Module contains class to work with user files."""
from book_models.stores.file_store import FileStore


class UserFileStore(FileStore):
    """User File Store works with files regarding users."""

    def insert(self, data):
        """Insert a new row of user date in the users file.

        Args:
            data: str - data from a user to be inserted
        """
        with open(self.file_name, 'a+') as fp:
            fp.write(data + '\n')

    def update(self, data_to_update, data_to_update_with):
        """Update a row of the users file with new information.

        Args:
            data_to_update: str - exact text to be updated
            data_to_update_with: str - the new information to be replaced with
        """
        with open(self.file_name, 'r+') as fp:
            content = fp.read()
            content = content.replace(data_to_update, data_to_update_with)
            fp.seek(0)
            fp.truncate()
            fp.write(content)

    def delete(self, data):
        """Delete a user's information from the users file.

        Args:
            data: str - user data to be deleted from the file.
        """
        with open(self.file_name, "r") as fp:
            lines = fp.readlines()
        with open(self.file_name, "w") as fp:
            for line in lines:
                if line.strip("\n") != data:
                    fp.write(line)

    def read(self):
        """Read all the user information from the users file.

        Returns:
            str: content - all the user data from the file
        """
        with open(self.file_name, 'r') as fp:
            content = fp.read()
            return content
