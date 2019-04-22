import pygame
from pygame.sprite import Sprite


class HealthBar(Sprite):

    def __init__(self, screen, actor):
        """Create an object HealthBar"""
        super(HealthBar, self).__init__()
        self.screen = screen
        self.actor = actor

        # Create a rectangle for health bar in (0, 0) and set its position
        self.rect = pygame.Rect(0, 0, 100, 4)
        self.rect.centerx = actor.rect.centerx
        self.rect.top = actor.rect.top + 5

        # set value of hp and its color
        self.hp = actor.hp
        #self.red = 255, 0, 0
        self.color = 0, 255, 0

    def update(self):
        self.rect.centerx = self.actor.rect.centerx
        self.rect.top = self.actor.rect.top + 5
        self.hp = self.actor.hp

    def draw_health_bar(self):
        rect = self.rect.copy()
        print(self.actor.rect.width)
        rect.width = self.actor.hp * self.rect.width / self.actor.maxhp
        rect.left = self.rect.left
        pygame.draw.rect(self.screen, self.color, rect)
