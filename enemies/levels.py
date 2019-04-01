import numpy as np
from alien import Alien
from scipy.stats import *
from game_functions import *
import math
import random


class Level:
    ai_settings = None
    screen = None
    ship = None
    aliens = None
    nivel = 0

    def __init__(self):
        pass

    @staticmethod
    def create_fleet(self, ai_settings1, screen1, ship1, aliens1):

        "codigo distribuicao"
        ai_settings = ai_settings1
        screen = screen1
        ship = ship1
        aliens = aliens1

        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
        sizefleet = number_rows * number_aliens_x

        nivel = .nivel + 1
        "entradas = (chi2.rvs(nivel, size = qtde))"
        upperlimit = 10 + math.floor(chi2.ppf(0.90, self.nivel))
        entradas = [random.randrange(1, upperlimit) for _ in range(self.sizefleet)]
        dificuldade = []
        i = 0
        while len(dificuldade) < self.sizefleet:
            dificuldade.append(math.ceil(1 / (0.1 + chi2.cdf(entradas[i], self.nivel))))
            i = i + 1

        for row_number in range(self.number_rows):
            for alien_number in range(self.number_aliens_x):
                create_alien(self.ai_settings, self.screen, self.aliens, alien_number, row_number)
