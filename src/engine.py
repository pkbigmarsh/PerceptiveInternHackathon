# engine.py
# https://github.com/pkbigmarsh/PerceptiveInternHackathon
#

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((800, 600))
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
