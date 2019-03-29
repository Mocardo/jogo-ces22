import pygame
from actors.actor import Actor
from actors.actor import Faction


class Player(Actor):
    faction = Faction.ALLIED

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        super(Player, self).__init__(screen)

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
