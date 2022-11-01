# Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap. Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen or vice versa
import pygame
from time import sleep
import sys

image = pygame.image.load('images/ship3.png')
image_rect = image.get_rect()
class Alien_Invasion():
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 230)

        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(image, image_rect)
        pygame.display.flip()
if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()

sleep(10)