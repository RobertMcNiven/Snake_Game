# Robert McNiven
# Integration Project
# My take on the classic game Snake

# References
# https://pythonprogramming.net/drawing-objects-pygame-tutorial/
# Tutorial I used for the text functions
# https://www.youtube.com/watch?v=FfWpgLFMI7w
# Tutorial I used to initiate the game and teach me player models
# https://www.flaticon.com/
# website I used to get the models for the player and apple
# https://en.bloggif.com/text?id=4b61524d1e87cf37615e77df36a1fd49
# Website I used to make the title name
# https://www.w3schools.com/colors/colors_rgb.asp
# Website I used to calculate RGB values
# https://www.pygame.org/docs/
# Where I got the pygame library and read about the offered
# functions that come with it


# I have to import these libraries so that i can use the functions
# they provide.
import pygame
import time
import math

# initialize pygame
pygame.init()

# create a screen x,y
display_X = 800
display_Y = 600
# Creating a variable of the screen
screen = pygame.display.set_mode((display_X, display_Y))

# Title and Icon at the top of the screen
pygame.display.set_caption('Snake')
icon = pygame.image.load('skull.png')
pygame.display.set_icon(icon)

# These are all the images I have to load into the game
player_Img = pygame.image.load('snake.png')
title_Gif = pygame.image.load('title.gif')
apple_Img = pygame.image.load('apple.png')


# I found I have to make functions of all the images I loaded in
# I am giving them arguments of x,y which will be their coordinates
# in the 800x600 window
def player(x, y):
    # Screen.blit basically means to draw whatever argument I give it
    # onto the display, in this case it is the player model
    screen.blit(player_Img, (x, y))


def apple(x, y):
    # In this case it is the goal, the apple
    screen.blit(apple_Img, (x, y))


def title(x, y):
    screen.blit(title_Gif, (x, y))


# This is a function that determines the players position compared
# to the apple's position. If the distance between them is <= 28 then
# the function will return true to the variable distance__apple
# I can use this to check if the player is 'colliding' with it.
def is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y):
    distance__apple = math.sqrt(((apple_X - player_X) ** 2) + ((apple_Y - player_Y) ** 2))
    if distance__apple <= 28:
        return True
    else:
        return False


# the next 2 functions were an easier way to create text on the screen in pygame
# I found it online in one of the tutorials I watched but I changed it to meet
# the needs I needed. How it works is that the second function calls to the
# first one. I use the first one to set the text I want to output and the color
# I want it to be. Then, I return that. In the second function, I set the type of font
# and the size. Finally it draws it to the screen with the built in 'blit' function
# in pygame
def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def message_display(text):
    text_surf, text_rect = text_objects(text, large_text)
    screen.blit(text_surf, text_rect)
    pygame.display.update()


# I made this function just as an easier way to draw the rectangles
# I use on the levels. Since in the pygame function you need to specify
# the display name every time, I figured since they will all be on one
# display, this was a good choice.
def rectangles(rect_X, rect_Y, rect_W, rect_H, color):
    # Here is the pygame function for drawing rectangles. I only have to give
    # it 1 less argument but it makes it easier to use
    pygame.draw.rect(screen, color, [rect_X, rect_Y, rect_W, rect_H])


# Creating the start button as a function so I can put it on multiple screens
# i.e. a winning screen, a death screen, amd the intro screen
def start_button():
    # gets the mouse position on the screen in the window
    mouse_pos = pygame.mouse.get_pos()
    # determines if the mouse is being clicked and returns a list of values, (0,0,0)
    # where the values are (mouse1,mouse2,mouse3). if the button is clicked
    # it returns a value of 1 rather than 0.
    click = pygame.mouse.get_pressed()
    # this if statement gives determines if the mouse click is within the
    # boundaries of the rectangle and executes the game loop if it is
    # it also changes the color if the mouse is over the button.
    if 150 + 200 > mouse_pos[0] > 150 and 400 + 100 > mouse_pos[1] > 400:
        pygame.draw.rect(screen, (0, 255, 0), (150, 400, 200, 100))
        if click[0] == 1:
            game_loop()
    # this else statement sets up the inital rectangle and writes the text on it
    # it is also meant to be, if nothing is clicked or the mouse does not scroll
    # over it, the button does nothing.
    else:
        pygame.draw.rect(screen, (0, 200, 0), (150, 400, 200, 100))
    start_button_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_objects('Start', start_button_text)
    text_rect.center = ((150 + (200 / 2)), (400 + (100 / 2)))
    screen.blit(text_surf, text_rect)


