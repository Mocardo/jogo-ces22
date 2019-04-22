import pygame
from pygame.sprite import Sprite


class HealthBar(Sprite):

    def __init__(self, screen, actor):
        """Create an object HealthBar"""
        super(HealthBar, self).__init__()
        self.screen = screen

        # Create a rectangle for health bar in (0, 0) and set its position
        self.rect = pygame.Rect(0, 0, 20, 4)
        self.rect.centerx = actor.rect.centerx
        self.rect.top = actor.rect.top + 5

        # set value of hp and its color
        self.hp = actor.hp
        #self.red = 255, 0, 0
        self.color = 0, 255, 0

    def update(self, actor):
        self.rect.centerx = actor.rect.centerx
        self.rect.top = actor.rect.top + 5
        self.hp = actor.hp

    def draw_health_bar(self, actor):
        rect = self.rect
        rect.width = actor.hp * 20
        rect.left = self.rect.left
        pygame.draw.rect(self.screen, self.color, rect)
