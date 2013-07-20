import pygame

class Sprite(filepath):
	def __init__(self, filepath):
		self.filepath = filepath
		self.image = pygame.image.load(filepath)
		self.rect = self.image.get_rect()

	def move(self, inc_x, inc_y):
		self.rect.move((inc_x, inc_y))

	def get_position(self):
		return (self.rect.left, self.rect.top)

	def draw(self, window_surface):
		window_surface.blit()