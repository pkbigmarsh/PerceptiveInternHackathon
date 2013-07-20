# engine.py
# https://github.com/pkbigmarsh/PerceptiveInternHackathon
#

## !! ----- Import Statements ----- !! ##
import pygame, sys
from pygame.locals import *
from sprite import *
from collision import *

## !! ----- Constants ----- !! ##
FRAME_RATE = 30
SCREEN_SIZE = WIDTH, HEIGHT = 800, 400
TILE_SIZE = 20

## !! ----- Game Logic ----- !! ##
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Hackathon')

char = Sprite('../resources/char.png')
char.rect.x = 0
char.rect.y = 0

whiteColor = pygame.Color(255,255,255)

while True:
	windowSurfaceObj.fill(whiteColor)
	
	char.draw(windowSurfaceObj)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
				char.rect.x = char.rect.x + TILE_SIZE

	pygame.display.update()
	fpsClock.tick(30)
