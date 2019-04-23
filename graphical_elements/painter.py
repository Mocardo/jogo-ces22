from graphical_elements.background import Background
from settings import GameState
import pygame


class Painter:

    def __init__(self, game):
        self.screen = game.screen
        self.game = game

        self.background = Background(self.screen)

    def paint(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        # screen.fill(ai_settings.bg_color)
        if self.game.game_state == GameState.game_active or self.game.game_state == GameState.game_level_passed:
            self.background.blitme()
            self.background.blitme2()
            self.background.update()

            self.game.enemies.blitme()
            self.game.drop_group.blitme()
            self.game.enemy_projectiles.blitme()
            self.game.neutral_projectiles.blitme()
            self.game.allied_projectiles.blitme()
            self.game.player.blitme()

            # Draw the score information.
            # sb.show_score() # TODO
        # Draw the play button if the game is inactive.
        else:
            self.game.starting_screen.paint()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
