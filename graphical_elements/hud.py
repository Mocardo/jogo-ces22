from settings import Settings
import pygame.font


class HUD:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.game = game
        self.scoreboard = game.scoreboard
        self.level_generator = game.level_generator

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

    def prep_level(self):
        # Turn the level into a rendered image.
        self.level_image = self.font.render(str(self.level_generator.nivel  ), True, self.text_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top + 5

    def prep_score(self):
        self.scoreboard.prep_score()

    def draw(self):
        self.prep_score()
        self.prep_level()
        self.screen.blit(self.level_image, self.level_rect)
        self.scoreboard.show_score()
