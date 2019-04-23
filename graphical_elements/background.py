import pygame


class Background:
    image = pygame.image.load("images/background_volcanic.bmp")

    def __init__(self, screen):
        """Initialize the background and set its starting position."""
        self.screen = screen

        # Load the background image and get its rect.
        self.rect = self.__class__.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new background at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the background at its current location."""
        self.screen.blit(self.__class__.image, self.rect)

    def blitme2(self):
        """Draw the background on the auxiliar location"""
        self.rect.bottom -= self.screen_rect.bottom
        self.screen.blit(self.__class__.image, self.rect)
        self.rect.bottom += self.screen_rect.bottom

    def update(self):
        if self.rect.bottom <= 2*self.screen_rect.bottom:
            self.rect.bottom += 1
        else:
            self.rect.bottom = self.screen_rect.bottom
