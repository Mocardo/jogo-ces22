import math
from game_sprites.game_sprite import GameSprite
from game_sprites.actors.actor import Faction
from settings import Settings


class AbstractProjectile(GameSprite):
    """A class to manage projectiles fired by anyone."""
    image = None

    def __init__(self, screen, starting_position, starting_angle, damage_multiplier, speed_multiplier, faction):
        """Create a projectile at a given position moving through a given angle"""
        super().__init__(screen)

        self.faction = faction

        if self.faction == Faction.Allied:
            self.base_speed = Settings.player_bullet_base_speed
        else:
            self.base_speed = Settings.enemy_bullet_base_speed

        self.base_damage = Settings.bullet_base_damage

        self.set_position(starting_position)
        self.angle = starting_angle
        self.speed = self.base_speed * speed_multiplier
        self.damage = self.base_damage * damage_multiplier

    def update(self):
        """Move the bullet through the screen."""
        self.velocity = [math.cos(self.angle), - math.sin(self.angle)]
        self.velocity = [self.speed * i for i in self.velocity]

        super().update()
