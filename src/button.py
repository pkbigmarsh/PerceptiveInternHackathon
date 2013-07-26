#	button.py
#	Class defining a button

import pygame, sys
from pygame.locals import *
from constants import *

def noOp(caller):
	pass

class Button(object):
	def __init__(self, x, y, w, h, label, font):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.label = label
		self.font = font
		self.disabled = False
		self.onPush = noOp
		self.selected = False
		self.pressed = False
		self.hover = False

	def mouseDown(self, x, y):
		self.selected = False
		self.pressed = False
		if not self.disabled:
			if self.hover:
				self.selected = True
				self.pressed = True

	def mouseMove(self, x, y):
		if not self.disabled:
			self.pressed = False
			self.hover = False
			if (x > self.x and
				y > self.y and
				x < self.x + self.w and
				y < self.y + self.h):
				self.hover = True
				if self.selected:
					self.pressed = True

	def mouseUp(self):
		if self.pressed:
			self.onPush(self)
		self.selected = False
		self.pressed = False

	def draw(self, surface):
		backgroundColor = BUTTON_BACKGROUND
		textColor = BUTTON_TEXT
		tlColor = BUTTON_BORDER_BRIGHT
		brColor = BUTTON_BORDER_DARK
		if self.disabled:
			backgroundColor = BUTTON_BACKGROUND_DISABLED
			textColor = BUTTON_TEXT_DISABLED
		elif self.pressed:
			backgroundColor = BUTTON_BACKGROUND_PRESSED
			textColor = BUTTON_TEXT_PRESSED
			tlColor = BUTTON_BORDER_DARK
			brColor = BUTTON_BORDER_BRIGHT
		elif self.hover:
			textColor = BUTTON_TEXT_HOVER

		surface.fill(tlColor, (self.x, self.y, self.w, 1))
		surface.fill(tlColor, (self.x, self.y, 1, self.h))
		surface.fill(brColor, (self.x + self.w, self.y, 1, self.h))
		surface.fill(brColor, (self.x, self.y + self.h, self.w, 1))

		surface.fill(backgroundColor, (self.x + 1, self.y + 1, self.w - 2, self.h - 2))

		text = self.font.render(self.label, True, textColor, backgroundColor)
		surface.blit(text, (self.x + self.w // 2 - self.font.size(self.label)[0] // 2, self.y + self.h // 2 - self.font.size(self.label)[1] // 2))
