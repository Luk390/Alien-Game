import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class for enemies"""
	def __init__(self, ai_game):
		"""Initilise enemy with start position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load alien
		self.image = pygame.image.load('images/footballBully.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store position
		self.x = float(self.rect.x)