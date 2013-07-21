#baddy.py
import pygame
from sprite import *
from random import randint
from constants import *
from loadMap import * 
from baddies import *
class Baddy(Sprite):
	

	def __init__(self, filepath):
		Sprite.__init__(self, filepath)
		self.health = 10
		self.speed = randint(1,5)
		# self.direct = [0,0]
		self.direct = genDir()

	def update(self, window_surface, impassables):
		curX = self.rect.x
		curY = self.rect.y 
		# print curX
		# print curY
		# newX = curX + (2 * self.direct[0])
		# newY = curY + (2 * self.direct[1])
		newX = curX + (self.direct[0] * self.speed)
		newY = curY + (self.direct[1] * self.speed)
		if newX <= 0:
			newX = 0
			self.direct = genDir()
		elif newX >= WIDTH - self.rect.width:
			newX = WIDTH - self.rect.width
			self.direct = genDir()

		if newY <= 0:
			newY = 0
			self.direct = genDir()

		elif newY >= HEIGHT - self.rect.height:
			newY = HEIGHT -self.rect.height
			self.direct = genDir()

		self.set_position(newX, newY)
		# Detect any impassable objects or baddies
		if pygame.sprite.spritecollide(self, impassables(), False):
			self.set_position(curX, curY)
			self.direct = genDir()
		self.draw(window_surface)

	# def update(self, window_surface):
	# 	self.draw(window_surface)


def genDir():
		dir = WEST
		direction = randint(1,8)
		# print direction
		if direction == 1:
			dir = NORTH
		if direction == 2:
			# print WEST
			dir == WEST
		if direction == 3:
			dir = SOUTH
		if direction == 4:
			dir = EAST
		if direction == 5:
			dir = NORTH_EAST
		if direction == 6:
			dir = NORTH_WEST
		if direction == 7:
			dir = SOUTH_EAST
		if direction == 8:
			dir = SOUTH_WEST
		# print dir
		return dir