# Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap. Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen or vice versa
import pygame
from time import sleep
import sys

image = pygame.image.load('images/star.png')
image_rect = image.get_rect()
class Star_Invasion():
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 230)

        self.screen = pygame.display.set_mode((1600,800))
        pygame.display.set_caption("Star Invasion")

    def _create_fleet(self):
        """Make a fleet of aliens"""
        #create and alien and find the number of aliens in a row
        #spacing bewtween each alien is eqaul to one alien width
        alien = Alien(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)

        #determine the number of row of aliens that fit on the screen
        available_space_y = (self.screen_height - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        #create the full fleet of stars
        for row_number in range(number_rows):
            for alien_number in range(number_star_x):
                self._create_star(star_number, row_number)


    def _create_star(self, alien_number, row_number):
        """create an alien and place it in a row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def run_game(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(image, image_rect)
        pygame.display.flip()
if __name__ == '__main__':
    si = Star_Invasion()
    si.run_game()

sleep(5)