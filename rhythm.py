import random
import sys

# symbols for accents, ghosts notes, and barlines
accSym = '>'
ghostSym = '.'
barSym = ' | '

# by default, there are 4 beats to a measure, but 1st argument changes this
beats = 4
if len(sys.argv) > 1:
	beats = int(sys.argv[1])

# by default, 16th notes. 2nd argument changes notes per beat
notesPerBeat = 4
if len(sys.argv) == 3:
	notesPerBeat = int(sys.argv[2])

# loop for within one beat
for beat in range(beats):

	# begin with line break
	if beat % 4 == 0:
		print('\n\n|', end = '')

	# generate a random integer
	# in binary, it will be as many digits as there are notes in a beat
	rand = random.randint(0, 2**notesPerBeat - 1)

	# convert the integer into a binary string
	# 1's will be replaced with '>'
	# 0's will be replaced with '.'
	binStr = bin(rand).replace("0b","")
	binStr = binStr.replace("1",accSym)
	binStr = binStr.replace("0",ghostSym)
	padLen =  notesPerBeat - len(binStr)
	padStr = ""
	for x in range(padLen):
		padStr = padStr + ghostSym
	print(padStr + binStr, end = barSym)
print('\n')