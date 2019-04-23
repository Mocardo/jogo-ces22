import pygame
from game_sprites.actors.actor import Actor
from game_sprites.actors.actor import Faction
from settings import Settings
from weapons.pistol import Pistol


class Player(Actor):
    image = pygame.image.load('images/ship.png')
    faction = Faction.Allied

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        super().__init__(screen)

        # Start each new ship at the bottom center of the screen.
        self.starting_position = (self.screen_rect.centerx,
                                  self.screen_rect.bottom - self.__class__.image.get_rect().height//2)
        self.set_position(self.starting_position)

        self.maxhp = Settings.player_max_hp
        self.hp = self.maxhp
        self.speed = Settings.player_base_speed
        self.weapon = Pistol(self.screen, self.__class__.faction)

    def reset_health(self):
        self.hp = self.maxhp

    def reset_position(self):
        self.position = self.starting_position

    def fire_weapon(self, projectile_group):
        if self.weapon.weapon_ready():
            projectile_group.add(self.weapon.fire(self.rect.midtop))

    def increase_hp(self, hp):
        self.hp += hp
        if self.hp > self.maxhp:
            self.hp = self.maxhp

