"""The publisher can publish new books."""


class Publisher:
    """Help authors publish new books."""

    def __init__(self, name: str, location: str):
        """Initializer.

        Args:
            name: str - name of the publisher
            location: str - main location of the publishing office.
        """
        self.name = name
        self.location = location
