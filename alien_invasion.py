import sys
from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""
	def __init__(self):
		"""Initilise the game, and create game resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

		# Set background colour
		self.bg_colour = (230, 230, 230)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_bullets()
			self._update_screen()

	def _check_events(self):		
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Stop moving right
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			# Stop moving left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Stop moving ship to the right
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			# Stop moving ship to the left
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullet group"""
		if len(self.bullets) < self.settings.bullet_limit:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		# Get rid of old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		print(len(self.bullets))

	def _update_screen(self):
		"""update images on the screen and flip to the new screen"""
		# Redraw the screen during each pass through the loop
		self.screen.fill(self.bg_colour)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Make the most recently drawn screen visible
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()