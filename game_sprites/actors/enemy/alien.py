import pygame
from game_sprites.actors.enemy.abstract_enemy import AbstractEnemy
from weapons.pistol import Pistol
from settings import Settings


class Alien(AbstractEnemy):
    """A class to represent an alien enemy."""
    image = pygame.image.load('images/alien.png')

    def __init__(self, screen, level):
        """Initialize the alien and set its starting position."""
        super().__init__(screen, level)

        self.maxhp = Settings.alien_max_hp
        self.hp = self.maxhp
        self.speed = Settings.alien_base_speed

        self.weapon = Pistol(self.screen, self.__class__.faction)
