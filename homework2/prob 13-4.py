import sys
from pygame.sprite import Sprite
import pygame



class RaindropsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        """Fill the sky with raindrops."""
        # Create an drop and find the number of drops in a row.
        # Spacing between each drop is equal to one drop width.
        #   Note that the spacing here works reasonably for larger drops.
        #   If you're working with smaller drops, there might be a better
        #   approach to spacing.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width

        # We'll need this number again to make new rows.
        self.number_drops_x = available_space_x // (2 * drop_width)

        # Determine the number of rows of drops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)

        # Fill the sky with drops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """Create a single row of raindrops."""
        for drop_number in range(self.number_drops_x):
            self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Create an drop and place it in the row."""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)

    def _update_raindrops(self):
        """Update drop positions, and look for drops
        that have disappeared.
        """
        self.raindrops.update()

        # Assume we won't make new drops.
        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(drop)
                make_new_drops = True

        # Make a new row of drops if needed.
        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        self.image = pygame.image.load('images/raindrop.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 2.1)
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.raindrop_speed = 1.5


if __name__ == '__main__':
    # Make a game instance, and run the game.
    rd_game = RaindropsGame()
    rd_game.run_game()