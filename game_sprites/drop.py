import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """A class to manage drop item."""
    image = pygame.image.load('images/drop.png')

    def __init__(self, screen, position):
        """Create a drop object at the alien's current position."""
        super().__init__()
        self.screen = screen

        # Load the drop image and set its rect attribute.
        self.rect = self.__class__.image.get_rect()
        self.rect.center = [int(i) for i in position]

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
        self.rect.y = int(self.y)
        if self.rect.top > self.screen.bottom:
            self.kill()

    def blitme(self):
        """Draw the drop to the screen."""
        self.screen.blit(self.image, self.rect)
