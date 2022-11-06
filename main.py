"""

SNAKE GAME PROJECT

working on:

	options menu and its features
	over all structure

todo:

	Add walls the snake has to avoid or else it dies
	Options/Settings? colours, speed, screen size etc...
	Score?
	AI to play the game itself?

	WHEN KYS DO END SCREEN

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

"""

import pygame

from classes import *
from game import *
from options import *

pygame.init()

# Window init
pygame.display.set_caption("Epic Game")

# Window struct, carries width, height and the window surface
window_data = create_window_stuct(1300, 800)

# Main menu background
bg_main_menu = create_background(window_data.width, window_data.height, 'aquamarine2')

# Fonts
fontsmall = pygame.font.SysFont('Arial', 40)
fontbig = pygame.font.SysFont('Arial', 80)

# Main menu buttons
start_button = text_button(window_data.width / 2 - 100 / 2, window_data.height / 2 - 55, 100, 50, "START", pygame.font.SysFont(None, 50))
options_button = text_button(window_data.width / 2 - 100 / 2, window_data.height / 2, 100, 50, "OPTIONS", pygame.font.SysFont(None, 50))
quit_button = text_button(window_data.width / 2 - 100 / 2, window_data.height / 2 + 55, 100, 50, "QUIT", pygame.font.SysFont(None, 50))

# Settings struck: (snek, background, food)
colour_settings = create_colour_settings(('black'), ('gray'), ('red'))

# Snek struct: (speed, block size, head cords, body cords)
snek_data = create_snek_struct(10, 10, [510, 500], [[510, 500], [520, 500], [530, 500]])

running = True

# Menu loop
while running:

	window_data.window.blit(bg_main_menu.surface, (0, 0))

	# Main menu title
	main_menu = fontbig.render('Main Menu', True , ('black'))
	window_data.window.blit(main_menu, (window_data.width / 2 - 200, window_data.height / 2 - 200))

	if start_button.draw(window_data.window):
		reset_data(snek_data)
		play(snek_data, colour_settings, window_data)
	
	if options_button.draw(window_data.window):
		options(snek_data, colour_settings, window_data)

	if quit_button.draw(window_data.window):
		pygame.quit()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()