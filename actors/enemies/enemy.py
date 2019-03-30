from actors.actor import Actor


class Enemy(Actor):

    def __init__(self, screen, projectile_group):
        """Initialize the ship and set its starting position."""
        super(Enemy, self).__init__(screen, projectile_group)

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.float_center = [float(self.rect.center[0]), float(self.rect.center[1])]
