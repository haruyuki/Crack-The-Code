# Smash the Code with GUI
# Pekotaro
# Puppy Pug Studios
# Codes of Dustfall
# The Lucky Fox Inn
'''
From the outside it looks modest, clean and snug. Softwood and intricate wooden carvings make up most of the building's outer structure.
It's impossible to see through the large, stained glass windows, but the happiness and joy from within can be felt outside.

As you enter the tavern through the heavy, wooden door, you're welcomed by dancing people and clapping hands.
The bartender is working up a sweat, but still manages to welcome you with a wink.

It's as lovely inside as it is on the outside. Hardwooden beams support the upper floor and the torches attached to them. The walls are packed with rows of painted portraits. You recognize the bartender on one of them, so the others must be either friends, family or previous owners..

The tavern itself is packed. Soldiers seem to be the primary clientele here, which often leads to exciting evenings. Several long tables are occupied by happy, excited groups of people, some are dancing on the table, while others cheer them on with clapping and yelling. The other, smaller tables are also occupied by people who are clearly having a good time. Even most of the stools at the bar are occupied, though nobody seems to mind more company.

You did hear rumors about this tavern, supposedly it's famous for something, but you can't remember what for. Though judging by the amount of women in this tavern and the amount of them trying to subtly eye the bartender, it's probably his good looks and charm. You manage to find a seat and prepare for what will undoubtedbly be a great evening.
'''

# -------------------- IMPORTS --------------------
import pygame
import glob
import os
import random
import collections
import sys

# -------------------- PYGAME VARIABLE SETUP --------------------
FPS = 60
window_width = 1280
window_height = 720

# -------------------- COLOURS --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -------------------- VARIABLES --------------------
combinations_colour = []
combinations_number = []
instructions = 'Mastermind is a puzzle based game. Your goal is to break a 4-digit code, where each digit is different, in the fewest number of guesses.'
guesses_current = 0

# -------------------- CODE COMBINATIONS --------------------
directory_colour = glob.glob(os.path.join('scores_colour', '*'))
for i in range(len(directory_colour)):
	combinations_colour.append(directory_colour[i][14:-4])

directory_number = glob.glob(os.path.join('scores_number', '*'))
for i in range(len(directory_number)):
	directory_number[i]
	combinations_number.append(directory_number[i][14:-4])

# -------------------- SCENE BASE --------------------


class SceneBase:  # Base template for all scenes
	def __init__(self):
		self.next = self

	def ProcessInput(self, events, pressed_keys):  # This method will receive all the events that happened since the last frame
		print("uh-oh, you didn't override this in the child class")

	def Update(self):  # Put your game logic in here for the scene
		print("uh-oh, you didn't override this in the child class")

	def Render(self, screen):  # Put your render code here. It will receive the main screen Surface as input
		print("uh-oh, you didn't override this in the child class")

	def SwitchToScene(self, next_scene):  # Function to switch to another scene
		self.next = next_scene

	def Terminate(self):
		self.SwitchToScene(None)

# -------------------- SCENE BASE TEMPLATE --------------------

'''
class XScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			pass

	def Update(self):
		pass

	def Render(self, screen):
		pass
'''
# -------------------- ANIMATION FUNCTIONS --------------------


# -------------------- FUNCTIONS --------------------


def blit_text(surface, text, pos, font, max_width, max_height):
	words = [word.split(' ') for word in text.splitlines()]
	space = font.size(' ')[0]
	x, y = pos
	for line in words:
		for word in line:
			word_surface = font.render(word, True, BLACK)
			word_width, word_height = word_surface.get_size()
			if x + word_width >= max_width:
				x = pos[0]
				y += word_height
			surface.blit(word_surface, (x, y))
			x += word_width + space
		x = pos[0]
		y += word_height

# -------------------- MAIN CODE --------------------


