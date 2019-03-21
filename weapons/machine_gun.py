from pygame import Surface
from weapons.abstract_weapon import AbstractWeapon
from weapons.projectiles.bullet import Bullet


class MachineGun(AbstractWeapon):
    """Fires bullets very fast."""

    def __init__(self, screen, projectile_group):
        super().__init__(screen, projectile_group)

        self.image = Surface()  # Dummy

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 10

    def fire(self, current_position, angle):
        new_projectile = Bullet(self.screen, current_position, angle,
                                self.damageMultiplier, self.speedMultiplier)
        self.projectileGroup.add(new_projectile)
