import pygame
from game_sprites.projectiles.abstract_projectile import AbstractProjectile


class Bullet(AbstractProjectile):
    """A class to manage bullets fired by anyone."""
    image = pygame.image.load('images/bullet.png')
    base_speed = 8
    base_damage = 3

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction):
        """Create a bullet at a given position moving through a given angle"""
        super().__init__(screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction)

    """ 
    def __init__(self, ai_settings, screen, ship):
        # Create a bullet object at the ship's current position.
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def draw_bullet(self):
        " Draw the bullet to the screen. "
        pygame.draw.rect(self.screen, self.color, self.rect)
    """
