import pygame.draw_py
from pygame import Rect


class HealthBar:
    def __init__(self, actor):
        self.hp = actor.hp
        self.actor_position = actor.actor_position
        
        self.base_rect = Rect()
        self.base_rect.size = (20, 4)

    def update_base_rect(self):

        self.base_rect.center = (self.actor_position + (0, 5))


    def draw_health_bar(self):

        pass  # TODO:
