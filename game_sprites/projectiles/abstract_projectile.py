from game_sprites.game_sprite import GameSprite
import math


class AbstractProjectile(GameSprite):
    """A class to manage projectiles fired by anyone."""
    image = None
    baseSpeed = 1
    baseDamage = 1

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier):
        """Create a projectile at a given position moving through a given angle"""
        super().__init__(screen)

        self.set_position(starting_position)
        self.angle = starting_angle
        self.speed = self.__class__.baseSpeed * speed_multiplier
        self.damage = self.__class__.baseDamage * damage_multiplier

    def update(self):
        """Move the bullet through the screen."""
        self.velocity = self.speed * [math.cos(self.angle), math.sin(self.angle)]

        # Update the decimal position of the bullet.
        self.position += self.velocity

        # Update the rect position.
        self.rect.center = int(self.position[0]), int(self.position[1])
