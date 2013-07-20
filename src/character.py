import pygame
from sprite import *
from constants import *

class Character:
	def __init__(self):
		self.sprite = Sprite('../resources/char.png')
		self.health = 10
		self.speed = 20

	def move(self, direction):
		#pos = self.sprite.getPosition()
		curX = self.sprite.rect.x
		curY = self.sprite.rect.y
		moveX = curX + (direction[0] * self.speed)
		moveY = curY + (direction[1] * self.speed)

		# Detect if near any edges/walls
		if moveX <= 0:
			moveX = 0
		elif moveX >= WIDTH - self.sprite.rect.width:
			moveX = WIDTH - self.sprite.rect.width

		if moveX <= 0:
			moveX = 0
		elif moveX >= WIDTH - self.sprite.rect.height:
			moveX = WIDTH - self.sprite.rect.height

		self.sprite.set_position(moveX, moveY)

	def draw(self, window_surface):
		self.sprite.draw(window_surface)