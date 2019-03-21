from pygame.sprite import Sprite
from pygame import Surface
from math import cos, sin


class AbstractProjectile(Sprite):
    """A class to manage projectiles fired by anyone."""

    def __init__(self, starting_position, starting_angle, damage_multiplier, speed_multiplier):
        """Create a projectile at a given position moving through a given angle"""
        super().__init__(self)

        self.image = Surface()  # Dummy

        self.rect = self.image.get_rect()
        self.rect.centerx = starting_position[0]
        self.rect.top = starting_position

        self.damage = 1 * damage_multiplier
        self.speed = 1 * speed_multiplier
        self.angle = starting_angle

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet through the screen."""

        # Update the decimal position of the bullet.
        self.x += self.speed * cos(self.angle)
        self.y += self.speed * sin(self.angle)

        # Update the rect position.
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """Draw the bullet to the screen."""

        screen.blit(self.image, self.rect)
