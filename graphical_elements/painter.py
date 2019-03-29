from graphical_elements.background import Background
from graphical_elements.button import Button


class Painter:

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.background = Background(self.screen)
        self.play_button = Button(self.screen, "Play")

    def paint(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        # screen.fill(ai_settings.bg_color)
        self.background.blitme()
        self.background.blitme2()
        self.game.ship.blitme()
        # alien.blitme()
        self.game.aliens.draw(screen)

        # Redraw all bullets behind ship and aliens.
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        # Draw the score information.
        sb.show_score()

        # Draw the play button if the game is inactive.
        if not stats.game_active:
            play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
