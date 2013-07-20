# engine.py
# https://github.com/pkbigmarsh/PerceptiveInternHackathon
#

## !! ----- Import Statements ----- !! ##
import pygame, sys
from pygame.locals import *
from sprite import *
from collision import *
from character import *
from baddies import *

# sys.path.append('./constants')

from constants import *

## !! ----- Constants ----- !! ##

import loadMap
from loadMap import *

## !! ----- Game Logic ----- !! ##
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Hackathon')

char = Character()

initTiles()
loadMap('../resources/map1.csv')

whiteColor = pygame.Color(255,255,255)

while True:
	windowSurfaceObj.fill(whiteColor)
	
	drawTiles(windowSurfaceObj)

	char.draw(windowSurfaceObj)
	
	generateBaddies(char,impassables()).draw(windowSurfaceObj)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
				char.move(EAST)

	pygame.display.update()
	fpsClock.tick(30)
