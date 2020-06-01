class GameStats:
	"""Track stats"""

	def __init__(self, ai_game):
		"""Initialise stat tracker"""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start game in inactive state
		self.game_active = False


	def reset_stats(self):
		"""Initialise stats that can change in the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
