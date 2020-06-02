import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
	"""Scoreboard class"""
	def __init__(self, ai_game):
		"""Score attributes"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.game_stats

		# Font settings for scoring information
		self.text_colour = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score image
		self.prep_score()
		self.prep_hi_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Turn score into a rendered image"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, 
			self.text_colour, self.settings.bg_colour)

		# Display the score at top right
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_hi_score(self):
		"""Turn hi score into a rendered image"""
		hi_score = int(round(self.stats.hi_score, -1))
		hi_score_str = "{:,}".format(hi_score)
		self.hi_score_image = self.font.render(hi_score_str, True,
			self.text_colour, self.settings.bg_colour)

		# center hi score to top of screen
		self.hi_score_rect = self.hi_score_image.get_rect()
		self.hi_score_rect.centerx = self.screen_rect.centerx
		self.hi_score_rect.top = 20

	def prep_level(self):
		level = str(self.stats.level)
		self.level_image = self.font.render(level, True,
			self.text_colour, self.settings.bg_colour)

		# place below score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom +10

	def prep_ships(self):
		"""Show lives"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 20
			self.ships.add(ship)

	def show_score(self):
		"""Draw scoreboard"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.hi_score_image, self.hi_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def check_hi_score(self):
		"""Check if a new hi score has occured"""
		if self.stats.score > self.stats.hi_score:
			self.stats.hi_score = self.stats.score
			self.prep_hi_score()
