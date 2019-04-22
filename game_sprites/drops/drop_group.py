from game_sprites.game_sprite_group import GameSpriteGroup


class DropGroup(GameSpriteGroup):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        for drop in self.sprites():
            drop.update()
            if not drop.is_on_screen():
                self.remove(drop)
