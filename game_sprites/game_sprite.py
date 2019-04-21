from pygame.sprite import Sprite
from pygame import Surface


class GameSprite(Sprite):
    """A base class for game sprites"""
    image = None

    def __init__(self, screen, starting_position=None):
        super().__init__(self)

        self.screen = screen
        self.screen_rect = screen.get_rect()

        if starting_position is not None:
            self.position = [float(i) for i in starting_position]
        else:
            self.position = [0.0, 0.0]

        if self.__class__.image is not None:
            self.rect = self.__class__.image.get_rect()
            self.rect.center = [int(i) for i in self.position]

        self.velocity = [0.0, 0.0]

    def update(self):
        self.position += self.velocity
        self.rect.center = [int(i) for i in self.position]

        if not self.is_on_screen():
            self.kill()

    def is_on_screen(self):
        return self.rect.colliderect(self.screen_rect)
