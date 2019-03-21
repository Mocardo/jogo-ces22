class Settings():
    """A class to store all settings for Alien Invasion."""
    screen_width = 512
    screen_height = 768
    bg_color = (150, 150, 250)

    # Ship settings
    ship_limit = 3

    # Bullet settings
    bullet_width = 3
    bullet_height = 15
    bullet_color = 60, 60, 60
    bullets_allowed = 6

    # Alien settings
    fleet_drop_speed = 10

    # Scoring
    alien_points = 50

    # How quickly the game speeds up
    speedup_scale = 1.1

    # How quickly the alien point values increase
    score_scale = 1.5

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings




    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

