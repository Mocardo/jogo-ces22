from settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self):
        """Initialize statistics."""
        self.reset_stats()

        # Start Alien Invasion in stopped state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

        self.ships_left = Settings.ship_limit
        self.score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = Settings.ship_limit
        self.score = 0
        self.level = 1
