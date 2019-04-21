from game_sprites.projectiles.abstract_projectile import AbstractProjectile


class Laser(AbstractProjectile):
    """A class to represent LAZ0RS!!!1!!1 fired by anyone."""
    image = None  # TODO
    base_speed = 1
    base_damage = 1

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction):
        """Create a bullet at a given position moving through a given angle"""
        super().__init__(screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction)
