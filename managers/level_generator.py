from game_sprites.actors.enemy.alien import Alien
from scipy.stats import *
import math
import random
from settings import Settings


class LevelGenerator:

    def __init__(self, game):
        self.screen = game.screen
        self.player = game.player
        self.enemies = game.enemies
        self.nivel = 0

    def create_fleet(self):

        "codigo distribuicao"
        alien_rect = Alien.image.get_rect()
        number_aliens_x = self.get_number_enemies_x(alien_rect.width)
        number_rows = self.get_number_rows(self.player.rect.height, alien_rect.height)
        sizefleet = number_rows * number_aliens_x

        self.nivel = self.nivel + 1
        "entradas = (chi2.rvs(nivel, size = qtde))"
        upperlimit = 10 + math.floor(chi2.ppf(0.90, self.nivel))
        entradas = [random.randrange(1, upperlimit) for _ in range(sizefleet)]
        dificuldade = []
        i = 0
        while len(dificuldade) < sizefleet:
            dificuldade.append(math.ceil(1 / ((0.1/math.sqrt(self.nivel)) + chi2.cdf(entradas[i], self.nivel))))
            i = i + 1

        print(dificuldade)
        i = 0
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number, dificuldade[i])
                i = i+1

    def get_number_enemies_x(self, enemy_width):
        """Determine the number of aliens that fit in a row."""
        available_space_x = Settings.screen_width - 2 * enemy_width
        number_enemies_x = int(available_space_x / (2 * enemy_width))
        return number_enemies_x

    def get_number_rows(self, player_height, enemy_height):
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = (Settings.screen_height - (3 * enemy_height) - player_height)
        number_rows = int(available_space_y / (2 * enemy_height))
        return number_rows

    def create_alien(self, alien_number, row_number, dificulty):
        """Create an alien and place it in the row."""
        alien = Alien(self.screen, dificulty)
        alien_width = alien.rect.width

        alien.set_position([alien_width + 2 * alien_width * alien_number,
                           alien.rect.height + 2 * alien.rect.height * row_number])

        self.enemies.add(alien)
