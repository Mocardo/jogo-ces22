import sys
import pygame

from actors.player import Ship
from weapons.projectiles.projectile_group import ProjectileGroup
from actors.enemies.enemy_group import EnemyGroup

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from input_handler import UserInput
from graphical_elements.painter import Painter


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("Chen Invaders")

        self.stats = GameStats()
        self.sb = Scoreboard(self.screen, self.stats)

        # Make a ship, a group of projectiles, and a group of aliens.

        self.ship = Ship(self.screen)
        self.projectiles = ProjectileGroup(self.screen)
        self.aliens = EnemyGroup(self.screen)

        self.user_input = UserInput()
        self.painter = Painter(self.screen, self)

        self.game_active = False

        # setting BGM
        pygame.mixer.init()
        pygame.mixer.music.load("sound/魂斗罗 归来剧情模式经典6.mp3")

    def run(self):
        while True:
            self.user_input.update_key_states()
            self.parse_user_input()
            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self.update_aliens()
                self.painter.paint()
                if pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.play()
            self.update_screen()

    def parse_user_input(self):
        if self.user_input.q_pressed:
            sys.exit()
        if self.game_active:
            self.ship.moving_left = self.user_input.left_key_pressed
            self.ship.moving_right = self.user_input.right_key_pressed
            if self.user_input.space_key_pressed:
                self.ship.fire()
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



    def get_number_aliens_x(ai_settings, alien_width):
        """Determine the number of aliens that fit in a row."""
        available_space_x = ai_settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(ai_settings, ship_height, alien_height):
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows

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

    def check_fleet_edges(ai_settings, aliens):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break

    def change_fleet_direction(ai_settings, aliens):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1

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

    def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
                break

    def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet."""
        check_fleet_edges(ai_settings, aliens)
        aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Look for aliens hitting the bottom of the screen.
        check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
