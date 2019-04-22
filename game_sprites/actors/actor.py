from enum import Enum
from game_sprites.game_sprite import GameSprite
from graphical_elements.health_bar import HealthBar

class Faction(Enum):
    Neutral = 0
    Allied = 1
    Enemy = 2


class Actor(GameSprite):
    """A base class for the player and enemy"""
    faction = Faction.Neutral

    def __init__(self, screen):
        super().__init__(screen)

        self.starting_position = [0, 0]
        self.hp = 10
        self.weapon = None

        self.health_bar = HealthBar(screen, self)

    def update(self):
        super().update()

        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def die(self):
        self.kill()

    def fire_weapon(self, projectile_group):
        projectile_group.add(self.weapon.fire(self.rect.midtop))

    def move_to_beginning(self):
        """Center the ship on the screen."""
        self.set_position(self.starting_position)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.health_bar.draw_health_bar(self)
