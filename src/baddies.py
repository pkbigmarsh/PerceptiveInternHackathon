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

	for i in range(1,10):
		posx, posy = randint(0,800), randint(0,600)
		b = Sprite('../resources/baddie.png')
		b.set_position(posx, posy)
		b.group = 0
		if pygame.sprite.spritecollideany(b, noBaddies) == None:
			baddies.add(b)
			i += 1

	return baddies
