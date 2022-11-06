import pygame

from classes import *

# Dropdown menus colours when highlighted/not
COLOR_INACTIVE = ('aquamarine2')
COLOR_ACTIVE = ('aquamarine')
COLOR_LIST_INACTIVE = ('aquamarine2')
COLOR_LIST_ACTIVE = ('aquamarine')

# Options menu
def options(snek_data, colour_settings, window_data):

    # Option menus background
    bg_options_menu = create_background(window_data.width, window_data.height, 'aquamarine2')

	# Snek dropdown
    snek_colour_list = DropDown(
					[COLOR_INACTIVE, COLOR_ACTIVE],
					[COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
					50, 350, 200, 50, 
					pygame.font.SysFont(None, 30), 
					"Snek colour", ["white", "cyan", "pink", "blue", "red", "green", "yellow"])\
	
	# Food dropdown
    food_colour_list = DropDown(
					[COLOR_INACTIVE, COLOR_ACTIVE],
					[COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
					300, 350, 200, 50, 
					pygame.font.SysFont(None, 30), 
					"Food colour", ["white", "cyan", "pink", "blue", "red", "green", "yellow"])

	# Background dropdown
    background_colour_list = DropDown(
					[COLOR_INACTIVE, COLOR_ACTIVE],
					[COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
					550, 350, 200, 50, 
					pygame.font.SysFont(None, 30), 
					"Background colour", ["white", "cyan", "pink", "blue", "red", "green", "yellow"])
	
    running = True

    while running:

        pygame.display.update()

        # Options menu background colour
        #window_data.window.fill(white)
        window_data.window.blit(bg_options_menu.surface, (0, 0))

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

		# Options menu title
        fontbig = pygame.font.SysFont('Arial', 80)
        options_menu = fontbig.render('Options' , True , ('black'))
        window_data.window.blit(options_menu, (window_data.width / 2 - 150, 25))

		# Showcases the colour above snek colour menu
        pygame.draw.rect(window_data.window, colour_settings.snek_colour, pygame.Rect(140, 300, snek_data.snek_block_size * 2, snek_data.snek_block_size * 2))

		# Showcases the colour above food colour menu
        pygame.draw.rect(window_data.window, colour_settings.food_colour, pygame.Rect(390, 300, snek_data.snek_block_size * 2, snek_data.snek_block_size * 2))

		# Showcases the colour above background colour menu
        pygame.draw.rect(window_data.window, colour_settings.background_colour, pygame.Rect(640, 300, snek_data.snek_block_size * 2, snek_data.snek_block_size * 2))

		# updates the dropdown menu and changes the colour of the snek
        snek_colour_selected = snek_colour_list.update(event_list)
        if snek_colour_selected >= 0:
            snek_colour_list.main = snek_colour_list.options[snek_colour_selected]
            colour_settings.snek_colour = snek_colour_list.options[snek_colour_selected]

		# updates the dropdown menu and changes the colour of the food
        food_colour_selected = food_colour_list.update(event_list)
        if food_colour_selected >= 0:
            food_colour_list.main = food_colour_list.options[food_colour_selected]
            colour_settings.food_colour = food_colour_list.options[food_colour_selected]

		# updates the dropdown menu and changes the colour of the background
        background_colour_selected = background_colour_list.update(event_list)
        if background_colour_selected >= 0:
            background_colour_list.main = background_colour_list.options[background_colour_selected]
            colour_settings.background_colour = background_colour_list.options[background_colour_selected]
		
		#draws the dropdown menus
        snek_colour_list.draw(window_data.window)
        food_colour_list.draw(window_data.window)
        background_colour_list.draw(window_data.window)