def run_game(width, height, fps, starting_scene):
	global background, logo, button, button_highlighted
	pygame.init()
	pygame.display.set_caption('Masterminds')

	button_font = pygame.font.Font('fonts/Herculanum.ttf', 20)
	sidebar_font = pygame.font.Font('fonts/TrajanPro3-Regular.otf', 20)

	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()

	active_scene = starting_scene

	background = pygame.image.load('backgrounds/title.png').convert_alpha()
	logo = pygame.image.load('logo.png').convert_alpha()
	button = pygame.image.load('button.png').convert_alpha()
	button_highlighted = pygame.image.load('button_highlighted.png').convert_alpha()

	while active_scene is not None:

		pressed_keys = pygame.key.get_pressed()

		# Event filtering
		filtered_events = []
		for event in pygame.event.get():
			quit_attempt = False
			if event.type == pygame.QUIT:
				quit_attempt = True
			elif event.type == pygame.KEYDOWN:
				alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
				if event.key == pygame.K_ESCAPE:
					quit_attempt = True
				elif event.key == pygame.K_F4 and alt_pressed:
					quit_attempt = True

			if quit_attempt:
				active_scene.Terminate()
			else:
				filtered_events.append(event)

		active_scene.ProcessInput(filtered_events, pressed_keys)
		active_scene.Update()
		active_scene.Render(screen)

		active_scene = active_scene.next

		pygame.display.flip()
		clock.tick(fps)




# -------------------- SCENES --------------------

class TitleScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.play_hover = False
		self.how_to_play_hover = False
		self.credits_hover = False
		self.quit_hover = False

		self.play_button = pygame.Rect(474, 276, 333, 68)
		self.how_to_play_button = pygame.Rect(474, 366, 333, 68)
		self.credits_button = pygame.Rect(474, 456, 333, 68)
		self.quit_button = pygame.Rect(474, 546, 333, 68)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if self.play_button.collidepoint(pygame.mouse.get_pos()):
				self.play_hover = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.SwitchToScene(SelectionScene())
			else:
				self.play_hover = False

			if self.how_to_play_button.collidepoint(pygame.mouse.get_pos()):
				self.how_to_play_hover = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.SwitchToScene(HowToPlayScene())
			else:
				self.how_to_play_hover = False

			if self.credits_button.collidepoint(pygame.mouse.get_pos()):
				self.credits_hover = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.SwitchToScene(CreditScene())
			else:
				self.credits_hover = False

			if self.quit_button.collidepoint(pygame.mouse.get_pos()):
				self.quit_hover = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.Terminate()
			else:
				self.quit_hover = False

	def Update(self):
		pass

	def Render(self, screen):
		screen.blit(background, (0, 0))
		screen.blit(logo, (517, 34))

		if self.play_hover:
			screen.blit(button_highlighted, (459, 261))
		else:
			screen.blit(button, (459, 261))

		if self.how_to_play_hover:
			screen.blit(button_highlighted, (459, 351))
		else:
			screen.blit(button, (459, 351))

		if self.credits_hover:
			screen.blit(button_highlighted, (459, 441))
		else:
			screen.blit(button, (459, 441))

		if self.quit_hover:
			screen.blit(button_highlighted, (459, 531))
		else:
			screen.blit(button, (459, 531))


class CreditScene(SceneBase):  # Base template for all scenes
	def __init__(self):
		self.next = self

	def ProcessInput(self, events, pressed_keys):  # This method will receive all the events that happened since the last frame
		pass

	def Update(self):  # Put your game logic in here for the scene
		pass

	def Render(self, screen):  # Put your render code here. It will receive the main screen Surface as input
		pass


class HowToPlayScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.play_hover = 0

		self.instructions_scene = pygame.image.load

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			pass

	def Update(self):
		pass

	def Render(self, screen):
		screen.fill(WHITE)


run_game(window_width, window_height, FPS, TitleScene())
pygame.quit()
sys.exit()
'''
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

while True:
	try:
		print('How many guesses do you want? (1 - 10)')
		guesses_input = input('> ')
		guesses = int(guesses_input)
		if guesses < 1:
			print('That number is too low!')
		elif guesses > 10:
			print('That number is too high!')
		else:
			break
	except ValueError:
		print('That\'s not a number!')

while True:
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

code = random.choice(eval('combinations_' + selection))
print(code)
code_split = list(code)

print('Guess a 4-digit ' + selection)
if selection == 'colour':
	print('R O Y G B P')
elif selection == 'number':
	print('1 2 3 4 5 6 7 8 9')

while guesses_current <= guesses:
	b_dot = '•'
	w_dot = '◦'
	d = collections.defaultdict(int)
	black_dots = 0
	white_dots = 0
	repeats = 0
	win = False
	print(guesses_current)
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
'''


