
from enum import Enum


class GameState(Enum):
    game_inactive = 0
    game_active = 1
    game_level_passed = 2


class Settings:
    """A class to store all settings for Alien Invasion."""
    # Screen settings
    screen_width = 512
    screen_height = 768

    # Player settings
    player_max_hp = 100
    player_base_speed = 5

    # Projectile settings
    bullet_base_damage = 10
    bullet_base_speed = 5
    laser_base_speed = 1
    laser_base_damage = 1
    """
    bullet_width = 3
    bullet_height = 15
    bullet_color = 60, 60, 60
    bullets_allowed = 6
    """

    # Alien settings
    fleet_drop_speed = 10

    alien_max_hp = 20
    alien_base_speed = 2

    # Drop settings
    drop_acceleration = 0.04
    """
    # Scoring
    alien_points = 50
    # How quickly the alien point values increase
    score_scale = 1.5
    """

    next_level_delay = 3000

    def __init__(self):
        pass
