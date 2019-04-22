from graphical_elements.background import Background
from graphical_elements.button import Button
from graphical_elements.starting_screen import StartingScreen
import pygame


class Painter:

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.background = Background(self.screen)
        self.play_button = Button(self.screen, "Play")
        self.starting_screen = StartingScreen

    def paint(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        # screen.fill(ai_settings.bg_color)
        if self.game.game_active:
            self.background.blitme()
            self.background.blitme2()

            self.game.drop_group.blitme()
            self.game.enemies.blitme()
            self.game.ship.blitme()
            self.game.enemy_projectiles.blitme()
            self.game.neutral_projectiles.blitme()
            self.game.allied_projectiles.blitme()

            # Draw the score information.
            # sb.show_score() # TODO
        # Draw the play button if the game is inactive.
        else:
            self.starting_screen.paint()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
