from pygame import Surface
from weapons.abstract_weapon import AbstractWeapon
from game_sprites.projectiles.bullet import Bullet


class Pistol(AbstractWeapon):
    """Fires one bullet each press."""
    image = None  # TODO
    ammoType = Bullet

    def __init__(self, screen, faction):
        super().__init__(screen, faction)

        self.damageMultiplier = 1
        self.speedMultiplier = 1
        self.fireRate = 1
