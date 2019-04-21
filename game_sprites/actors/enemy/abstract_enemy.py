from game_sprites.actors.actor import Actor


class AbstractEnemy(Actor):
    faction = 2

    def __init__(self, screen):
        """Initialize the enemy and set its starting position."""
        super().__init__(screen)

        self.starting_position = (screen.screen_rect.left + self.__class__.image.get_rect().centerx,
                                  screen.screen_rect.top + self.__class__.image.get_rect().centery)
        self.set_position(self.starting_position)
