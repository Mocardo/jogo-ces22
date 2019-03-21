import pygame
from player.ship import Ship
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from rendering.background import Background




class Game:
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode(
            (Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(screen)

        stats = GameStats()
        sb = Scoreboard(screen, stats)

        # Make the background
        background = Background(screen)

        # Make the Play button.
        play_button = Button(screen, "Play")

        # Create an instance to store game statistics and create a scoreboard.


        # Make a ship, a group of bullets, and a group of aliens.

        bullets = Group()
        aliens = Group()

        # Create the fleet of aliens.
        gf.create_fleet(ai_settings, screen, ship, aliens)

        # setting BGM
        pygame.mixer.init()
        pygame.mixer.music.load("sound/魂斗罗 归来剧情模式经典6.mp3")

    # Start the main loop for the game.
    def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                stats.score += ai_settings.alien_points * len(aliens)
                sb.prep_score()
            check_high_score(stats, sb)

        if len(aliens) == 0:
            # If the entire fleet is destroyed, start a new level.
            # Destroy existing bullets, speed up game, and create new fleet.
            bullets.empty()
            ai_settings.increase_speed()

            # Increase level.
            stats.level += 1
            sb.prep_level()

            create_fleet(ai_settings, screen, ship, aliens)

    def run(self):
        while True:
            gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
            if stats.game_active:
                background.update()
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
                if pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.play()
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button, background)


