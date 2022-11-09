from pygame.sprite import Sprite
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initilize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0 ), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self._update_aliens()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the postions of all the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Make a fleet of aliens"""
        #create and alien and find the number of aliens in a row
        #spacing bewtween each alien is eqaul to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #determine the number of row of aliens that fit on the screen
        available_space_y = (self.settings.screen_height - (3 * alien_height))
        number_rows = available_space_y // (2 * alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)



    def _update_screen(self):
        """Update images on the screen, and then flip the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of represents right, -1 represents left
        self.fleet_direction = 1