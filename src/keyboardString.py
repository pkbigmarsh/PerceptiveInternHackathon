#	keyboardString.py
#	Used to get a string of text entered by the user
import pygame, sys
from pygame.locals import *
from Tkinter import Tk

class keyboardString(object):
	def __init__(self):
		self.string = ""
		self.start = 0
		self.end = 0
		self.cursor = 0

	def addKeyPress(self, keyCode):	#	THIS METHOD NOT DONE YET
		keyMods = pygame.key.get_mods()
		if keyMods & KMOD_CTRL == 0:
			k = ""
			if (keyMods & KMOD_SHIFT != 0):
				if keyCode in ks.keys():
					k = ks[keyCode]
				elif keyCode in kn.keys():
					k = kn[keyCode]
			else:
				if keyCode in kn.keys():
					k = kn[keyCode]
			if len(k) > 0:
				self.string = self.string[0:self.start] + k + self.string[self.end:]
				self.start += 1
				self.cursor = self.end = self.start
				return

		if keyCode == K_BACKSPACE:
			if self.start == self.end:
				if self.start != 0:
					self.string = self.string[0:self.start - 1] + self.string[self.end:]
					self.start -= 1
					if self.start < 0:
						self.start = 0
					self.cursor = self.end = self.start
			else:
				self.string = self.string[0:self.start] + self.string[self.end:]
				self.cursor = self.end = self.start
		elif keyCode == K_DELETE:
			if self.start == self.end:
				self.string = self.string[0:self.start] + self.string[self.end + 1:]
			else:
				self.string = self.string[0:self.start] + self.string[self.end:]
				self.cursor = self.end = self.start


		elif keyCode == K_RIGHT:
			if keyMods & KMOD_SHIFT != 0:
				if self.start == self.end:
					self.end += 1
					if self.end > len(self.string):
						self.end = len(self.string)
					self.cursor = self.end
				else:
					if self.cursor == self.start:
						self.start += 1
						self.cursor = self.start
					else:
						self.end += 1
						if self.end > len(self.string):
							self.end = len(self.string)
						self.cursor = self.end
			else:
				if self.start == self.end:
					self.start += 1
					if self.start > len(self.string):
						self.start = len(self.string)
					self.cursor = self.end = self.start
				else:
					self.cursor = self.start = self.end


		elif keyCode == K_LEFT:
			if keyMods & KMOD_SHIFT != 0:
				if self.start == self.end:
					self.start -= 1
					if (self.start < 0):
						self.start = 0
					self.cursor = self.start
				else:
					if self.cursor == self.start:
						self.start -= 1
						if (self.start < 0):
							self.start = 0
						self.cursor = self.start
					else:
						self.start += 1
						self.cursor = self.end
			else:
				if self.start == self.end:
					self.start -= 1
					if (self.start < 0):
						self.start = 0
					self.cursor = self.end = self.start
				else:
					self.cursor = self.end = self.start

		elif keyCode == K_HOME:
			if keyMods & KMOD_SHIFT != 0:
				self.start = 0
			else:
				self.cursor = self.end = self.start = 0

		elif keyCode == K_END:
			if keyMods & KMOD_SHIFT != 0:
				self.end = len(self.string)
			else:
				self.cursor = self.start = self.end = len(self.string)

		elif keyCode == K_c and (keyMods & KMOD_CTRL != 0):
			tk = Tk()
			tk.withdraw()
			tk.clipboard_clear()
			tk.clipboard_append(self.string[self.start:self.end])
			tk.destroy()

		elif keyCode == K_v and (keyMods & KMOD_CTRL != 0):
			tk = Tk()
			tk.withdraw()
			clipboard = tk.selection_get(selection = "CLIPBOARD")
			tk.destroy()
			self.string = self.string[:self.start] + clipboard + self.string[self.end:]
			self.cursor = self.start = self.end + len(clipboard)

		elif keyCode == K_x and (keyMods & KMOD_CTRL != 0):
			tk = Tk()
			tk.withdraw()
			tk.clipboard_clear()
			tk.clipboard_append(self.string[self.start:self.end])
			tk.destroy()
			self.string = self.string[:self.start] + self.string[self.end:]


	def setCursorPosition(self, position):
		if position < 0:
			self.cursor = self.start = self.end = 0
		elif position > len(self.string):
			self.cursor = self.start = self.end = len(self.string)
		else:
			self.cursor = self.start = self.end = position

	def setSelection(self, startDrag, endDrag):
		if endDrag > startDrag:
			self.start = startDrag
			self.end = endDrag
		else:
			self.start = endDrag
			self.end = startDrag
		if self.start < 0:
			self.start = 0
		if self.end > len(self.string):
			self.end = len(self.string)
		if endDrag > startDrag:
			self.cursor = self.end
		else:
			self.cursor = self.start

kn = dict()
ks = dict()

def initKeyStrings():
	for charValue in range(K_a, K_z):
		kn[charValue] = chr(charValue)
		ks[charValue] = chr(charValue - 32)
	for charValue in range(K_0, K_9):
		kn[charValue] = chr(charValue)
	for charValue in range(K_KP0, K_KP9):
		kn[charValue] = chr(charValue - 208)

	ks[K_0] = ')'
	ks[K_1] = '!'
	ks[K_2] = '@'
	ks[K_3] = '#'
	ks[K_4] = '$'
	ks[K_5] = '%'
	ks[K_6] = '^'
	ks[K_7] = '&'
	ks[K_8] = '*'
	ks[K_9] = '('

	kn[K_COMMA] = chr(K_COMMA)
	ks[K_COMMA] = '<'
	kn[K_PERIOD] = chr(K_PERIOD)
	ks[K_PERIOD] = '>'
	kn[K_SLASH] = chr(K_SLASH)
	ks[K_SLASH] = '?'
	kn[K_SEMICOLON] = chr(K_SEMICOLON)
	ks[K_SEMICOLON] = ':'
	kn[K_QUOTE] = chr(K_QUOTE)
	ks[K_QUOTE] = '"'
	kn[K_LEFTBRACKET] = chr(K_LEFTBRACKET)
	ks[K_LEFTBRACKET] = '{'
	kn[K_RIGHTBRACKET] = chr(K_RIGHTBRACKET)
	ks[K_RIGHTBRACKET] = '}'
	kn[K_BACKSLASH] = chr(K_BACKSLASH)
	ks[K_BACKSLASH] = '|'
	kn[K_MINUS] = chr(K_MINUS)
	ks[K_MINUS] = '_'
	kn[K_EQUALS] = chr(K_EQUALS)
	ks[K_EQUALS] = '+'
	kn[K_BACKQUOTE] = chr(K_BACKQUOTE)
	ks[K_BACKQUOTE] = '~'

	kn[K_RETURN] = '\n'
	kn[K_TAB] = '\t'
	kn[K_SPACE] = ' '

	kn[K_KP_PERIOD] = '.'
	kn[K_KP_ENTER] = '\n'
	kn[K_KP_PLUS] = '+'
	kn[K_KP_MINUS] = '-'
	kn[K_KP_MULTIPLY] = '*'
	kn[K_KP_DIVIDE] = '/'
