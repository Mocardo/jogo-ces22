from game_sprites.game_sprite_group import GameSpriteGroup


class EnemyGroup(GameSpriteGroup):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        for enemy in self.sprites():
            enemy.update()
