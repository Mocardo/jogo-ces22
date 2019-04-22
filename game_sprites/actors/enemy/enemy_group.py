from pygame.sprite import Group


class EnemyGroup(Group):
    def __init__(self, screen):
        super().__init__(self)
        self.screen = screen

    def update(self):
        for enemy in self.sprites():
            enemy.update()
