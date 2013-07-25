import pygame, sys
from pygame.locals import *
from sprite import Sprite
import constants
from item import *
from loadMap import *
import copy

def metaMap(levelName):
	file = open(levelName)
	print file
	lines = file.readlines()
	tempValues = []
	tempList = []
	values = []
	for line in lines:

		values.extend(line.split(','))
	x = 0
	y = 0
	for value in values:
		print value
		if value == '\n':
			y+=1
			# print tempList
			if tempList:
				tempValues.append(tempList)
			# print tempList
			# print tempValues
			tempList = []
			# print tempList
		elif value != '\n' or value != '': 
			tempList.append(value)
			x+=1

	print values
	# print values[0]
	# print '../resources/' + values[0] + '.csv'
	# print MAP
	print len(values)

	print tempValues
def loadNext(direct):
	file = open('../resources/level1.csv')
	# file = open(levelName)
	lines = file.readlines()
	tempValues = []
	tempList = []
	values = []
	for line in lines:
		line.replace('\n', '')
		values.extend(line.split(','))
	x = 0
	y = 0
	for value in values:
		# value.replace('\n','')
		print value
		if value == '\n':
			y+=1
			# print tempList
			if tempList:
				tempValues.extend(tempList)
			# print tempList
			# print tempValues
			del tempList[:]
			tempList[:] = []
			# print tempList
		elif value != '\n' and value != '': 
			tempList.append(value)
			x+=1
	print tempValues
	# values = tempValues
	# constants.MAP = constants.MAP + 1
	# if constants.MAP > 1:
	# 	constants.MAP = 0
	curMap = constants.MAP
	if direct == "left":
		constants.MAP -= 1
	if direct == "right":
		constants.MAP += 1
	if constants.MAP < 0:
		constants.MAP = curMap
	if constants.MAP > len(values):
		constants.MAP = curMap
	print constants.MAP
	# print values[0]
	# print '../resources/' + values[0] + '.csv'
	resource = '../resources/' + tempValues[constants.MAP] + '.csv'
	print resource
	# print tileData
	# clearMap()
	# print " "
	# print tileData
	loadMap(resource)