class Settings:
	"""A class to store the game settings"""
	def __init__(self):
		"""Initialise game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_colour = (230, 230, 230)

		# Ship settings
		self.ship_speed = 3
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 2
		self.bullet_width = 750
		self.bullet_height = 15
		self.bullet_colour = (60,60,60)
		self.bullet_limit = 3

		# Alien settings
		self.alien_speed = 20
		self.fleet_drop_speed = 10
		# fleet direction 1 = right -1 = left
		self.fleet_direction = 1