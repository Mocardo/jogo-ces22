import math
from pygame.sprite import Sprite
from game_sprites.actors.actor import Faction
from game_sprites.projectiles.abstract_projectile import AbstractProjectile


class AbstractWeapon(Sprite):
    """Base class for all game weapons."""
    image = None
    ammoType = AbstractProjectile

    def __init__(self, screen, faction):
        super().__init__()

        self.screen = screen
        self.faction = faction

        self.damage_multiplier = 1
        self.speed_multiplier = 1
        self.fire_rate = 1

        if self.faction == Faction.Enemy:
            self.target_angle = - math.pi / 2
            self.position_correction = (0, self.__class__.ammoType.image.get_rect().height//2)
        else:
            self.target_angle = math.pi / 2
            self.position_correction = (0, - self.__class__.ammoType.image.get_rect().height//2)

    def fire(self, starting_position, angle=None):  # TODO: implementar mira
        new_projectile = self.__class__.ammoType(self.screen,
                                                 list(map(sum, zip(starting_position, self.position_correction))),
                                                 self.target_angle, self.damage_multiplier,
                                                 self.speed_multiplier, self.faction)
        return new_projectile
