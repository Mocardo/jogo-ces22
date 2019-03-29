from enum import Enum
from pygame import Surface
from pygame.sprite import Sprite


class Faction(Enum):
    NONE = 0
    ALLIED = 1
    ENEMY = 2


class Actor(Sprite):
    faction = Faction.NONE

    def __init__(self, screen):
        super(Actor, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load the ship image and get its rect.
        self.image = Surface()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

        self.hp = 100
        self.speed = [0, 0]

    def update(self):
        self.float_center += self.speed
        self.rect.center[0] = int(self.float_center[0])
        self.rect.center[1] = int(self.float_center[1])

        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
