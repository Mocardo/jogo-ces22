from pygame.sprite import Group


class EnemyGroup(Group):
    def __init__(self, screen, projectile_group):
        super().__init__(self)
        self.screen = screen
        self.projectile_group = projectile_group

    def update(self):
        pass  # TODO
