import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to manage drop item."""

    def __init__(self, screen, alien):
        """Create a drop object at the alien's current position."""
        super(Drop, self).__init__()
        self.screen = screen

        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load('images/drop.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.contery = alien.rect.centery

        # Store the drops's speed as a decimal value.
        self.y = float(self.rect.y)

        self.speed_factor = 0

    def update(self):
        """Move the drop down the screen."""
        # Update the decimal position of the drop.
        self.y += self.speed_factor
        # Update the drop speed factor.
        self.speed_factor += 0.1
        # Update the drop position.
        self.rect.y = self.y

    def draw_drop(self):
        """Draw the drop to the screen."""
        pygame.draw.rect(self.image, self.rect)5
