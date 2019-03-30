

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
        self.enemy_projectiles