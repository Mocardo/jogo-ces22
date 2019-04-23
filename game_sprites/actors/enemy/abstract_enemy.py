from game_sprites.actors.actor import Actor
from game_sprites.actors.actor import Faction
from settings import Settings
from graphical_elements.health_bar import HealthBar

class AbstractEnemy(Actor):
    faction = Faction.Enemy

    def __init__(self, screen, level):
        """Initialize the enemy and set its starting position."""
        super().__init__(screen)

        self.starting_position = (self.screen_rect.left + self.__class__.image.get_rect().width//2,
                                  self.screen_rect.top + self.__class__.image.get_rect().height//2)
        self.set_position(self.starting_position)

        self.level = level

        self.maxhp = Settings.alien_max_hp*level
        self.hp = self.maxhp
        self.health_bar = HealthBar(screen, self)
