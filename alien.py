import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class for enemies"""
	def __init__(self, ai_game):
		"""Initilise enemy with start position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load alien
		self.image = pygame.image.load('images/aaron.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store position
		self.x = float(self.rect.x)

	def update(self):
		"""Move alien to the right """
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x


	def check_edges(self):
		"""Return True if alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <=0:
			return True
		
