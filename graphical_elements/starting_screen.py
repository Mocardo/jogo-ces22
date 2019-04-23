from graphical_elements.button import Button
import pygame


class StartingScreen:
    image = pygame.image.load("images/start.PNG")

    def __init__(self, screen):
        self.screen = screen
        self.play_button = Button(screen, "Play")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def paint(self):
        self.screen.blit(self.image, self.rect)
        self.play_button.draw_button()

    def check_if_started(self, mouse_x, mouse_y):
        return self.play_button.check_if_clicked(mouse_x, mouse_y)
