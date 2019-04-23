import pygame
from pygame.sprite import Sprite
from pygame import Rect


class HealthBar(Sprite):

    def __init__(self, screen, actor):
        """Create an object HealthBar"""
        super(HealthBar, self).__init__()
        self.screen = screen
        self.actor = actor

        self.width = 100
        self.height = 4
        self.vertical_spacing = 5

        # Create a rectangle for health bar in (0, 0) and set its position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = actor.rect.centerx
        self.rect.top = actor.rect.top + self.vertical_spacing

        # set value of hp and its color
        self.hp = actor.hp
        self.red = 255, 0, 0
        self.green = 0, 255, 0

    def update(self):
        self.rect.centerx = self.actor.rect.centerx
        self.rect.top = self.actor.rect.top + 5
        self.hp = self.actor.hp

    def draw_health_bar(self):
        width_green = int((self.actor.hp/self.actor.maxhp) * self.rect.width)
        width_red = int(self.width - width_green)

        rect_green = Rect(self.rect.left, self.actor.rect.top + self.vertical_spacing,
                          width_green, self.height)
        pygame.draw.rect(self.screen, self.green, rect_green)

        if width_red > 0:
            rect_red = Rect(self.rect.left + width_green, self.actor.rect.top + self.vertical_spacing,
                            width_red, self.height)
            pygame.draw.rect(self.screen, self.red, rect_red)
