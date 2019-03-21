from pygame.sprite import Sprite
from pygame import Surface
from weapons.projectiles.abstract_projectile import AbstractProjectile


class AbstractWeapon(Sprite):
    """Base class for all game weapons."""

    def __init__(self, screen, projectile_group):
        super().__init__(self)

        self.screen = screen
        self.image = Surface()  # dummy

        self.projectileGroup = projectile_group

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 1

    def fire(self, current_position, angle):
        new_projectile = AbstractProjectile(self.screen, current_position, angle,
                                            self.damageMultiplier, self.speedMultiplier)
        self.projectileGroup.add(new_projectile)
