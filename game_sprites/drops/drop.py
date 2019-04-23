import pygame
from game_sprites.game_sprite import GameSprite
from settings import Settings


class Drop(GameSprite):
    """A class to manage drop item."""
    image = pygame.image.load('images/drop.png')

    def __init__(self, screen, position):
        """Create a drop object at the alien's current position."""
        super().__init__(screen)

        # Load the drop image and set its rect attribute.
        self.set_position(position)
        self.points = Settings.drop_points
        self.hp = Settings.drop_hp

    def update(self):
        """Move the drop down the screen."""
        # Update the decimal position of the drop.
        self.velocity[1] += Settings.drop_acceleration
        # Update the drop position.
        super().update()

    def blitme(self):
        """Draw the drop to the screen."""
        self.screen.blit(self.image, self.rect)
