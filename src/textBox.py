#	textBox.py
#	Class defining a textbox ui element
#	that the user can interact with

import pygame, sys
from pygame.locals import *
from keyboardString import *
from constants import *

#textBoxIdCounter = 0
#textBoxes = WeakValueDictionary()	#	<-- Look at that awesomeness right there

class TextBox(object):
	def __init__(self, x, y, w, h, font):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.font = font
		self.value = keyboardString()
		self.drawFontOffset = (h - font.get_height()) / 2
		self.focused = False
		self.start = 0
		self.disabled = False

	def getCursorPositionFromPosition(self, x):
		#	Font metrics
		x -= self.x + 2
		ans = 0
		off = 0
		for size in self.font.metrics(self.value.string):
			if x < off + size[4] // 2:
				break
			off += size[4]
			ans += 1
		return ans


	def mouseDown(self, x, y):
		self.focused = False
		if not self.disabled:
			if (x > self.x and
				y > self.y and
				x < self.x + self.w and
				y < self.y + self.h):
				self.focused = True
				self.start = self.getCursorPositionFromPosition(x)


	def mouseHeld(self, x):
		if self.focused:
			self.value.setSelection(self.start, self.getCursorPositionFromPosition(x))

	def keyEvent(self, keyCode):
		if self.focused:
			self.value.addKeyPress(keyCode)

	def getString(self):
		return self.value.string

	def draw(self, surface):
		if self.disabled:
			backgroundColor = TEXTBOX_BACKGROUND_DISABLED
			textColor = TEXTBOX_TEXT_DISABLED
		elif self.focused:
			backgroundColor = TEXTBOX_BACKGROUND_FOCUSED
			textColor = TEXTBOX_TEXT_FOCUSED
		else:
			backgroundColor = TEXTBOX_BACKGROUND
			textColor = TEXTBOX_TEXT

		surface.fill(backgroundColor, Rect(self.x, self.y, self.w, self.h))
		pygame.draw.rect(surface, TEXTBOX_BORDER, Rect(self.x, self.y, self.w, self.h), 1)

		text = self.font.render(self.getString(), True, textColor, backgroundColor)
		surface.blit(text, (self.x + 2, self.y + self.drawFontOffset))
		
		if self.focused:
			cursorStart = self.font.size(self.value.string[:self.value.start])[0]
			cursorEnd = self.font.size(self.value.string[:self.value.end])[0] + 1
			surface.fill(TEXTBOX_SELECTED, Rect(
				cursorStart + self.x + 2,
				self.y + self.drawFontOffset - 1,
				cursorEnd - cursorStart,
				self.font.get_height() + 1), BLEND_ADD)
