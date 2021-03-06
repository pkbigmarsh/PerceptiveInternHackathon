import pygame
from sprite import *
from constants import *
from metaMap import *
class Character(Sprite):
	def __init__(self, filepath, health, speed):
		Sprite.__init__(self, '../resources/char.png')
		self.health = health
		self.speed = speed

	def move(self, direction, impassables, baddies):
		#pos = self.sprite.getPosition()
		charWidth = self.rect.width
		charHeight = self.rect.height
		curX = self.rect.x
		curY = self.rect.y
		newX = curX + (direction[0] * self.speed)
		newY = curY + (direction[1] * self.speed)
		# Detect if near any edges/walls
		if newX <= 4:
			newX = WIDTH - charWidth - 5
			loadNext('left')
		elif newX >= WIDTH - charWidth -4:
			newX = 5
			loadNext('right')
		if newY <= 0:
			newY = HEIGHT - charHeight 
		elif newY >= HEIGHT - charHeight:
			newY = 0

		self.set_position(newX, newY)
		# Detect any impassable objects or baddies
		if pygame.sprite.spritecollide(self, impassables, False):
			# print "collided with impass"
			self.set_position(curX, curY)
		if pygame.sprite.spritecollide(self, baddies, False):
			self.set_position(curX, curY)

	def update(self, window_surface):
		self.draw(window_surface)
