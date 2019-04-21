import math
from game_sprites.game_sprite import GameSprite


class AbstractProjectile(GameSprite):
    """A class to manage projectiles fired by anyone."""
    image = None
    base_speed = 1
    base_damage = 1

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction):
        """Create a projectile at a given position moving through a given angle"""
        super().__init__(screen)

        self.faction = faction
        self.set_position(starting_position)
        self.angle = starting_angle
        self.speed = self.__class__.base_speed * speed_multiplier
        self.damage = self.__class__.base_damage * damage_multiplier

    def update(self):
        """Move the bullet through the screen."""
        self.velocity = self.speed * [math.cos(self.angle), math.sin(self.angle)]
        super().update()
