import pygame

class Background():

    def __init__(self, screen):
        """Initialize the background and set its starting position."""
        self.screen = screen

        # Load the background image and get its rect.
        self.image = pygame.image.load("images/background_volcanic.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new background at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the background at its current location."""
        self.screen.blit(self.image, self.rect)
