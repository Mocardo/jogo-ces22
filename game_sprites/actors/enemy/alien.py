import pygame
from game_sprites.actors.enemy.abstract_enemy import AbstractEnemy
from weapons.pistol import Pistol


class Alien(AbstractEnemy):
    """A class to represent an alien enemy."""
    image = pygame.image.load('images/alien.png')

    def __init__(self, screen, level):
        """Initialize the alien and set its starting position."""
        super().__init__(screen, level)

        self.weapon = Pistol(self.screen, self.__class__.faction)
