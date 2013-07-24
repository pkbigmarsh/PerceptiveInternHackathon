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
from metaMap import *
from constants import *
from loadMap import *
from textBox import *

## !! ----- Game Logic ----- !! ##
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Map Editor')

initTiles()

whiteColor = pygame.Color(255,255,255)

pygame.font.init()
fontNormal = pygame.font.Font("../resources/font/Grantham Roman.ttf", 24)
box1 = TextBox(0, 0, 400, 32, fontNormal)
box1.value.string = "Bla bla"

initKeyStrings()

keyMap = dict()
keyPressed = list()

pygame.key.set_mods(0)

while True:
	windowSurfaceObj.fill(whiteColor)
	
	drawTiles(windowSurfaceObj)

	drawItems(windowSurfaceObj)

	box1.draw(windowSurfaceObj)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			box1.keyEvent(event.key)
			keyMap[event.key] = 0
			keyPressed.append(event.key)
		if event.type == KEYUP:
			if event.key in keyPressed:
				keyPressed.remove(event.key)
			
	pygame.display.update()

	for key in keyPressed:
		keyMap[key] += 1
		if (keyMap[key]) > 15:
			if (keyMap[key] % 2) == 0:
				box1.keyEvent(key)

	fpsClock.tick(30)
