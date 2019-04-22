from game_sprites.actors.actor import Actor
from game_sprites.actors.actor import Faction


class AbstractEnemy(Actor):
    faction = Faction.Enemy

    def __init__(self, screen, level):
        """Initialize the enemy and set its starting position."""
        super().__init__(screen)

        self.starting_position = (screen.screen_rect.left + self.__class__.image.get_rect().width//2,
                                  screen.screen_rect.top + self.__class__.image.get_rect().height//2)
        self.set_position(self.starting_position)

        self.level = level
