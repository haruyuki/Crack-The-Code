import glob
import os
import random
import collections

combinations_colour = []
combinations_number = []
instructions = 'Mastermind is a puzzle based game. Your goal is to break a 4-digit code, where each digit is different, in the fewest number of guesses.'
guesses_current = 0
b_dot = '•'
w_dot = '◦'
win = False

directory_colour = glob.glob(os.path.join('scores_colour', '*'))
for i in range(len(directory_colour)):
	combinations_colour.append(directory_colour[i][14:-4])

directory_number = glob.glob(os.path.join('scores_number', '*'))
for i in range(len(directory_number)):
	directory_number[i]
	combinations_number.append(directory_number[i][14:-4])


print('Welcome to Mastermind!')

while True:
	print('Would you like to view instructions? (Yes/No)')
	instructions_input = input('> ')
	yes = ['y', 'yes']
	no = ['n', 'no']
	if instructions_input.lower() in yes:
		print(instructions)
		break
	elif instructions_input.lower() in no:
		break
	else:
		print('Select an option!')

while False:
	print('Would you like to guess with colours or numbers? (Colour/Number)')
	selection_input = input('> ')
	colour = ['c', 'color', 'colour']
	number = ['n', 'num', 'number']
	if selection_input.lower() in colour:
		selection = 'colour'
		break
	elif selection_input.lower() in number:
		selection = 'number'
		break
	else:
		print('Select an option!')

selection = 'number'

code = random.choice(eval('combinations_' + selection))
code_split = list(code)

print('You have 10 guesses.')
print('An empty dot ( ◦ ) means a number is correct but is in the wrong position.')
print('A filled dot ( • ) means a number is correct and in the right position.')
print('Guess a 4-digit ' + selection)
if selection == 'colour':
	print('R O Y G B P')
elif selection == 'number':
	print('1 2 3 4 5 6 7 8 9')

while guesses_current < 10:
	d = collections.defaultdict(int)
	black_dots = 0
	white_dots = 0
	repeats = 0
	#print(guesses_current)
	code_guess = input('> ')
	for c in code_guess:
		d[c] += 1
	for i in range(9):
		if d[str(i + 1)] > 1:
			repeats += 1
	if repeats > 0:
		print('You can\'t use a number twice!')
	elif len(code_guess) < 4:
		print('You\'re missing ' + str((4 - len(code_guess))) + ' ' + selection + '(s)')
	elif len(code_guess) > 4:
		print('That\'s ' + str(len(code_guess) - 4) + ' ' + selection + '(s) too many!' )
	elif list(code_guess) == code_split:
		print('You got it!')
		win = True
		break
	else:
		code_guess_split = list(code_guess)
		for i in range(4):
			location = i + 1
			if code_guess_split[i] in code_guess:
				try:
					if [a for a, b in enumerate(code_split) if b == code_guess_split[i]][0] == i:
						black_dots += 1
					else:
						white_dots += 1
				except IndexError:
					pass
		print(b_dot * black_dots + w_dot * white_dots)
		guesses_current += 1

if win:
	print('You won!')
else:
	print('You lose...')
	print(code)



