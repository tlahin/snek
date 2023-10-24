
import pygame

# Renders score at the bottom of the screen, updates it in real time
def score_board(window_data, score, difficulty_settings):

	# Text font
	board_font = pygame.font.SysFont('Arial', 80)

	# Content
	score_surface = board_font.render('Points: ' + str(score), True, ('black'))
	difficulty_surface = board_font.render('Difficulty: ' + str(difficulty_settings.difficulty), True, ('black'))

	# Board rect
	score_rect = pygame.Rect(5, 705, 800, 700)
	difficulty_rect = pygame.Rect(600, 705, 500, 700)

	# Draws the rect with the content
	window_data.window.blit(score_surface, score_rect)
	window_data.window.blit(difficulty_surface, difficulty_rect)

def render(snek_data, window_data, difficulty_settings, colour_settings, wall, snack, power_up, exit_button, score):

	# Rendering snake
	for pos in snek_data.body:
		pygame.draw.rect(window_data.window, colour_settings.snek_colour, pygame.Rect(pos[0], pos[1], snek_data.block_size, snek_data.block_size))

	# Rendering snack
	pygame.draw.rect(window_data.window, colour_settings.food_colour, pygame.Rect(snack.cords[0], snack.cords[1], snack.size, snack.size))

	# Rendering power_up
	pygame.draw.rect(window_data.window, colour_settings.power_up_colour, pygame.Rect(power_up.cords[0], power_up.cords[1], power_up.size, power_up.size))

	# Rendering wall
	for pos in wall.cords:
		pygame.draw.rect(window_data.window, colour_settings.wall_colour, pygame.Rect((pos[0], pos[1]), (wall.size, wall.size)))

	# Breaks the loops and shows end screen when pressed
	if exit_button.draw(window_data.window):
		dead = True

	# Displays the score and difficulty
	score_board(window_data, score, difficulty_settings)