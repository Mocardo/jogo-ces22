from pygame import Surface
from weapons.abstract_weapon import AbstractWeapon
from weapons.projectiles.bullet import Bullet


class Pistol(AbstractWeapon):
    """Fires one bullet each press."""

    def __init__(self, screen, projectile_group):
        super().__init__(screen, projectile_group)

        self.image = Surface()  # Dummy

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 1

    def fire(self, current_position, angle):
        new_projectile = Bullet(self.screen, current_position, angle,
                                self.damageMultiplier, self.speedMultiplier)
        self.projectileGroup.add(new_projectile)
