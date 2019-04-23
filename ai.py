import scipy
import numpy


class AI:
    def __init__(self, game):
        self.enemies = game.enemies
        self.game = game

    def update_aliens(self):
        self.brownian_movement()
        self.shoot()


    def brownian_movement(self):
        for enemy in self.enemies:
            enemy.velocity[0] += numpy.random.normal(loc=0, scale=1/230, size=None)
            enemy.velocity[1] += numpy.random.normal(loc=0, scale=1/230, size=None)

    def shoot(self):
        for enemy in self.enemies:
            maxp = 0.0001
            p = numpy.random.normal(loc=0, scale=1/enemy.level, size=None)
            if p > maxp:
                p = maxp
            check = numpy.random.randint(0, 100)
            if p > check:
                enemy.fire_weapon(self.game.enemy_projectiles)
