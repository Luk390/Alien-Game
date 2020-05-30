class Settings:
	"""A class to store the game settings"""
	def __init__(self):
		"""Initialise game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_colour = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5

		# Bullet settings
		self.bullet_speed = 2.
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (60,60,60)
		self.bullet_limit = 3