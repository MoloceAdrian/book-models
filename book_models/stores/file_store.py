"""This module helps developers define the contract with the File Store"""


class FileStore:
    """Abstract class for a file store."""

    def __init__(self, file_name):
        """Initializer.

        Args:
            file_name: str - name of the file to work with
        """
        self.file_name = file_name

    def insert(self, data):
        """Insert new data into the file."""
        raise NotImplementedError

    def update(self, data_to_update, data_to_update_with):
        """Find and update data."""
        raise NotImplementedError

    def delete(self, data):
        """Delete given data."""
        raise NotImplementedError

    def read(self):
        """Read the data."""
        raise NotImplementedError
