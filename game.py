
import pygame
import random

def pause_game():

	paused = True

	while paused:
		for event in pygame.event.get():
			#if you exit the window during pause function it returns '1'
			if event.type == pygame.QUIT:
					return 1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					paused = False
					return False
	return True

# Grow snek
def grow_tail(snek_data):

	snek_data.snek_body.append([-10, -10])
	print("GROWS")

# Game loop
def play(snek_data, colour_settings, window_data):

	dead = False
	snack_spawned = False
	new_direction = 'LEFT'
	current_direction = new_direction
	fps = pygame.time.Clock()

	while not dead:

		fps.tick(snek_data.snek_speed)
		pygame.display.update()

		# Get inputs
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				dead = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					current_direction = 'UP'
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					current_direction = 'DOWN'
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					current_direction = 'LEFT'
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					current_direction = 'RIGHT'
				if event.key == pygame.K_SPACE:
					print("PAUSE")
					if pause_game() == 1:
						dead = True
					print("RESUME")
				# debug functionality | grows the snake when pressing 'g'
				if event.key == pygame.K_g:
					print("GROW")
					grow_tail(snek_data)

		# Prevents the snek from going backwards
		if current_direction == 'UP' and new_direction != 'DOWN':
			new_direction = 'UP'
		if current_direction == 'DOWN' and new_direction != 'UP':
			new_direction = 'DOWN'
		if current_direction == 'LEFT' and new_direction != 'RIGHT':
			new_direction = 'LEFT'
		if current_direction == 'RIGHT' and new_direction != 'LEFT':
			new_direction = 'RIGHT'

		# Moves the snek to the direction
		if new_direction == 'UP':
			snek_data.snek_head[1] -= snek_data.snek_block_size
		if new_direction == 'DOWN':
			snek_data.snek_head[1] += snek_data.snek_block_size
		if new_direction == 'LEFT':
			snek_data.snek_head[0] -= snek_data.snek_block_size
		if new_direction == 'RIGHT':
			snek_data.snek_head[0] += snek_data.snek_block_size

		# Checks if snek hits a wall and makes it come out the otherside
		if snek_data.snek_head[0] < 0:
			snek_data.snek_head[0] = window_data.width - snek_data.snek_block_size
		elif snek_data.snek_head[0] >= window_data.width:
			snek_data.snek_head[0] = 0
		if snek_data.snek_head[1] < 0:
			snek_data.snek_head[1] = window_data.height - snek_data.snek_block_size
		elif snek_data.snek_head[1] >= window_data.height:
			snek_data.snek_head[1] = 0

		# Set background colour
		window_data.window.fill(colour_settings.background_colour)

		# Add new snake block in the direction of movement and remove last block
		snek_data.snek_body.insert(0, list(snek_data.snek_head))
		snek_data.snek_body.pop()

		# Checks if theres an active food if not generates a new one within the window
		if snack_spawned == False:
			snack_pos = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 10) * 10]
			snack_spawned = True

		# Grow snek when colliding with food
		if snek_data.snek_head == snack_pos:
			grow_tail(snek_data)
			snack_spawned = False

		# Check for self collision
		if snek_data.snek_head in snek_data.snek_body[1::]:
			dead = True

        # Rendering snake and snacks
		for pos in snek_data.snek_body:
			pygame.draw.rect(window_data.window, colour_settings.snek_colour, pygame.Rect(pos[0], pos[1], snek_data.snek_block_size, snek_data.snek_block_size))

		pygame.draw.rect(window_data.window, colour_settings.food_colour, pygame.Rect(snack_pos[0], snack_pos[1], snek_data.snek_block_size, snek_data.snek_block_size))

	print("DEAD")