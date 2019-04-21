import pygame
from game_sprites.actors.actor import Actor
from weapons.pistol import Pistol


class Player(Actor):
    image = pygame.image.load('images/ship.png')

    def __init__(self, screen, projectile_group):
        """Initialize the ship and set its starting position."""
        super(Player, self).__init__(screen, projectile_group)

        # Load the ship image and get its rect.
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

        self.weapon = Pistol(self.screen, self.projectile_group)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
