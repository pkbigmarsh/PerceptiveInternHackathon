import pygame
from sprite import *

class Character:
	def __init__(self):
		self.sprite = Sprite('../resources/char.png')
		self.health = 10
		self.speed = 5

	def move(self, direction):
		self.sprite.move(direction[0] * self.speed, direction[1] * self.speed)

	def draw(self, window_surface):
		self.sprite.draw(window_surface)