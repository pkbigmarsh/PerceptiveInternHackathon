# engine.py
# https://github.com/pkbigmarsh/PerceptiveInternHackathon
#

## !! ----- Import Statements ----- !! ##
import pygame, sys
from pygame.locals import *

## !! ----- Constants ----- !! ##
FRAME_RATE = 30
SCREEN_SIZE = WIDTH, HEIGHT = 800, 400

## !! ----- Game Logic ----- !! ##
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Hackathon')

charImg = pygame.image.load('./resources/char.png')
charRect = charImg.get_rect()
charx, chary = 0, 0

whiteColor = pygame.Color(255,255,255)

while True:
	windowSurfaceObj.fill(whiteColor)
	
	windowSurfaceObj.blit(charImg, (charx, chary))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			print 'nothing here yet'
			#if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
				# TODO: move sprite

	pygame.display.update()
	fpsClock.tick(30)
