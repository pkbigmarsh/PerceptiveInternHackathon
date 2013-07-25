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
fontNormal = pygame.font.Font("../resources/font/Walkway rounded.ttf", 24)
box1 = TextBox(0, 0, 400, 32, fontNormal)
box1.value.string = "Bla bla"

initKeyStrings()

keyMap = dict()
keyPressed = list()
buttonDown = dict()
buttonDown[1] = False

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
		elif event.type == KEYDOWN:
			box1.keyEvent(event.key)
			keyMap[event.key] = 0
			keyPressed.append(event.key)
		elif event.type == KEYUP:
			if event.key in keyPressed:
				keyPressed.remove(event.key)
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				box1.mouseDown(event.pos[0], event.pos[1])
			buttonDown[event.button] = True
		elif event.type == MOUSEBUTTONUP:
			buttonDown[event.button] = False


	pygame.display.update()

	if buttonDown[1]:
		box1.mouseHeld(pygame.mouse.get_pos()[0])

	for key in keyPressed:
		keyMap[key] += 1
		if (keyMap[key]) > 15:
			if (keyMap[key] % 2) == 0:
				box1.keyEvent(key)

	fpsClock.tick(30)
