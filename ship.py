import pygame

class Ship:
	"""Manages the ship"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Load the ship image to the rect
		self.image = pygame.image.load('images/BEER.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False

		# Ship's position as decimal value
		self.x = float(self.rect.x)

	def update(self):
		"""Update the ship's position based on the movement flag"""
		if self.moving_right:
			if self.rect.right < self.settings.screen_width - 10:
				self.x += self.settings.ship_speed
		if self.moving_left:
			if self.rect.left > 5:
				self.x -= self.settings.ship_speed

		# Update ship position
		self.rect.x = self.x

	def blitme(self):
		# Draw the ship at its current location
		self.screen.blit(self.image, self.rect)