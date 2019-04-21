from pygame.sprite import Group


class ProjectileGroup(Group):
    def __init__(self, screen):
        super().__init__(self)
        self.screen = screen

    def update(self):
        for projectile in self.sprites():
            projectile.update()
            if not projectile.is_on_screen(self.screen):
                self.remove(projectile)