# this function is the same as the start button except it quits the window when
# clicked and is a different color, and has different text on it.
def quit_button():
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 450 + 200 > mouse_pos[0] > 450 and 400 + 100 > mouse_pos[1] > 400:
        pygame.draw.rect(screen, (255, 0, 0), (450, 400, 200, 100))
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(screen, (200, 0, 0), (450, 400, 200, 100))
    quit_button_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_objects('Quit', quit_button_text)
    text_rect.center = ((450 + (200 / 2)), (400 + (100 / 2)))
    screen.blit(text_surf, text_rect)


# I am making a function for every individual screen from here on out
# For example a screen for each level and the intro, winning, and death screens
def intro_screen():
    intro = True
    # starts an infinite while loop unless the player exits, presses the
    # quit button, or starts the game.
    while intro:
        # gets the events that happens. this needs to be here or the
        for event in pygame.event.get():
            # if the event that happens is the player pressing the quit button
            # in the upper right, the game exits and closes the window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # makes the background all black based on RGB values run through
        # the pygame function fill
        screen.fill((0, 0, 0))
        # places the title img at those coordinates through the title function
        # i made.
        title(280, 82)
        # places the player model at thees coordinates
        player(368, 150)
        start_button()
        quit_button()
        # this continuously updates the screen after every iteration of the while
        # loop.
        pygame.display.update()


# Sets up the first level
def level_1():
    # Sets up players initial x,y position
    player_X = 400
    player_Y = 450
    # sets up apple x,y position
    apple_X = 620
    apple_Y = 172
    # makes the initial player movement 0
    player_X_change = 0
    player_Y_change = 0
    not_dead = True
    # starts an infinite while loop(explain each part individually)
    while not_dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # continuously checks if the player is pressing the keys
            # depending on the key pressed, it changes the value of the player
            # x change or y change. that value is then added to the players
            # x or y value. They have to all be separate if statements because
            # I want the player to be able to go diagonal and for it to continuously
            # check if the player is changing directions.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -0.15
                if event.key == pygame.K_RIGHT:
                    player_X_change = 0.15
                if event.key == pygame.K_UP:
                    player_Y_change = -0.15
                if event.key == pygame.K_DOWN:
                    player_Y_change = 0.15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        # adds the player changed values to the current player x,y value
        player_X += player_X_change
        player_Y += player_Y_change
        # sets up the screen
        screen.fill((0, 0, 0))
        # uses my rectangle function to draw the 2 rectangles needed to make the course
        # for level 1
        rectangles(368, 200, 96, 300, (255, 105, 180))
        rectangles(368, 136, 300, 96, (255, 105, 180))
        # places the player model on the x,y coordinates given to it.
        player(player_X, player_Y)
        # places the apple on the coordinates specified.
        # I made it at the end of the course
        apple(apple_X, apple_Y)
        # this gets the returned value from the collision function. if it is
        # true it runs the if statement. I am going to make it so that if
        # the player hits the apple it goes to the next level. but for right now
        # it only prints out that the player model hit the apple model.
        collision = is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y)
        if collision:
            print('collide')

        # these next statements set the boundaries specific to level 1. I have
        # to do these separate for each level because each course will be different
        # there might be a way to do this easier in a function, i need to
        # research it
        # since there are 2 rectangles made, I had to make separate boundaries
        # for each one
        # if the player model hits these boundaries it gets reset to the start
        # position.
        if player_Y >= 200:
            if player_X <= 368 or player_X >= 432:
                player_X = 400
                player_Y = 450
            if player_Y >= 468:
                player_X = 400
                player_Y = 450
        if player_Y <= 200:
            if player_X <= 368 or player_X >= 636:
                player_X = 400
                player_Y = 450
            if player_Y < 136:
                player_X = 400
                player_Y = 450
        pygame.display.update()


# This was actually the first function I made for the game just to initialize it
# and make sure the library works.
def game_loop():
    print('game loop is running')
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            level_1()
            # This line and the "init" line always needs to be here.
            # it initializes then updates the game constantly
            pygame.display.update()


# This starts the game up always at the intro screen by running the intro screen
# function
intro_screen()
