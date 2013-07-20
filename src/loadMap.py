#
#
#
#

import pygame, sys
from pygame.locals import *

tileData = []
tileImages = dict()

def loadMap(filename):
	file = open(filename)

	lines = file.readlines()

	y = 0
	for line in lines:
		x = 0
		for char in line:
			if char == '#':
				newTile = {
				'rect': pygame.Rect(x, y, x + 20, y + 20),
				'surface': pygame.transform.scale(tileImages[char], (20, 20)),
				'type': "grass"
				}
				tileData.append(newTile)
			if char == ' ':
				newTile = {
				'rect': pygame.Rect(x, y, x + 20, y + 20),
				'surface': pygame.transform.scale(tileImages[char], (20, 20)),
				'type': "rock"
				}
				tileData.append(newTile)
			x += 20
		y += 20

def drawTiles(surface):
	for tile in tileData:
		surface.blit(tile['surface'], tile['rect'])

def initTiles():
	tileImages['#'] = pygame.image.load('../resources/white.png')
	tileImages[' '] = pygame.image.load('../resources/black.png')
