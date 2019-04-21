from pygame.sprite import Sprite
from pygame import Surface
from math import cos, sin


class AbstractProjectile(Sprite):
    """A class to manage projectiles fired by anyone."""

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier):
        """Create a projectile at a given position moving through a given angle"""
        super().__init__(self)

        self.screen = screen
        self.image = Surface()  # Dummy

        self.rect = self.image.get_rect()
        self.rect.centerx = starting_position[0]
        self.rect.top = starting_position

        self.angle = starting_angle
        self.speed = 1 * speed_multiplier
        self.damage = 1 * damage_multiplier

        self.position = [float(self.rect.x), float(self.rect.y)]

    def update(self):
        """Move the bullet through the screen."""

        # Update the decimal position of the bullet.
        self.position += self.speed * cos(self.angle), self.speed * sin(self.angle)

        # Update the rect position.
        self.rect.center = int(self.position[0]), int(self.position[1])

    def is_on_screen(self, screen):
        return self.rect.colliderect(screen.get_rect())

    def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        bullets.update()
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    def draw(self, screen):
        """Draw the bullet to the screen."""

        screen.blit(self.image, self.rect)
