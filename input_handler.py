import pygame
import sys


class UserInput:
    def __init__(self):
        self.q_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.space_key_pressed = False

        self.mouse_left_button_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0

    def update_key_states(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   sys.exit()
            elif event.type == pygame.KEYDOWN:              self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:                self.check_keyup_events(event)

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouse_left_button_pressed = pygame.mouse.get_pressed()[1]

    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:     self.right_key_pressed = True
        elif event.key == pygame.K_LEFT:    self.left_key_pressed = True
        elif event.key == pygame.K_SPACE:   self.space_key_pressed = True
        elif event.key == pygame.K_q:       self.q_pressed = True

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:     self.right_key_pressed = False
        elif event.key == pygame.K_LEFT:    self.left_key_pressed = False
        elif event.key == pygame.K_SPACE:   self.space_key_pressed = False
        elif event.key == pygame.K_q:       self.q_pressed = False
