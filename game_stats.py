class GameStats:
    """track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start alien invasion in an active status
        self.game_active = True

    def reset_stats(self):
        """Init statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit