from settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self):
        """Initialize statistics."""
        # High score should never be reset.
        self.high_score = 0
        self.max_level = 1
