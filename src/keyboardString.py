#	keyboardString.py
#	Used to get a string of text entered by the user

class keyboardString(Object):
	__init__():
		this.string = ""
		this.cursorPos = 0

	addKeyPress(keyCode):	#	THIS METHOD NOT DONE YET
		k = ""
		stringAsList = list(string)
		if key.get_mods() & KMOD_SHIFT != 0:
			if keyCode in ks:
				stringAsList[cursorPos:cursorPos] = ks[keyCode]
				string = "".join(stringAsList)
				return
			if keyCode in kn:
				stringAsList[cursorPos:cursorPos] = kn[keyCode]
				string = "".join(stringAsList)
				return
		else:
			if keyCode in kn:
				stringAsList[cursorPos:cursorPos] = kn[keyCode]
				string = "".join(stringAsList)
				return
		if keyCode == K_BACKSPACE:
			if cursorPos > 0:
				string = string[0:cursorPos - 1] + string[cursorPos:]
		elif keyCode == K_DELETE:
			string = string[0:cursorPos] + string[CursorPos + 1:]

	setCursorPosition(position):
		if position < 0:
			cursorPos = 0
		elif position > len(string):
			cursorPos = len(string)
		else:
			cursorPos = position

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

	kn[K_KP_PERIOD] = '.'
	kn[K_KP_ENTER] = '\n'
	kn[K_KP_PLUS] = '+'
	kn[K_KP_MINUS] = '-'
	kn[K_KP_MULTIPLY] = '*'
	kn[K_KP_DIVIDE] = '/'

