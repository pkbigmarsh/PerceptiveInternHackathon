#
#
#
#

import pygame, sys
from pygame.locals import *
from sprite import Sprite
from constants import *
from item import *

tileData = []
tileImages = dict()
impass = pygame.sprite.Group()

def loadMap(filename):
	del tileData[:]
	tileData[:] = []
	impass.empty()
	file = open(filename)

	lines = file.readlines()

	y = 0
	for line in lines:
		x = 0
		line = line.replace('\n', '')
		values = line.split(',')
		for value in values:
			parts = value.split(';')
			tilePart = parts[0]
			metadata = parts[1:]	#	The rest
			if tilePart in tileImages:
				newTile = {
				'rect': pygame.Rect(x, y, x + TILE_SIZE, y + TILE_SIZE),
				'surface': pygame.transform.scale(tileImages[tilePart], (TILE_SIZE, TILE_SIZE)),
				'type': "tile"
				}
				tileData.append(newTile)
				if tilePart == 'B':
					b = Sprite('../resources/bush.png')
					b.set_position(x, y)
					b.rect.width = 20 #height and width are not setting properly. not sure why
					b.rect.height = 20 
					impass.add(b)
				if tilePart == 'R':
					b = Sprite('../resources/rock.png')
					b.set_position(x, y)
					b.rect.width = 20
					b.rect.height = 20
					impass.add(b)
			if len(metadata) > 0:
				if metadata[0] == "player":
					#	TODO Move play here if the game just started
					pass
				elif metadata[0] == "baddy":
					#	TODO Put baddy here
					pass
				elif metadata[0] == "item":
					if metadata[1] == "coin":
						Item("../resources/coin.png").set_position(x, y)

			x += TILE_SIZE
		y += TILE_SIZE

def drawTiles(surface):
	for tile in tileData:
		surface.blit(tile['surface'], tile['rect'])

def initTiles():
	tileImages['#'] = pygame.image.load('../resources/white.png')
	tileImages[' '] = pygame.image.load('../resources/black.png')
	tileImages['G'] = pygame.image.load('../resources/grass.png')
	tileImages['R'] = pygame.image.load('../resources/rock.png')
	tileImages['B'] = pygame.image.load('../resources/bush.png')

def impassables():
	return impass
