"""Player model for the game."""


class Player:
    """Represents the current player and their location."""

    def __init__(self, room):
        """Create a player starting in the given room."""
        self.room = room
        