from pygame import Surface
from weapons.projectiles.abstract_projectile import AbstractProjectile


class Laser(AbstractProjectile):
    """A class to represent LAZ0RS!!!1!!1 fired by anyone."""

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier):
        """Create a bullet at a given position moving through a given angle"""
        super().__init__(screen, starting_position, starting_angle, damage_multiplier, speed_multiplier)

        self.image = Surface()  # Dummy
