"""

SNAKE GAME PROJECT

working on:

	options menu and its features
	over all structure

todo:

	Add walls the snake has to avoid or else it dies
	Powerups such as speed or immunity
	AI to play the game itself?

authors:
	tlahin
	Poks

Started:
	Oct 26, 2022

Controls:
	Move:
		'wasd' or arrow keys
	Pause/unpause:
		'space'

	debug:
		'g' to grow
		'h' to respawn food

"""

import pygame

import classes
import game
import options

pygame.init()

# Window init
pygame.display.set_caption("Epic Game")

# Window struct, carries width, height and the window surface
window_data = classes.window_stuct(1300, 800)

# Main menu background
bg_main_menu = classes.background(window_data.width, window_data.height, 'aquamarine2')

# Fonts
fontsmall = pygame.font.SysFont('Arial', 40)
fontbig = pygame.font.SysFont('Arial', 80)

# Main menu buttons
start_button = classes.text_button(window_data.width / 2 - 100 / 2, window_data.height / 2 - 55, 100, 50, "START", pygame.font.SysFont(None, 50))
options_button = classes.text_button(window_data.width / 2 - 100 / 2, window_data.height / 2, 100, 50, "OPTIONS", pygame.font.SysFont(None, 50))
quit_button = classes.text_button(window_data.width / 2 - 100 / 2, window_data.height / 2 + 55, 100, 50, "QUIT", pygame.font.SysFont(None, 50))

# Settings struck: (snek, background, food)
colour_settings = classes.colour_settings(('black'), ('gray'), ('red'))

# Snek struct: (speed, block size, head cords, body cords)
snek_data = classes.snek_struct(10, 10, [510, 500], [[510, 500], [520, 500], [530, 500]])

running = True

# Menu loop
while running:

	pygame.display.flip()

	# Main menu background
	window_data.window.blit(bg_main_menu.surface, (0, 0))

	# Main menu title
	main_menu = fontbig.render('Main Menu', True , ('black'))
	window_data.window.blit(main_menu, (window_data.width / 2 - 200, window_data.height / 2 - 200))

	# Start button to play the game | resets the game before playing
	if start_button.draw(window_data.window):
		game.reset_data(snek_data)
		game.play(snek_data, colour_settings, window_data)

	# Options button in main menu to open options menu
	if options_button.draw(window_data.window):
		options.options(snek_data, colour_settings, window_data)

	# Quit button to close the game
	if quit_button.draw(window_data.window):
		running = False
		pygame.quit()

	# Quits the program if you close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

pygame.quit()
