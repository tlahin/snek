import pygame

class DropDown():

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
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
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
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

# Settings for the gameloop
class create_settings():

	def __init__(self, snek_colour, background_colour, food_colour):
		self.snek_colour = snek_colour
		self.background_colour = background_colour
		self.food_colour = food_colour
    
# Create a button using images.
class image_button():

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

# Create a button with colours.
class colour_button():

    def __init__(self, x, y, width, heigh, colour):
        self.rect = pygame.Rect((x, y), (width, heigh))
        self.colour = colour
        self.clicked = False

	# Render the button and create a event handler
    def draw(self, window):
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
