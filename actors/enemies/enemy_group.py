from pygame.sprite import Group


class EnemyGroup(Group):
    def __init__(self, screen):
        super().__init__(self)
        self.screen = screen

