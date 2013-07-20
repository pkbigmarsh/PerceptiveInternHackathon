#baddy.py

from sprite import Sprite
from random import randint

class baddy(Sprite):
	
	def __init__(self):
		pygame.sprite.Group.__init__(self)

