# baddies.py

from random import randint
from sprite import *

def generateBaddies(char, map):
	noBaddies = map.copy()
	playerSprite = pygame.sprite.Sprite()

	x, y = char.sprite.get_position()
	no_zone = pygame.rect.Rect((x,y),(100,100))
	playerSprite.rect = no_zone
	noBaddies.add(playerSprite)

	baddies = pygame.sprite.Group()

	for b in range(1,10):
		posx, posy = randint(0,WIDTH), randint(0,HEIGHT)
		b = Sprite('../resources/baddie.png')
		b.set_position(posx, posy)
		if spritecollideany(b, noBaddies) == None:
			baddies.add(b)
			b += 1

	return baddies
