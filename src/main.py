## !! ----- Import Statements ----- !! ##
import pygame, sys
from pygame.locals import *

import ./constants/COLORS

## !! ----- Constants ----- !! ##
FRAME_RATE = 30
SCREEN_SIZE = WIDTH, HEIGHT = 800, 400

## !! ----- Load Graphics ----- !! ##


## !! ----- Set up the Screen ------ !! ##
pygame.init()
windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)


## !! ------ Main Loop ----- !! ##
while True:
	windowSurfaceObj.fill(WHITE)

	## !! ----- Event Handling ----- !! ##
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FRAME_RATE)