from pygame.sprite import Sprite
from pygame import Surface


class GameSprite(Sprite):
    """A base class for sprites that can move."""
    image = None

    def __init__(self, screen):
        super().__init__(self)

        # Set screen reference
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set Rect
        if self.__class__.image is not None:
            self.rect = self.__class__.image.get_rect()
        else:
            self.rect = Surface().get_rect()

        # Set position and velocity
        self.position = [0.0, 0.0]  # Dummy, i just want to declare self.position in __init__
        self.velocity = [0.0, 0.0]
        self.set_position([0.0, 0.0])

    def update(self):
        new_position = self.position + self.velocity
        self.set_position(new_position)

    def set_position(self, new_position):
        self.position = [float(i) for i in new_position]
        self.rect.center = [int(i) for i in new_position]

    def is_on_screen(self):
        return self.rect.colliderect(self.screen_rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
