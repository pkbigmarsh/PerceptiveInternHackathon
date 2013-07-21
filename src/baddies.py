# baddies.py

from random import randint
from sprite import *
from baddy import *
from loadMap import *
import pygame
class Baddies(pygame.sprite.Group):
	def __init__(self):
		pygame.sprite.Group.__init__(self)

	def generateBaddies(self, char, map):
		noBaddies = map.copy()
		playerSprite = pygame.sprite.Sprite()

		x, y = char.get_position()
		no_zone = pygame.rect.Rect((x,y),(100,100))
		playerSprite.rect = no_zone
		noBaddies.add(playerSprite)

		# baddies = pygame.sprite.Group()

		
		i = 1
		while i <= 10:
			b = Baddy('../resources/baddie.png')
			posx, posy = randint(0,800-b.rect.width), randint(0,600-b.rect.height)
			b.set_position(posx, posy)
			b.width = 10
			b.height = 30
			b.group = 0
			if pygame.sprite.spritecollideany(b, noBaddies) == None and pygame.sprite.spritecollideany(b, self) == None:
				self.add(b)
				i += 1

		# return baddies
	def refresh(self, window_surface, impass):
		self.update(window_surface, impass)
		self.draw(window_surface)
	# def update(self, windowSurfaceObj):
	# 	# for i in len(self.sprites()):

	# 	self.draw(windowSurfaceObj)
	
