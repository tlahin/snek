
import pygame

def render(snek_data, window_data, colour_settings, wall, snack, power_up):

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
