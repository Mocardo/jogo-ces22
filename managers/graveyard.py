from game_sprites.drops.drop import Drop
from game import GameState

class Graveyard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

    def check_deaths(self):
        self.check_enemy_deaths()
        self.check_player_death()

    def check_enemy_deaths(self):
        for enemy in self.game.enemies:
            if enemy.hp <= 0:
                self.game.drop_group.add(Drop(self.screen, enemy.position))
                enemy.die()

        if len(self.game.enemies.sprites()) == 0:
            self.game.game_state = GameState.game_level_passed
            self.game.clock.tick()




    def check_player_death(self):
        if self.game.player.hp <= 0:
            self.game.end_game()
