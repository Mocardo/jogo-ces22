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
from pygame.sprite import Group
from ai import AI


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
        self.explosion_group = Group()

        self.player = Player(self.screen)
        self.enemies = EnemyGroup(self.screen)

        self.collision_manager = CollisionManager(self)
        self.graveyard = Graveyard(self)
        self.level_generator = LevelGenerator(self)
        self.input_handler = InputHandler(self)

        self.starting_screen = StartingScreen(self.screen)
        self.painter = Painter(self)

        self.ai = AI(self)

        self.game_state = GameState.game_inactive

        self.clock = pygame.time.Clock()
        self.time_until_next_horde = 0
        pygame.mixer.init()



    def run(self):

        pygame.mixer.music.load("sound/start.mp3")
        while True:
            self.input_handler.parse_user_input()
            if self.game_state == GameState.game_active or self.game_state == GameState.game_level_passed:
                break
            else:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
            self.painter.paint()
        pygame.mixer.music.load("sound/BGM.mp3")
        while True:
            self.input_handler.parse_user_input()
            if self.game_state == GameState.game_active:
                self.player.update()
                self.ai.update_aliens()
                self.enemies.update()
                self.drop_group.update()
                self.allied_projectiles.update()
                self.enemy_projectiles.update()
                self.neutral_projectiles.update()
                self.collision_manager.check_collisions()
                self.graveyard.check_deaths()
                self.explosion_group.update()
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
            elif self.game_state == GameState.game_level_passed:
                self.player.update()
                self.enemies.update()
                self.drop_group.update()
                self.allied_projectiles.update()
                self.enemy_projectiles.update()
                self.neutral_projectiles.update()
                self.collision_manager.check_collisions()
                self.explosion_group.update()
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                self.level_ended()
            self.painter.paint()

    def begin_game(self):

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the scoreboard images.
        # sb.prep_score()        # TODO
        # sb.prep_high_score()
        # sb.prep_level()
        # sb.prep_ships()

        self.begin_level()

    def begin_level(self):
        self.game_state = GameState.game_active
        self.time_until_next_horde = 0

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
        tick = float(self.clock.tick())
        self.time_until_next_horde += tick
        if self.time_until_next_horde > Settings.next_level_delay:
            self.game_state = GameState.game_active
            self.begin_level()

    """
    def check_high_score(stats, sb):
        # Check to see if there's a new high score.
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()
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
