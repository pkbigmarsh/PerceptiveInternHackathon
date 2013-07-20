import pygame
from sprite_sheet import * 

class AnimatedSprite(pygame.sprite.Sprite):
	def __init__(self, filepath, width, height):
		pygame.sprite.Sprite.__init__(self)

		self.sprite_sheet = SpriteSheet(filepath, width, height)
		self.image = self.sprite_sheet.get_image(0,0)
		self.rect = self.image.get_rect()
		self.isPlaying = False
		self.range = [(0,0)]
		self.range_pos = 0

	def play(self):
		self.isPlaying = True

	def stop(self):
		self.isPlaying = False

	def reset(self):
		self.range_pos = 0

	def next(self):
		self.range_pos += 1
		if self.range_pos >= len(self.range):
			self.range_pos = 0
		pos = self.range[self.range_pos]
		self.image = self.sprite_sheet.get_image(pos[0], pos[1])

	def set_range(self, array_of_tuples):
		self.range = array_of_tuples
		self.reset()

	def play_row(self, row_num):
		self.play()
		self.reset()
		self.range = []
		for x in range(0, self.sprite_sheet.width):
			self.range.append((x, row_num))

	def play_column(self, col_num):
		self.play()
		self.reset()
		self.range = []
		for x in range(0,self.sprite_sheet.height):
			self.range.append((col_num, x))

	def draw(self, surface):
		surface.blit(self.image, self.rect)
		if self.isPlaying:
			self.next()
