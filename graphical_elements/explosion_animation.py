import pygame
from pygame.sprite import Sprite
from pygame import Rect
from settings import Settings
from pygame.time import Clock


class ExplosionAnimation(Sprite):
    image = pygame.image.load("images/explosion.png")

    def __init__(self, screen, position):
        super().__init__()
        self.screen = screen
        self.position = position
        self.full_rect = self.__class__.image.get_rect()
        self.width = self.full_rect.width/3
        self.height = self.full_rect.height/3
        self.rect = Rect(0, 0, self.width, self.height)
        self.rect.center = self.position
        self.frame_index = 0
        self.clock = Clock()
        self.time = 0

    def update(self):
        self.time += self.clock.tick()
        if self.time > Settings.explosion_duration/9:
            self.frame_index += 1
            self.time = 0

    def draw(self):
        subrect = self.rect.copy()
        subrect.left = self.full_rect.left + (self.frame_index % 3) * self.width
        subrect.top = self.full_rect.top + (self.frame_index // 3) * self.height
        self.screen.blit(self.__class__.image, self.rect, subrect)
