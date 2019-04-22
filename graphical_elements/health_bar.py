import pygame.draw_py
from pygame import Rect


class HealthBar:
    def __init__(self, hp, actor_position):
        self.hp = hp
        self.actor_position = actor_position

        self.base_rect = Rect(*actor_position, 20, 4)

    def update_base_rect(self):
        self.base_rect.center = (self.actor_position + (0, 5))

    def blitme(self):
        pass  # TODO
