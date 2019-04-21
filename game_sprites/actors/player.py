import pygame
from game_sprites.actors.actor import Actor
from weapons.pistol import Pistol


class Player(Actor):
    image = pygame.image.load('images/ship.png')
    faction = 1

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        super().__init__(screen)

        # Start each new ship at the bottom center of the screen.
        self.starting_position = (screen.screen_rect.centerx,
                                  screen.screen_rect.bottom - self.__class__.image.get_rect().centery)
        self.set_position(self.starting_position)

        self.weapon = Pistol(self.screen, self.__class__.faction)
