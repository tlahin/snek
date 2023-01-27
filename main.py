
# README.md :)

import pygame

import classes
import game
import options

pygame.init()

# Window init
pygame.display.set_caption("Epic Game")

# Window struct, carries width, height and the window surface
window_data = classes.window_stuct(1300, 800)

# Main menu background img
snek_img = pygame.image.load("./resources/snek_bg.png").convert_alpha()
snek_img = pygame.transform.scale(snek_img, (500, 400))

# Main menu background
bg_main_menu = classes.background(window_data.width, window_data.height, 'aquamarine2')

# Fonts
fontsmall = pygame.font.SysFont('Arial', 40)
fontbig = pygame.font.SysFont('Arial', 80)

# Main menu buttons
start_button = classes.text_button(window_data.width / 2 - 100, window_data.height / 2 - 55, 100, 50, "START", pygame.font.SysFont(None, 50))
options_button = classes.text_button(window_data.width / 2 - 100, window_data.height / 2, 100, 50, "OPTIONS", pygame.font.SysFont(None, 50))
quit_button = classes.text_button(window_data.width / 2 - 100, window_data.height / 2 + 55, 100, 50, "QUIT", pygame.font.SysFont(None, 50))

# Settings struct: (snek, background, food)
colour_settings = classes.colour_settings('white', 'black', 'green', 'red')

# Difficulty struct
difficulty_settings = classes.difficulty_settings('Normal')

# Snek struct: (speed, block size, head cords, body cords)
snek_data = classes.snek_struct(10, 10, [510, 500], [[510, 500], [520, 500], [530, 500]])

running = True

# Menu loop
while running:

	pygame.display.flip()

	# Main menu background
	window_data.window.blit(bg_main_menu.surface, (0, 0))
	window_data.window.blit(snek_img, (475, 180))

	# Main menu title
	snek_title = fontbig.render('SNEK', True , ('black'))
	title_rect = snek_title.get_rect(center=(window_data.width / 2, 100))
	window_data.window.blit(snek_title, title_rect)

	# Start button to play the game | resets the game before playing
	if start_button.draw(window_data.window):
		game.reset_data(snek_data)
		game.play(snek_data, colour_settings, window_data, difficulty_settings)

	# Options button in main menu to open options menu
	if options_button.draw(window_data.window):
		options.options(snek_data, colour_settings, window_data, difficulty_settings)

	# Quit button to close the game
	if quit_button.draw(window_data.window):
		running = False

	# Quits the program if you close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

pygame.quit()
