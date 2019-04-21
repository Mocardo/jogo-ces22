from pygame import Surface
from game_sprites.game_sprite import GameSprite


class Actor(GameSprite):
    """A base class for the player and enemy"""

    def __init__(self, screen, starting_position=None):
        super().__init__(screen, starting_position)

        self.rect = self.__class__.image.get_rect()

        # Load the ship image and get its rect.
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.position = [float(i) for i in self.rect.center]
        self.speed = [0, 0]
        self.hp = 100

        self.weapon = None

    def update(self):
        self.position += self.speed
        self.rect.center = int(self.position[0]), int(self.position[1])

        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def fire_weapon(self):
        self.weapon.fire(self.rect.center, 0)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
