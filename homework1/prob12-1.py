# Blue Sky: Make a Pygame window with a blue background
import pygame
from time import sleep
import sys

class Alien_Invasion():
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 230)

        self.screen = pygame.display.set_mode((200,200))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()

sleep(8)