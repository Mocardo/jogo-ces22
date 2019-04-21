from pygame import Surface
from weapons.abstract_weapon import AbstractWeapon
from game_sprites.projectiles.laser import Laser


class LaserGun(AbstractWeapon):
    """The weapon that fires LAZORS111!!!!1!1!"""
    image = None  # TODO
    ammoType = Laser

    def __init__(self, screen, faction):
        super().__init__(screen, faction)

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 0.5
