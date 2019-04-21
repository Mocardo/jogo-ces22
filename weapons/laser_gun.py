from pygame import Surface
from weapons.abstract_weapon import AbstractWeapon
from game_sprites.projectiles.laser import Laser


class LaserGun(AbstractWeapon):
    """The weapon that fires LAZORS111!!!!1!1!"""

    def __init__(self, screen, projectile_group):
        super().__init__(screen, projectile_group)

        self.image = Surface()  # Dummy

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 0.5

    def fire(self, current_position, angle):
        new_projectile = Laser(self.screen, current_position, angle,
                               self.damageMultiplier, self.speedMultiplier)
        self.projectileGroup.add(new_projectile)
