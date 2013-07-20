import pygame

class SpriteSheet():
	def __init__(self, filepath, width, height): # width and height of number tiles
		try:
			self.image = pygame.image.load(filepath).convert_alpha()
		except pygame.error, message:
			print 'Unable to load spritesheet image:', filepath
		self.filepath = filepath
		self.width = width
		self.height = height
		self.rect = self.image.get_rect()
		self.tile_rect = pygame.Rect(0, 0, self.rect.width / width, self.rect.height / height)

	def get_image(self, x, y):
		if x >= self.width or y >= self.height or x < 0 or y < 0:
			return False
		self.tile_rect.x = self.tile_rect.width * x
		self.tile_rect.y = self.tile_rect.height * y
		image = pygame.Surface(self.tile_rect.size).convert_alpha()
		image.blit(self.image, (0,0), self.tile_rect)
		return image

