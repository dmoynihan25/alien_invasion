#This is Dennis's Pygame
import sys
import pygame
from settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the shipe image and get its rect.
        self.image = pygame.image.laod('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initilize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #set the background color
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()