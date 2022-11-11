
import pygame

import classes
import game_objects

# Resets snek data to default starting position
def reset_data(snek_data):

	snek_data.head = [510, 500]
	snek_data.body = [[510, 500], [520, 500], [530, 500]]

def end_screen(window_data, score):

	# Go next button to return to main menu
	go_next_button = classes.text_button(window_data.width / 2 - 150 / 2, 550, 150, 75, "go next", pygame.font.SysFont('Arial', 40))

	# End screen background
	bg_end_menu = classes.background(window_data.width, window_data.height, 'aquamarine2')
	window_data.window.blit(bg_end_menu.surface, (0, 0))

	# End screen title to tilt the player
	end_title_font = pygame.font.SysFont('Arial', 80)
	end_title_surface = end_title_font.render("Don't be sorry, be better.", True, ('black'))
	end_title_rect = end_title_surface.get_rect()
	end_title_rect.midtop = (window_data.width / 2, window_data.height / 4 + 150)
	window_data.window.blit(end_title_surface, end_title_rect)

	# Shows the finals score at the end screen and trash talks the player
	end_score_font = pygame.font.SysFont('Arial', 80)
	end_score_font = end_score_font.render("Only got " + str(score) + " punttos ._.", True, ('black'))
	end_score_rect = end_score_font.get_rect()
	end_score_rect.midtop = (window_data.width / 2, window_data.height / 4)
	window_data.window.blit(end_score_font, end_score_rect)

	ended = False

	while not ended:

		pygame.display.update()

		# When clicked closes the end screen and returns to main menu
		if go_next_button.draw(window_data.window):
			ended = True

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				ended = True

# Pause game function
def pause_game(window_data, exit_button):

	paused = True

	while paused:

		if exit_button.draw(window_data.window):
			return 1
		for event in pygame.event.get():
			#if you exit the window during pause function it returns '1'
			if event.type == pygame.QUIT:
					return 1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					paused = False
					return False
	return True

# Renders score at the bottom of the screen, updates it in real time
def score_board(window_data, score):

	# Text font
	score_font = pygame.font.SysFont('Arial', 80)

	# Content
	score_surface = score_font.render('Punttos: ' + str(score), True, ('black'))

	# Board rect
	score_rect = pygame.Rect(5, 705, 1300, 700)

	# Draws the rect with the content
	window_data.window.blit(score_surface, score_rect)

# Grow snek
def grow_tail(snek_data):

	# Adds a new element to body list
	snek_data.body.append([-10, -10])

# Game loop
def play(snek_data, colour_settings, window_data):

	# Exit button and it's image
	exit_img = pygame.image.load("./resources/exit_button.png").convert_alpha()
	exit_img = pygame.transform.scale(exit_img, (50, 50))
	exit_button = classes.exit_button(1225, 725, exit_img)

	dead = False
	new_direction = 'LEFT'
	current_direction = new_direction
	fps = pygame.time.Clock()
	score = 0

	wall = game_objects.spawn_wall(snek_data, window_data)
	snack = game_objects.spawn_snack(snek_data, window_data, wall)

	while not dead:

		fps.tick(snek_data.speed)
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
					if pause_game(window_data, exit_button) == 1:
						dead = True
				# debug functionality | grows the snake when pressing 'g'
				if event.key == pygame.K_g:
					score += 1
					grow_tail(snek_data)
				# debug functionality | respawns food when pressing 'h'
				if event.key == pygame.K_h:
					snack.spawned = False
				# debug functionaluty | respawns the wall when pressing 'j'
				if event.key == pygame.K_j:
					wall = game_objects.spawn_wall(snek_data, window_data)

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
			snek_data.head[1] -= snek_data.block_size
		if new_direction == 'DOWN':
			snek_data.head[1] += snek_data.block_size
		if new_direction == 'LEFT':
			snek_data.head[0] -= snek_data.block_size
		if new_direction == 'RIGHT':
			snek_data.head[0] += snek_data.block_size

		# Checks if snek hits a wall and makes it come out the otherside
		if snek_data.head[0] < 0:
			snek_data.head[0] = window_data.game_width - snek_data.block_size
		elif snek_data.head[0] >= window_data.game_width:
			snek_data.head[0] = 0
		if snek_data.head[1] < 0:
			snek_data.head[1] = window_data.game_height - snek_data.block_size
		elif snek_data.head[1] >= window_data.game_height:
			snek_data.head[1] = 0

		# Set background colour
		window_data.window.fill(colour_settings.background_colour, pygame.Rect(0, 0, 1300, 800))
		pygame.draw.rect(window_data.window, ('aquamarine2'), pygame.Rect(0, 700, 1300, 100))

		# Add new snake block in the direction of movement and remove last block
		snek_data.body.insert(0, list(snek_data.head))
		snek_data.body.pop()

		# Checks if theres an active food if not generates a new one within the window
		if snack.spawned is False:
			game_objects.update_snack(snack, window_data)

		# Check for self collision
		if snek_data.head in snek_data.body[1::]:
			dead = True

		# Check for wall collision
		if snek_data.head in wall.cords:
			dead = True

		# Grow snek when colliding with food
		if snek_data.head == snack.cords:
			score += 1
			grow_tail(snek_data)
			snack.spawned = False

		### RENDERS, MOVE TO A DIFFERENT FILE
		# Rendering snake
		for pos in snek_data.body:
			pygame.draw.rect(window_data.window, colour_settings.snek_colour, pygame.Rect(pos[0], pos[1], snek_data.block_size, snek_data.block_size))
		
		# Rendering snack
		pygame.draw.rect(window_data.window, colour_settings.food_colour, pygame.Rect(snack.cords[0], snack.cords[1], snek_data.block_size, snek_data.block_size))
		
		# Rendering wall
		for pos in wall.cords:
			pygame.draw.rect(window_data.window, colour_settings.wall_colour, pygame.Rect((pos[0], pos[1]), (wall.size, wall.size)))

		# Breaks the loops and shows end screen when pressed
		if exit_button.draw(window_data.window):
			dead = True
		
		# Displays the score
		score_board(window_data, score)

	# Not so good players end up here...
	if dead:
		end_screen(window_data, score)
