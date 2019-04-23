import sys
import pygame

from game_sprites.actors.player import Player
from game_sprites.actors.enemy.enemy_group import EnemyGroup
from game_sprites.projectiles.projectile_group import ProjectileGroup
from game_sprites.drops.drop_group import DropGroup
from settings import GameState
from settings import Settings
from game_stats import GameStats
from managers.input_handler import InputHandler
from graphical_elements.painter import Painter
from managers.collision_manager import CollisionManager
from managers.graveyard import Graveyard
from managers.level_generator import LevelGenerator
from graphical_elements.starting_screen import StartingScreen


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("Chen Invaders")

        self.stats = GameStats()
        # self.sb = Scoreboard(self.screen, self.stats)

        # Make a ship, a group of projectiles, and a group of aliens.

        self.allied_projectiles = ProjectileGroup(self.screen)
        self.enemy_projectiles = ProjectileGroup(self.screen)
        self.neutral_projectiles = ProjectileGroup(self.screen)
        self.drop_group = DropGroup(self.screen)

        self.player = Player(self.screen)
        self.enemies = EnemyGroup(self.screen)

        self.collision_manager = CollisionManager(self)
        self.graveyard = Graveyard(self)
        self.level_generator = LevelGenerator(self)

        self.input_handler = InputHandler(self)
        self.starting_screen = StartingScreen(self.screen)
        self.painter = Painter(self)

        self.game_state = GameState.game_inactive
        self.clock = pygame.time.Clock()
        self.time0 = 0

        # setting BGM
        pygame.mixer.init()
        pygame.mixer.music.load("sound/BGM.mp3")

    def run(self):
        while True:
            self.input_handler.parse_user_input()
            if self.game_state == GameState.game_active or self.game_state == GameState.game_level_passed:
                self.player.update()
                self.enemies.update()
                self.drop_group.update()
                self.allied_projectiles.update()
                self.enemy_projectiles.update()
                self.neutral_projectiles.update()
                self.collision_manager.check_collisions()
                if self.game_state == GameState.game_active:
                    self.graveyard.check_deaths()
                elif self.game_state == GameState.game_level_passed:
                    self.level_ended()
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
            else:
                pass
            self.painter.paint()

    def begin_game(self):

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        self.game_state = GameState.game_active

        # Reset the scoreboard images.
        # sb.prep_score()        # TODO
        # sb.prep_high_score()
        # sb.prep_level()
        # sb.prep_ships()

        # Empty the list of aliens and bullets.
        self.enemies.empty()
        self.allied_projectiles.empty()
        self.enemy_projectiles.empty()
        self.neutral_projectiles.empty()
        self.drop_group.empty()

        # Create a new fleet and center the ship.
        self.level_generator.create_fleet()




    def level_ended(self):
        # TODO fazer animacaozinha que o alien desce do topo ate o meio
        self.time0 += self.clock.tick()
        print(self.time0)
        if self.time0 > Settings.next_level_delay:
            self.game_state = GameState.game_active
            self.time0 = 0
            self.begin_game()




    """
    def check_high_score(stats, sb):
        # Check to see if there's a new high score.
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()
    """

    """
    def create_enemies(self):
        # Create a full fleet of aliens.
        # Create an alien and find the number of aliens in a row.
        enemy = Alien(self.screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

        # Create the fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)

    def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        # Create an alien and place it in the row.
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)
    """

    def end_game(self):
        """Respond to ship being hit by alien."""
        # TODO implement lives
        """"
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
            """
        self.game_state = GameState.game_inactive
        pygame.mouse.set_visible(True)
