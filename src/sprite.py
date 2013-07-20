import pygame

class Sprite(pygame.sprite.Sprite):
	def __init__(self, filepath):
		self.filepath = filepath
		self.image = pygame.image.load(filepath)
		self.rect = self.image.get_rect()

	def set_(self, inc_x, inc_y):
		self.rect.move((inc_x, inc_y))

	def get_position(self):
		return (self.rect.x, self.rect.y)

	def draw(self, window_surface):
		window_surface.blit(self.image, self.rect)