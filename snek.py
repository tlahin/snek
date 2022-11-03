"""

SNAKE GAME PROJECT

working on:

	options button and its features
	make settings list more readable

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
import random

pygame.init()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (50, 255, 255)
pink = (255, 0, 150)
blue = (0, 128, 255)
red = (255, 0, 0)

# Window init
pygame.display.set_caption("Epic Game")
# Window size
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_main_menu = pygame.Surface((width, height))
bg_main_menu.fill(pygame.Color(white))
bg_options_menu = pygame.Surface((width, height))
bg_options_menu.fill(pygame.Color(white))

# Loads the pictures and scales them correctly
start_img = pygame.image.load("./resources/start_button.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (150, 50))
options_img = pygame.image.load("./resources/options_button.png").convert_alpha()
options_img = pygame.transform.scale(options_img, (150, 50))
quit_img = pygame.image.load("./resources/quit_button.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (150, 50))

# Fonts
fontsmall = pygame.font.SysFont('Arial', 50)
fontbig = pygame.font.SysFont('Arial', 80)

class image_button():
    """ Create a button using images. """
    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

	# Render the button and create a event handler
    def draw(self, surface):
        mouse_action = False
        mouse_pos = pygame.mouse.get_pos()
        surface.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                mouse_action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            return mouse_action

class colour_button():
    """ Create a button with colours. """
    def __init__(self, x, y, width, heigh, colour):
        self.rect = pygame.Rect((x, y), (width, heigh))
        self.colour = colour
        self.clicked = False

	# Render the button and create a event handler
    def draw(self, surface):
        mouse_action = False
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(window, self.colour, self.rect)
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                mouse_action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            return mouse_action

# Main menu buttons
start_button = image_button(width / 2 - 150 / 2, height / 2, start_img)
options_button = image_button(width / 2 - 150 / 2, height / 2 + 55, options_img)
quit_button = image_button(width / 2 - 150 / 2, height / 2 + 110, quit_img)

# Options menu buttons
red_button = colour_button(50, 50, 100, 100, red)
blue_button = colour_button(50, 160, 100, 100, blue)

# Pause game loop until space is pressed
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

# Settings for the gameloop
#0. Snek colour
#1. Game background colour
settings = [
	cyan,
	black
]
# Initializing snek
snek_speed = 10
snek_block_size = 10
snek_head = [510, 500]
snek_body = [
				[510, 500],
				[520, 500],
				[530, 500]
			]

# Grow snek
def grow_tail():

	snek_body.append([-10, -10])
	print("GROWS")

# Game loop
def play():

	dead = False
	snack_spawned = False
	new_direction = 'LEFT'
	current_direction = new_direction
	fps = pygame.time.Clock()

	while not dead:

		fps.tick(snek_speed)
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
					grow_tail()

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
			snek_head[1] -= snek_block_size
		if new_direction == 'DOWN':
			snek_head[1] += snek_block_size
		if new_direction == 'LEFT':
			snek_head[0] -= snek_block_size
		if new_direction == 'RIGHT':
			snek_head[0] += snek_block_size

		# Checks if snek hits a wall and makes it come out the otherside
		if snek_head[0] < 0:
			snek_head[0] = width - snek_block_size
		elif snek_head[0] >= width:
			snek_head[0] = 0
		if snek_head[1] < 0:
			snek_head[1] = height - snek_block_size
		elif snek_head[1] >= height:
			snek_head[1] = 0

		# Set background colour
		window.fill(settings[1])

		# Add new snake block in the direction of movement and remove last block
		snek_body.insert(0, list(snek_head))
		snek_body.pop()

		# Checks if theres an active food if not generates a new one within the window
		if snack_spawned == False:
			snack_pos = [random.randint(0, width / 10 - 10) * 10, random.randint(0, height / 10 - 10) * 10]
			snack_spawned = True

		# Grow snek when colliding with food
		if snek_head == snack_pos:
			grow_tail()
			snack_spawned = False

		# Check for self collision
		if snek_head in snek_body[1::]:
			dead = True

        # Rendering snake and snacks
		for pos in snek_body:
			pygame.draw.rect(window, settings[0], pygame.Rect(pos[0], pos[1], snek_block_size, snek_block_size))

		pygame.draw.rect(window, pink, pygame.Rect(snack_pos[0], snack_pos[1], snek_block_size, snek_block_size))

	print("DEAD")

# Options menu
def options(settings):

	looping = True

	while looping:
		pygame.display.update()

		window.fill(settings[1])

		options_menu = fontbig.render('Options' , True , (cyan))
		window.blit(options_menu, (width / 2 - 150, 25))

		if red_button.draw(window):
			print("PRESSED_1")
			settings[0] = red

		if blue_button.draw(window):
			print("PRESSED_2")
			settings[0] = blue

		for pos in snek_body:
			pygame.draw.rect(window, settings[0], pygame.Rect(pos[0], pos[1], snek_block_size * 2, snek_block_size * 2))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				looping = False

running = True
start = True

print("RUNNING")

# Menu loop
while running:

	window.blit(bg_main_menu, (0, 0))
	main_menu = fontbig.render('Main Menu' , True , (cyan))
	window.blit(main_menu, (width / 2 - 200, height / 2 - 200))

	if start_button.draw(window):
		print("START")
		play()

	if options_button.draw(window):
		print("OPTIONS")
		options(settings)
        
	if quit_button.draw(window):
		print("QUIT")
		pygame.quit()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("EXIT")
			running = False

	pygame.display.flip()
