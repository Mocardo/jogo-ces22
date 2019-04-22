from game_sprites.game_sprite_group import GameSpriteGroup


class ProjectileGroup(GameSpriteGroup):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        for projectile in self.sprites():
            projectile.update()
            if not projectile.is_on_screen():
                self.remove(projectile)
