import pygame
import sys


class InputHandler:
    def __init__(self, game):
        self.q_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.up_key_pressed = False
        self.down_key_pressed = False
        self.space_key_pressed = False

        self.mouse_left_button_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0

        self.game = game

    def parse_user_input(self):
        self.update_key_states()

        if self.q_pressed:
            sys.exit()
        if self.game.game_active:
            self.game.player.velocity = [self.right_key_pressed - self.left_key_pressed,
                                         self.down_key_pressed - self.up_key_pressed]
            if self.space_key_pressed:
                self.game.player.fire_weapon(self.game.allied_projectiles)
            else:
                self.game.player.cooldown_weapon()
        else:
            if self.mouse_left_button_pressed and self.game.starting_screen.check_if_started(self.mouse_x, self.mouse_y):
                self.game.begin_game()

    def update_key_states(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   sys.exit()
            elif event.type == pygame.KEYDOWN:              self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:                self.check_keyup_events(event)

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouse_left_button_pressed = pygame.mouse.get_pressed()[0]

    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:     self.right_key_pressed = True
        elif event.key == pygame.K_LEFT:    self.left_key_pressed = True
        elif event.key == pygame.K_UP:      self.right_key_pressed = True
        elif event.key == pygame.K_DOWN:    self.down_key_pressed = True
        elif event.key == pygame.K_SPACE:   self.space_key_pressed = True
        elif event.key == pygame.K_q:       self.q_pressed = True

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:     self.right_key_pressed = False
        elif event.key == pygame.K_LEFT:    self.left_key_pressed = False
        elif event.key == pygame.K_UP:      self.right_key_pressed = False
        elif event.key == pygame.K_DOWN:    self.down_key_pressed = False
        elif event.key == pygame.K_SPACE:   self.space_key_pressed = False
        elif event.key == pygame.K_q:       self.q_pressed = False
