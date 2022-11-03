#Make a game that begins with a rocket in the center of the screen
import pygame
import sys

class Alien_Invasion():
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 0)

        self.screen = pygame.display.set_mode((200,200))
        pygame.display.set_caption("Alien Invasion")




    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("You pressed a key!")

            elif event.type == pygame.KEYUP:
                print('You unpressed the key!')

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()