from pygame.sprite import Sprite
from weapons.projectiles.abstract_projectile import AbstractProjectile


class AbstractWeapon(Sprite):
    """Base class for all game weapons."""

    def __init__(self, screen, projectile_group):
        super().__init__(self)

        self.screen = screen
        self.image = None  # dummy
        self.projectile_group = projectile_group

        self.damage_multiplier = 1
        self.speed_multiplier = 1
        self.fire_rate = 1

    def fire(self, current_position, angle):
        # TODO
        new_projectile = AbstractProjectile(self.screen, current_position, angle,
                                            self.damage_multiplier, self.speed_multiplier, )
        self.projectile_group.add(new_projectile)
