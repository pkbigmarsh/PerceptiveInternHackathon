#	Item class

from sprite import *

Items = list()

class Item(Sprite):
	def __init__(self, filepath):
		super(Item, self).__init__(filepath)
		Items.append(self)

def drawItems(surface):
	for item in Items:
		item.draw(surface)
