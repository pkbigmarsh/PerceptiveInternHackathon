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
from animatedSprite import *

from constants import *

## !! ----- Constants ----- !! ##

import loadMap
from loadMap import *
moveUp = False
moveDown = False
moveLeft = False
moveRight = False

## !! ----- Game Logic ----- !! ##
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Hackathon')

char = Character('../resources/char.png',10,10)
char.set_position(100,100)
sprite = AnimatedSprite('../resources/spriteSheet1.png', 5, 1)
sprite.play_row(0)

initTiles()
loadMap('../resources/map1.csv')

whiteColor = pygame.Color(255,255,255)
baddy = Baddies()
impass = impassables()
baddy.generateBaddies(char,impass)


print char.rect.width
print char.rect.height
while True:
	windowSurfaceObj.fill(whiteColor)
	
	drawTiles(windowSurfaceObj)

	drawItems(windowSurfaceObj)

	char.update(windowSurfaceObj)
	
	# baddy.update(windowSurfaceObj)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				moveDown = True
			if event.key == K_UP:
				moveUp = True
			if event.key == K_LEFT:
				moveLeft = True
			if event.key == K_RIGHT:
				moveRight = True
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_UP:
				moveUp = False
			if event.key == K_DOWN:
				moveDown = False
			if event.key == K_LEFT:
				moveLeft = False
			if event.key == K_RIGHT:
				moveRight = False
	if moveUp:
		char.move(NORTH, impass, baddy)
		# sprite.stop()
	if moveDown:
		char.move(SOUTH, impass, baddy)
		# sprite.stop()
	if moveLeft:
		char.move(WEST, impass, baddy)
		# sprite.stop()
	if moveRight:
		char.move(EAST, impass, baddy)
		# sprite.stop()
	baddy.refresh(windowSurfaceObj, impassables)
	baddy.draw(windowSurfaceObj)
	sprite.draw(windowSurfaceObj)
	pygame.display.update()
	fpsClock.tick(30)
