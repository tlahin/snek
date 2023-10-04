import pygame

# Create a dropdown menu with multiple choices
class DropDown():

	def __init__(self, color_menu, color_option, x, y, width, height, font, main, options):

		self.color_menu = color_menu
		self.color_option = color_option
		self.rect = pygame.Rect(x, y, width, height)
		self.font = font
		self.main = main
		self.options = options
		self.draw_menu = False
		self.menu_active = False
		self.active_option = -1

	def draw(self, surface):

		pygame.draw.rect(surface, self.color_menu[self.menu_active], self.rect, 0)
		msg = self.font.render(self.main, 1, (0, 0, 0))
		surface.blit(msg, msg.get_rect(center = self.rect.center))

		if self.draw_menu:
			for i, text in enumerate(self.options):
				rect = self.rect.copy()
				rect.y += (i+1) * self.rect.height
				pygame.draw.rect(surface, self.color_option[1 if i == self.active_option else 0], rect, 0)
				msg = self.font.render(text, 1, (0, 0, 0))
				surface.blit(msg, msg.get_rect(center = rect.center))

	def update(self, event_list):

		mouse_pos = pygame.mouse.get_pos()
		self.menu_active = self.rect.collidepoint(mouse_pos)
		self.active_option = -1

		for i in range(len(self.options)):
			rect = self.rect.copy()
			rect.y += (i + 1) * self.rect.height
			if rect.collidepoint(mouse_pos):
				self.active_option = i
				break

		if not self.menu_active and self.active_option == -1:
			self.draw_menu = False

		for event in event_list:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if self.menu_active:
					self.draw_menu = not self.draw_menu
				elif self.draw_menu and self.active_option >= 0:
					self.draw_menu = False
					return self.active_option
		return -1

# Create a button with colours.
class colour_button():

	def __init__(self, x, y, width, heigh, colour):

		self.rect = pygame.Rect((x, y), (width, heigh))
		self.colour = colour
		self.clicked = False

	# Render the button and create a event handler
	def draw(self, surface):

		mouse_action = False
		mouse_pos = pygame.mouse.get_pos()
		pygame.draw.rect(surface, self.colour, self.rect)

		if self.rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				mouse_action = True
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			return mouse_action

# Settings for the gameloop
class colour_settings():

	def __init__(self, snek_colour, background_colour, food_colour, wall_colour, power_up_colour):

		self.snek_colour = snek_colour
		self.background_colour = background_colour
		self.food_colour = food_colour
		self.wall_colour = wall_colour
		self.power_up_colour = power_up_colour

# Difficulty settings of the game
class difficulty_settings():
	def __init__(self, difficulty):

		self.difficulty = difficulty

# Struct that carries sneks data
class snek_struct():

	def __init__(self, snek_speed, snek_block_size, snek_head, snek_body):

		self.speed = snek_speed
		self.block_size = snek_block_size
		self.head = snek_head
		self.body = snek_body
		self.shield = False

# Struct that carries window data
class window_struct():

	def __init__(self, width, height):

		self.width = width
		self.height = height
		self.window = pygame.display.set_mode((width, height))
		self.game_width = width
		self.game_height = height - 100

class background():

	def __init__(self, width, height, colour):

		self.surface = pygame.Surface((width, height))
		self.colour = self.surface.fill(pygame.Color(colour))

# Create a button with text on it
class text_button():

	def __init__(self, x, y, width, heigh, text, font):

		self.clicked = False
		self.rect = pygame.Rect((x, y), (width, heigh))
		self.text = text
		self.font = font

	def draw(self, surface):

		msg = self.font.render(self.text, 1, (0, 0, 0))
		surface.blit(msg, msg.get_rect(center = self.rect.center))
		mouse_action = False
		mouse_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				mouse_action = True
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			return mouse_action

# Create an exit button with an image | x, y cords for topleft corner of the image
class exit_button():

	def __init__(self, x, y, image):

		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):

		surface.blit(self.image, (self.rect.x,  self.rect.y))
		mouse_pos = pygame.mouse.get_pos()
		mouse_action = False

		if self.rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				mouse_action = True
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			return mouse_action

# Create walls
class wall_struct():

	def __init__(self, wall_cords, length, size):

		self.cords = wall_cords
		self.length = length
		self.size = size

# Create snacks
class snack_struct():

	def __init__(self, snack_cords, size, spawned, wall):

		self.cords = snack_cords
		self.size = size
		self.spawned = spawned
		self.wall = wall

# Create power ups
class power_up_struct():

	def __init__(self, power_up_cords, size, spawned, wall, power):

		self.cords = power_up_cords
		self.size = size
		self.spawned = spawned
		self.wall = wall
		self.power_type = power

