import pygame
from graphical_elements.explosion_animation import ExplosionAnimation

class CollisionManager:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.allied_projectiles = game.allied_projectiles
        self.enemy_projectiles = game.enemy_projectiles
        self.neutral_projectiles = game.neutral_projectiles
        self.player = game.player
        self.enemies = game.enemies
        self.drop_group = game.drop_group

    def check_collisions(self):
        self.check_enemies_projectiles_collisions()
        self.check_player_projectiles_collisions()
        self.check_player_drop_collision()
        self.check_player_enemy_collision()

    def check_enemies_projectiles_collisions(self):
        allied_collisions = pygame.sprite.groupcollide(self.enemies, self.allied_projectiles,
                                                       False, True)
        neutral_collisions = pygame.sprite.groupcollide(self.enemies, self.neutral_projectiles,
                                                        False, True)

        for enemy_hit in allied_collisions:
            for bullet in allied_collisions[enemy_hit]:
                enemy_hit.hp -= bullet.damage

        for enemy_hit in neutral_collisions:
            for bullet in neutral_collisions[enemy_hit]:
                enemy_hit.hp -= bullet.damage

    def check_player_projectiles_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemy_projectiles,
                                                       True)
        neutral_collisions = pygame.sprite.spritecollide(self.player, self.neutral_projectiles,
                                                         True)

        for bullet in enemy_collisions:
            self.player.hp -= bullet.damage

        for bullet in neutral_collisions:
            self.player.hp -= bullet.damage

    def check_player_drop_collision(self):
        drop_colisions = pygame.sprite.spritecollide(self.player, self.drop_group, True)

        for drop in drop_colisions:
            self.game.scoreboard.update_score(drop.points)
            self.game.player.increase_hp(drop.hp)

    def check_player_enemy_collision(self):
        player_colisions = pygame.sprite.spritecollide(self.player, self.enemies, True)

        for enemy in player_colisions:
            self.game.explosion_group.add(ExplosionAnimation(self.screen, enemy.position))
            self.player.hp -= 40
