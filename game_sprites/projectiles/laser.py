import pygame
from game_sprites.projectiles.abstract_projectile import AbstractProjectile


class Laser(AbstractProjectile):
    """A class to represent LAZ0RS!!!1!!1 fired by anyone."""
    image = pygame.image.load('images/lazer.png')
    base_speed = Settings.laser_base_speed
    base_damage = Settings.laser_base_damage

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction):
        """Create a bullet at a given position moving through a given angle"""
        super().__init__(screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction)
