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

#colours
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (50, 255, 255)
pink = (255, 0, 150)
blue = (0, 128, 255)
red = (255, 0, 0)

#window init
pygame.display.set_caption("Epic Game")
#window size
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_main_menu = pygame.Surface((width, height))
bg_main_menu.fill(pygame.Color(white))
bg_options_menu = pygame.Surface((width, height))
bg_options_menu.fill(pygame.Color(white))

#loads the pictures and scales them correctly
start_img = pygame.image.load("./resources/start_button.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (150, 50))
options_img = pygame.image.load("./resources/options_button.png").convert_alpha()
options_img = pygame.transform.scale(options_img, (150, 50))
quit_img = pygame.image.load("./resources/quit_button.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (150, 50))

#2 different fronts
fontsmall = pygame.font.SysFont('Arial', 50)
fontbig = pygame.font.SysFont('Arial', 80)

#Button class to create buttons with images
# pos = (x, y)
class image_button():

    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

	#checks for a event where you click the button and also renders it
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

#Button class to create buttons with plain colours
# pos = (x, y)
# size = (width, heigh)
class colour_button():

	def __init__(self, x, y, width, heigh, colour):

		self.rect = pygame.Rect((x, y), (width, heigh))
		self.colour = colour
		self.clicked = False

	#checks for a event where you click the button and also renders it
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

#Main menu buttons with images
start_button = image_button(width / 2 - 150 / 2, height / 2, start_img)
options_button = image_button(width / 2 - 150 / 2, height / 2 + 55, options_img)
quit_button = image_button(width / 2 - 150 / 2, height / 2 + 110, quit_img)

#optons menu buttons with colours
red_button = colour_button(50, 50, 100, 100, red)
blue_button = colour_button(50, 160, 100, 100, blue)

#pause function, pauses the game loop and only returns if you press space to unpause it or quits the game by closing the window
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

#settings for the gameloop
#0. snek colour
#1. game background colour
settings = [
	cyan,
	black
]
#'block' size of a singular element
snek_size = 10
#head starting position
snek_position = [510, 500]
#sneks starting body
snek_body = [
                [510, 500],
                [520, 500],
                [530, 500]
            ]

#snek grows by one block
def grow_tail():

    snek_body.append([-10, -10])
    print("GROWS")

#game loop
def play():

    #ARE WE ALIVE OR NOT?!
    dead = False

    #direction variables
    direction = 'LEFT'
    change_to = direction

    #speed and update speed
    fps = pygame.time.Clock()
    snek_speed = 5

    #snek food variables
    snack_spawned = False

    while not dead:

        fps.tick(snek_speed)
        pygame.display.update()

        #Gets the inputs such as key strokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_SPACE:
                    print("PAUSE")
                    if pause_game() == 1:
                        dead = True
                    print("RESUME")
                #debug functionality | grows the snake when pressing 'g'
                if event.key == pygame.K_g:
                    print("GROW")
                    grow_tail()

        #Prevents the snek from going backwards
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        #Moves the snek to the direction
        if direction == 'UP':
            snek_position[1] -= snek_size
        if direction == 'DOWN':
            snek_position[1] += snek_size
        if direction == 'LEFT':
            snek_position[0] -= snek_size
        if direction == 'RIGHT':
            snek_position[0] += snek_size

        #Checks if snek hits a wall and makes it come out the otherside
        if snek_position[0] < 0:
            snek_position[0] = width - snek_size
        elif snek_position[0] >= width:
            snek_position[0] = 0
        if snek_position[1] < 0:
            snek_position[1] = height - snek_size
        elif snek_position[1] >= height:
            snek_position[1] = 0

		#background back
        window.fill(settings[1])

        #Sets the 'new' aka moved position to the head of the list making the illusion of a moving snek
        snek_body.insert(0, list(snek_position))
        #removes the last element of the list aka the old position
        snek_body.pop()

        #Checks if theres an active food if not generates a new one within the window
        if snack_spawned == False:
            snack_pos = [random.randint(0, width / 10 - 10) * 10, random.randint(0, height / 10 - 10) * 10]
            snack_spawned = True

        #Checks if snek collides with the food, if so it consumes it and grows
        if snek_position == snack_pos:
            grow_tail()
            snack_spawned = False

        #if sneks position aka the head collides with the rest of the body itself, the game ends
        if snek_position in snek_body[1::]:
            dead = True

        #Renders the snek
        for pos in snek_body:
            pygame.draw.rect(window, settings[0], pygame.Rect(pos[0], pos[1], snek_size, snek_size))

		#renders the snacks
        pygame.draw.rect(window, pink, pygame.Rect(snack_pos[0], snack_pos[1], snek_size, snek_size))

    print("DEAD")

#Options menu
def options(settings):

	looping = True

	while looping:

		pygame.display.update()

		#background colour
		window.fill(settings[1])

		#options menu title
		options_menu = fontbig.render('Options' , True , (cyan))
		window.blit(options_menu, (width / 2 - 150, 25))

		#changes snek colour to red
		if red_button.draw(window):
			print("PRESSED_1")
			settings[0] = red
		#changes snek colour to blue
		if blue_button.draw(window):
			print("PRESSED_2")
			settings[0] = blue
		#renders the snek to see the colours
		for pos in snek_body:
			pygame.draw.rect(window, settings[0], pygame.Rect(pos[0], pos[1], snek_size, snek_size))
		#closes the options menu and goes back to mainm menu
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				looping = False

running = True
start = True

print("RUNNING")

#menu loop
while running:

	#menu background
	window.blit(bg_main_menu, (0, 0))

	#writes menu text on the screen using the bigfont variable
	main_menu = fontbig.render('Main Menu' , True , (cyan))
	window.blit(main_menu, (width / 2 - 200, height / 2 - 200))

	#start button rendering
	if start_button.draw(window):
		print("START")
		play()
	#options button rendering
	if options_button.draw(window):
		print("OPTIONS")
		options(settings)
	#quit button rendering
	if quit_button.draw(window):
		print("QUIT")
		pygame.quit()
	#close the window exits the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("EXIT")
			running = False

	pygame.display.flip()
