import numpy as np
from alien import Alien
from scipy.stats import *
import game_functions as gf
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

    @classmethod
    def create_fleet(cls, ai_settings1, screen1, ship1, aliens1):

        "codigo distribuicao"
        cls.ai_settings = ai_settings1
        cls.screen = screen1
        cls.ship = ship1
        cls.aliens = aliens1

        alien = Alien(cls.ai_settings, cls.screen)
        number_aliens_x = gf.get_number_aliens_x(cls.ai_settings, alien.rect.width)
        number_rows = gf.get_number_rows(cls.ai_settings, cls.ship.rect.height, alien.rect.height)
        sizefleet = number_rows * number_aliens_x

        cls.nivel = cls.nivel + 1
        "entradas = (chi2.rvs(nivel, size = qtde))"
        upperlimit = 10 + math.floor(chi2.ppf(0.90, cls.nivel))
        entradas = [random.randrange(1, upperlimit) for _ in range(sizefleet)]
        dificuldade = []
        i = 0
        while len(dificuldade) < sizefleet:
            dificuldade.append(math.ceil(1 / (0.1 + chi2.cdf(entradas[i], cls.nivel))))
            i = i + 1

        print(dificuldade)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                gf.create_alien(cls.ai_settings, cls.screen, cls.aliens, alien_number, row_number)
