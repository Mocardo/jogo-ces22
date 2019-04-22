from pygame.sprite import Group


class GameSpriteGroup(Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def blitme(self):
        for sprite in self.sprites():
            sprite.blitme()
