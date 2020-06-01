import pygame.font

class Scoreboard:
	"""Scoreboard class"""
	def __init__(self, ai_game):
		"""Score attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.game_stats

		# Font settings for scoring information
		self.text_colour = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		# Prepare the initial score image
		self.prep_score()

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

	def show_score(self):
		"""Draw scoreboard"""
		self.screen.blit(self.score_image, self.score_rect)
