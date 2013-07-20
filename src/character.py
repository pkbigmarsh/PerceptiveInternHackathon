import pygame
from sprite import *
from constants import *

class Character:
	def __init__(self):
		self.sprite = Sprite('../resources/char.png')
		self.health = 10
		self.speed = 10

	def move(self, direction):
		#pos = self.sprite.getPosition()
		charWidth = self.sprite.rect.width
		charHeight = self.sprite.rect.height
		curX = self.sprite.rect.x
		curY = self.sprite.rect.y
		newX = curX + (direction[0] * self.speed)
		newY = curY + (direction[1] * self.speed)

		# Detect if near any edges/walls
		if newX <= 0:
			newX = 0 
		elif newX >= WIDTH - charWidth:
			newX = WIDTH - charWidth

		if newY <= 0:
			newY = 0 
		elif newY >= HEIGHT - charHeight:
			newY = HEIGHT - charHeight

		self.sprite.set_position(newX, newY)

	def draw(self, window_surface):
		self.sprite.draw(window_surface)