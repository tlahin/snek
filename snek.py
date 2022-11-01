"""

SNAKE GAME PROJECT

todo:
    Add walls the snake has to avoid or else it dies
    Options/Settings? colours, speed, screen size etc...
    Score?
    AI to play the game itself?

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
cyan = (51, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 128, 255)
red = (255, 0, 0)
pink = (249, 173, 159)

#window init
pygame.display.set_caption("Epic Game")
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_menu = pygame.Surface((width, height))
bg_menu.fill(pygame.Color(white))
bg_play = pygame.Surface((width, height))
bg_play.fill(pygame.Color(black))

#loads the pictures and inits them
start_img = pygame.image.load("./resources/start_button.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (150, 50))
quit_img = pygame.image.load("./resources/quit_button.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (150, 50))

#2 different fronts
fontsmall = pygame.font.SysFont('Arial', 50)
fontbig = pygame.font.SysFont('Arial', 80)

#Button class
class button():

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

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

#Main menu buttons
start_button = button(width / 2 - 150 / 2, height / 2, start_img)
quit_button = button(width / 2 - 150 / 2, height / 2 + 55, quit_img)

#pause function
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

#snek stats
snek_size = 10
snek_position = [510, 500]
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
        window.fill(black)

        #print("snek_body", snek_body,"snek_position", snek_position)

        snek_body.insert(0, list(snek_position))
        snek_body.pop()

        #Checks if theres an active food if not generates a new one within the window
        if snack_spawned == False:
            snack_pos = [random.randint(0, width / 10 - 10) * 10, random.randint(0, height / 10 - 10) * 10]
            print(snack_pos)
            snack_spawned = True

        #Checks if snek collides with the food, if so it consumes it and grows
        if snek_position == snack_pos:
            grow_tail()
            snack_spawned = False

        #if snek collides with itself, game ends
        if snek_position in snek_body[1::]:
            dead = True

        #Renders the snek
        for pos in snek_body:
            pygame.draw.rect(window, cyan, pygame.Rect(pos[0], pos[1], snek_size, snek_size))

        pygame.draw.rect(window, pink, pygame.Rect(snack_pos[0], snack_pos[1], snek_size, snek_size))

    print("DEAD")

running = True
start = True

print("RUNNING")

#menu loop
while running:

    #menu background
    window.blit(bg_menu, (0, 0))

    #writes menu text on the screen
    menu = fontbig.render('Main Menu' , True , (black))
    window.blit(menu, (width / 2 - 200, height / 2 - 200))

    #start button rendering
    if start_button.draw(window):
        print("START")
        play()
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
