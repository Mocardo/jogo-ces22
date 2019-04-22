import pygame


class Graveyard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.player = self.game.player
        self.enemies = self.game.enemies

    def check_deaths(self):
        self.check_enemy_deaths()
        self.check_player_death()

    def check_enemy_deaths(self):
        for enemy in self.enemies:
            if enemy.hp <= 0:
                enemy.die()

    def check_player_death(self):
        if self.player.hp <= 0:
            self.game.game_active = False
            pygame.mouse.set_visible(True)
