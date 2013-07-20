#baddy.py
import pygame
from sprite import *
from random import randint

class Baddy(Sprite):
	def __init__(self, filepath):
		Sprite.__init__(self, filepath)

	def move(self):
		self.sprite.move(*randint)