from actors.actor import Actor
from actors.actor import Faction


class Enemy(Actor):
    faction = Faction.ENEMY

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        super(Enemy, self).__init__(screen)

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
