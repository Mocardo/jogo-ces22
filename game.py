import sys
import pygame

from game_sprites.actors.player import Player
from game_sprites.actors.enemy.enemy_group import EnemyGroup
from game_sprites.projectiles.projectile_group import ProjectileGroup

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from input_handler import InputHandler
from graphical_elements.painter import Painter
from managers.collision_manager import CollisionManager
from managers.graveyard import Graveyard


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("Chen Invaders")

        self.stats = GameStats()
        self.sb = Scoreboard(self.screen, self.stats)

        # Make a ship, a group of projectiles, and a group of aliens.

        self.allied_projectiles = ProjectileGroup(self.screen)
        self.enemy_projectiles = ProjectileGroup(self.screen)
        self.neutral_projectiles = ProjectileGroup(self.screen)

        self.player = Player(self.screen)
        self.enemies = EnemyGroup(self.screen)

        self.drop_group = pygame.sprite.Group()

        self.collision_manager = CollisionManager(self)
        self.graveyard = Graveyard(self)

        self.input_handler = InputHandler()
        self.painter = Painter(self)

        self.game_active = False

        # setting BGM
        pygame.mixer.init()
        pygame.mixer.music.load("sound/BGM.mp3")

    def run(self):
        while True:
            self.read_user_input()
            if self.game_active:
                self.update()
                self.collision_manager.check_collisions()
                self.graveyard.check_deaths()
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
            self.painter.paint()

    def update(self):
        self.player.update()
        self.enemies.update()
        self.allied_projectiles.update()
        self.enemy_projectiles.update()
        self.neutral_projectiles.update()

    def read_user_input(self):
        self.input_handler.update_key_states()

        if self.input_handler.q_pressed:
            sys.exit()
        if self.game_active:
            # TODO
            self.player.velocity = [self.input_handler.right_key_pressed - self.input_handler.left_key_pressed,
                                    self.input_handler.down_key_pressed - self.input_handler.up_key_pressed]
            if self.input_handler.space_key_pressed:
                self.player.fire_weapon()
        else:
            if self.play_button.check_if_clicked():
                self.begin_game()

    def begin_game(self):
        # Reset the game settings.
        self.ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        self.stats.reset_stats()
        self.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

    def check_high_score(stats, sb):
        """Check to see if there's a new high score."""
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()

    def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)

    def create_fleet(ai_settings, screen, ship, aliens):
        """Create a full fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

        # Create the fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)

    def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Respond to ship being hit by alien."""
        if stats.ships_left > 0:
            # Decrement ships_left.
            stats.ships_left -= 1

            # Update scoreboard.
            sb.prep_ships()

            # Empty the list of aliens and bullets.
            aliens.empty()
            bullets.empty()

            # Create a new fleet and center the ship.
            create_fleet(ai_settings, screen, ship, aliens)
            ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)
