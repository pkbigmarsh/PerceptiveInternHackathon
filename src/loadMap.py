#
#
#
#

import pygame, sys
from pygame.locals import *

from constants import *

tileData = []
tileImages = dict()

def loadMap(filename):
	file = open(filename)

	lines = file.readlines()

	y = 0
	for line in lines:
		x = 0
		values = line.split(',')
		for char in values:
			if char in tileImages:
				newTile = {
				'rect': pygame.Rect(x, y, x + TILE_SIZE, y + TILE_SIZE),
				'surface': pygame.transform.scale(tileImages[char], (TILE_SIZE, TILE_SIZE)),
				'type': "grass"
				}
				tileData.append(newTile)
			if char == 'B':
				newTile = {
				'rect': pygame.Rect(x, y, x + TILE_SIZE, y + TILE_SIZE),
				'surface': pygame.transform.scale(tileImages[char], (TILE_SIZE, TILE_SIZE)),
				'type': "rock"
				}
				tileData.append(newTile)
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
