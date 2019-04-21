import pygame
from game_sprites.actors.enemies.abstract_enemy import Enemy
from weapons.pistol import Pistol


class Alien(Enemy):
    """A class to represent a single alien in the fleet."""
    image = pygame.image.load('images/alien.png')

    def __init__(self, screen, projectile_group):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__(screen, projectile_group)

        # Load the alien image and set its rect attribute.
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

        self.weapon = Pistol(self.screen, self.projectile_group)
