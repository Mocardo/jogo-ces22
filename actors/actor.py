from pygame import Surface
from pygame.sprite import Sprite


class Actor(Sprite):
    image = Surface()

    def __init__(self, screen, projectile_group):
        super(Actor, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load the ship image and get its rect.
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.position = [float(self.rect.center[0]), float(self.rect.center[1])]
        self.speed = [0, 0]
        self.hp = 100

        self.projectile_group = projectile_group
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
