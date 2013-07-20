import pygame

spriteImages = dict()

class Sprite(pygame.sprite.Sprite):
	def __init__(self, filepath):
		pygame.sprite.Sprite.__init__(self)
		self.filepath = filepath
		if filepath not in spriteImages:
			spriteImages[filepath] = pygame.image.load(filepath)
		self.image = spriteImages[filepath]
		self.rect = self.image.get_rect()

	def set_position(self, inc_x, inc_y):
		self.rect.x = inc_x
		self.rect.y = inc_y

	def get_position(self):
		return (self.rect.x, self.rect.y)

	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def draw(self, window_surface):
		window_surface.blit(self.image, self.rect)
