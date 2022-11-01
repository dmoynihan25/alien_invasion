#Make a game that begins with a rocket in the center of the screen
import pygame
import sys

#image = pygame.image.load('images/rocket.png')
#image_rect = image.get_rect()
class Alien_Invasion():
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 230)

        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()
