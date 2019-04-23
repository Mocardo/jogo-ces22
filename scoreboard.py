
import pygame.font
from settings import Settings


class Scoreboard:
    # A class to report scoring information.

    def __init__(self, screen):
        # Initialize score keeping attributes.
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.score = 0

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()

    def prep_score(self):
        # Turn the score into a rendered image.
        rounded_score = int(round(self.score, -1))
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # Draw scores.
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)

    def reset_score(self):
        self.score = 0

    def update_score(self, newscore):
        self.score += newscore
