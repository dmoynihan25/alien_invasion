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
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False


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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.ship_speed = 1.5

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.ship_speed
        if self.moving_up and self.rect.top < self.screen_rect.top:
            self.y += self.ship_speed
        if self.moving_down and self.rect.bottom > 0:
            self.y -= self.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()
