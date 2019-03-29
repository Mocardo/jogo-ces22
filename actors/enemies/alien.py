import pygame
from actors.enemies.enemy import Enemy


class Alien(Enemy):
    """A class to represent a single alien in the fleet."""

    def __init__(self, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__(screen)

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
