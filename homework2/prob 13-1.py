import pygame
from pygame.sprite import Sprite
from time import sleep
import sys


class StarInvasion:
    def __init__(self):
        """Initilize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0 ), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Invasion")

        #create and instance to store game stats
        self.stars = pygame.sprite.Group()

        self._create_fleet()

        #set the background color
        self.bg_color = (230,0,0)



    def _create_fleet(self):
        """Make a fleet of aliens"""
        # create and alien and find the number of aliens in a row
        # spacing bewtween each alien is eqaul to one alien width
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # determine the number of row of aliens that fit on the screen
        available_space_y = (self.screen_height - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        # create the full fleet of aliens
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """create an alien and place it in a row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and then flip the new screen."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


    def run_game(self):
        """Start the main loop for the game."""
        self.screen.fill(self.bg_color)
        self._create_fleet()
        self._update_screen()


class Star(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, si_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = si_game.screen

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/star2.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)


if __name__ == '__main__':
    #make a game instance and run the game
    si = StarInvasion()
    si.run_game()

sleep(5)

