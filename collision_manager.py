import pygame


class CollisionManager:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.friend_projectiles = self.game.friend_projectiles
        self.enemy_projectiles = self.game.enemy_projectiles
        self.neutral_projectiles = self.neutral_projectiles
        self.player = self.player
        self.enemies = self.enemies

    def check_collisions(self):



    def check_projectile_enemy_collisions(self):
        enemy_collisions = pygame.sprite.groupcollide(self.friend_projectiles,
                                                      self.enemies, True, False)
        if enemy_collisions:
            for bullet, enemies_hit in enemy_collisions:
                for enemy_hit in enemies_hit:
                    enemy_hit.decrease_life(bullet.damage)

    def check_projectile_player_collisions(self):
        enemy_collisions = pygame.sprite.groupcollide(self.enemy_projectiles,
                                                      self.player, True, False)
        if enemy_collisions:
            for bullet, enemies_hit in enemy_collisions:
                for enemy_hit in enemies_hit:
                    enemy_hit.decrease_life(bullet.damage)