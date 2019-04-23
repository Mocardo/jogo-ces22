
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
    player_base_speed = 3

    # Projectile settings
    bullet_base_damage = 10
    player_bullet_base_speed = 5
    enemy_bullet_base_speed = 1.5
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
    alien_weapon_cooldown = 3000

    # Drop settings
    drop_acceleration = 0.02
    drop_points = 500
    drop_hp = 10

    # Scoring
    points_per_alien = 100

    # Graphics settings
    explosion_duration = 500

    # Game settings
    next_level_delay = 3000

    def __init__(self):
        pass
