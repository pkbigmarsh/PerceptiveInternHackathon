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

pygame.font.init()
fontNormal = pygame.font.Font("../resources/font/Walkway rounded.ttf", 24)

box1 = TextBox(800 // 2 - 400 // 2, 600 // 2 - 32 // 2 + 00, 400, 32, fontNormal)
box1.value.string = "Thing 1"
box2 = TextBox(800 // 2 - 400 // 2, 600 // 2 - 32 // 2 + 64, 400, 32, fontNormal)
box2.value.string = "Thing 2"
box3 = TextBox(800 // 2 - 400 // 2, 600 // 2 - 32 // 2 + 128, 400, 32, fontNormal)
box3.value.string = "Thing 3"
box3.disabled = True

textBoxes = list()
textBoxes.append(box1)
textBoxes.append(box2)
textBoxes.append(box3)


initKeyStrings()

keyMap = dict()
keyPressed = list()
buttonDown = dict()
buttonDown[1] = False

pygame.key.set_mods(0)

while True:
	windowSurfaceObj.fill(BLACK)
	
	#drawTiles(windowSurfaceObj)

	drawItems(windowSurfaceObj)

	for box in textBoxes:
		box.draw(windowSurfaceObj)

	if buttonDown[1]:
		for box in textBoxes:
			box.mouseHeld(pygame.mouse.get_pos()[0])

	for key in keyPressed:
		keyMap[key] += 1
		if (keyMap[key]) > 15:
			if (keyMap[key] % 2) == 0:
				for box in textBoxes:
					box.keyEvent(key)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			for box in textBoxes:
				box.keyEvent(event.key)
			keyMap[event.key] = 0
			keyPressed.append(event.key)
		elif event.type == KEYUP:
			if event.key in keyPressed:
				keyPressed.remove(event.key)
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				for box in textBoxes:
					box.mouseDown(event.pos[0], event.pos[1])
			buttonDown[event.button] = True
		elif event.type == MOUSEBUTTONUP:
			buttonDown[event.button] = False

	pygame.display.update()

	fpsClock.tick(30)
