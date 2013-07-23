#	keyboardString.py
#	Used to get a string of text entered by the user

class keyboardString(Object):
	def __init__():
		this.string = ""
		this.start = 0
		this.end = 0
		this.cursor = 0

	def addKeyPress(keyCode):	#	THIS METHOD NOT DONE YET

		if key.get_mods() & KMOD_CTRL != 0:
			k = ""
			if (key.get_mods() & KMOD_SHIFT != 0):
				if keyCode in ks:
					k = ks[keyCode]
				if keyCode in kn:
					k = kn[keyCode]
			else:
				if keyCode in kn:
					k = kn[keyCode]
			if k != "":
				string = string[0:start] + [k] + string[end:]
				start += 1
				cursor = end = start
				return

		if keyCode == K_BACKSPACE:
			if start == end:
				string = string[0:start - 1] + string[end:]
				start -= 1
				cursor = end = start
			else:
				string = string[0:start] + string[end:]
				cursor = end = start
		elif keyCode == K_DELETE:
			if start == end:
				string = string[0:start] + string[end + 1:]
			else:
				string = string[0:start] + string[end:]
				cursor = end = start


		elif keyCode == K_RIGHT:
			if key.get_mods() & KMOD_SHIFT != 0:
				if start == end:
					end += 1
					if end > len(string):
						end = len(string)
					cursor = end
				else:
					if cursor == start:
						start += 1
						cursor = start
					else:
						end += 1
						if end > len(string):
							end = len(string)
						cursor = end
			else:
				if start == end:
					start += 1
					cursor = end = start
				else:
					cursor = start = end


		elif keyCode == K_LEFT:
			if key.get_mods() & KMOD_SHIFT != 0:
				if start == end:
					start -= 1
					if (start < 0):
						start = 0
					cursor = start
				else:
					if cursor == start:
						start -= 1
						if (start < 0):
							start = 0
						cursor = start
					else:
						start += 1
						cursor = end
			else:
				if start == end:
					start += 1
					cursor = end = start
				else:
					cursor = start = end

		elif keyCode == K_c && (key.get_mods() & KMOD_CTRL != 0):
			#	TODO copy text
		elif keyCode == K_v && (key.get_mods() & KMOD_CTRL != 0):
			#	TODO paste text
		elif keyCode == K_x && (key.get_mods() & KMOD_CTRL != 0):
			#	TODO cut text

	def setCursorPosition(position):
		if position < 0:
			cursor = start = end = 0
		elif position > len(string):
			cursor = start = end = len(string)
		else:
			cursor = start = end = position

	def setSelection(startDrag, endDrag):
		if endDrag > startDrag:
			start = startDrag
			end = endDrag
		else:
			start = endDrag
			end = startDrag
		if start < 0:
			start = 0
		if end > len(string):
			end = len(string)
		if endDrag > startDrag:
			cursor = end
		else:
			cursor = start

kn = dict()
ks = dict()

def initKeyStrings:
	for charValue in range(K_a, K_z):
		kn[charValue] = chr(charValue)
		ks[charValue] = char(charValue - 32)
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

	kn[K_ENTER] = '\n'
	kn[K_TAB] = '\t'

	kn[K_KP_PERIOD] = '.'
	kn[K_KP_ENTER] = '\n'
	kn[K_KP_PLUS] = '+'
	kn[K_KP_MINUS] = '-'
	kn[K_KP_MULTIPLY] = '*'
	kn[K_KP_DIVIDE] = '/'
