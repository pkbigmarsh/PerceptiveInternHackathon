# baddies.py

from random import randint
from sprite import *
class baddies(pygame.sprite.Group):
	def __init__(self):
		pygame.sprite.Group.__init__(self)

	def generateBaddies(self, char, map):
		noBaddies = map.copy()
		playerSprite = pygame.sprite.Sprite()

		x, y = char.sprite.get_position()
		no_zone = pygame.rect.Rect((x,y),(100,100))
		playerSprite.rect = no_zone
		noBaddies.add(playerSprite)

		# baddies = pygame.sprite.Group()

		
		i = 1
		while i <= 10:
			b = Sprite('../resources/baddie.png')
			posx, posy = randint(0,800-b.rect.width), randint(0,600-b.rect.height)
			b.set_position(posx, posy)
			b.group = 0
			if pygame.sprite.spritecollideany(b, noBaddies) == None:
				self.add(b)
				i += 1

		return baddies

	def update(self, windowSurfaceObj):
		self.draw(windowSurfaceObj)