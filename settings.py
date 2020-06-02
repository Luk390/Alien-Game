class Settings:
	"""A class to store the game settings"""
	def __init__(self):
		"""Initialise game static settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 750
		self.bg_colour = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 2
		self.bullet_width = 2
		self.bullet_height = 15
		self.bullet_colour = (60,60,60)
		self.bullet_limit = 3

		# Alien settings
		self.alien_speed = 1
		self.fleet_drop_speed = 10

		# fleet direction 1 = right -1 = left
		self.fleet_direction = 1

		# Game difficulty ramp speed
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		"""Initialise settings that change"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.
		self.alien_speed = 2
		# scoring 
		self.alien_points = 2

		# fleet_direction of 1 = right, -1 = left
		self.fleet_direction = 1


	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points *= self.score_scale





