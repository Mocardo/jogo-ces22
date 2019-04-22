import pygame


class CollisionManager:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.allied_projectiles = self.game.allied_projectiles
        self.enemy_projectiles = self.game.enemy_projectiles
        self.neutral_projectiles = self.game.neutral_projectiles
        self.player = self.game.player
        self.enemies = self.game.enemies

    def check_collisions(self):
        self.check_enemies_projectiles_collisions()
        self.check_player_projectiles_collisions()

    def check_enemies_projectiles_collisions(self):
        allied_collisions = pygame.sprite.groupcollide(self.enemies, self.allied_projectiles,
                                                       False, True)
        neutral_collisions = pygame.sprite.groupcollide(self.enemies, self.neutral_projectiles,
                                                        False, True)

        for enemy_hit, bullets in allied_collisions:
            for bullet in bullets:
                enemy_hit.decrease_life(bullet.damage)

        for enemy_hit, bullets in neutral_collisions:
            for bullet in bullets:
                enemy_hit.decrease_life(bullet.damage)

    def check_player_projectiles_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemy_projectiles,
                                                       True)
        neutral_collisions = pygame.sprite.spritecollide(self.player, self.neutral_projectiles,
                                                         True)

        for bullet in enemy_collisions:
            self.player.decrease_life(bullet.damage)

        for bullet in neutral_collisions:
            self.player.decrease_life(bullet.damage)
