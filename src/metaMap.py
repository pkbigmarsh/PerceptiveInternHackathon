import pygame, sys
from pygame.locals import *
from sprite import Sprite
import constants
from item import *
from loadMap import *

def metaMap(levelName):
	file = open(levelName)
	lines = file.readlines()

	for line in lines:
		line = line.replace('\n', '')
		values = line.split(',')
	print values
	print values[0]
	print '../resources/' + values[0] + '.csv'
	print MAP
def loadNext(direct):
	file = open('../resources/level1.csv')
	lines = file.readlines()
	# print MAP
	# if direct == "left":
	# 	constants.MAP -= 1
	# if direct == "right":
	# 	constants.MAP += 1
	

	for line in lines:
		line = line.replace('\n', '')
		values = line.split(',')
	constants.MAP = constants.MAP + 1
	if constants.MAP > 1:
		constants.MAP = 0
	print constants.MAP
	# print values[0]
	# print '../resources/' + values[0] + '.csv'
	resource = '../resources/' + values[constants.MAP] + '.csv'
	# print tileData
	# clearMap()
	print " "
	# print tileData
	loadMap(resource)