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


# I have to import these libraries so that I can use the functions
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
enemy_Img = pygame.image.load('owl.png')
egg_Img = pygame.image.load('egg.png')


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


def egg(x, y):
    screen.blit(egg_Img, (x, y))


def enemy(x, y):
    screen.blit(enemy_Img, (x, y))


def is_colliding_with_egg(egg_X, egg_Y, player_X, player_Y, distance_max):
    distance_egg = math.sqrt(((egg_X - player_X) ** 2) + ((egg_Y - player_Y) ** 2))
    if distance_egg <= distance_max:
        return True
    else:
        return False


def is_colliding_with_enemy(enemy_X, enemy_Y, player_X, player_Y, distance):
    distance_enemy = math.sqrt(((enemy_X - player_X) ** 2) + ((enemy_Y - player_Y) ** 2))
    if distance_enemy <= distance:
        return True
    else:
        return False

# This is a function that determines the players position compared
# to the apple's position. If the distance between them is <= 28 then
# the function will return true to the variable distance__apple
# I can use this to check if the player is 'colliding' with it.
def is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y, distance):
    distance_apple = math.sqrt(((apple_X - player_X) ** 2) + ((apple_Y - player_Y) ** 2))
    if distance_apple <= distance:
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
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
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
            #game_loop()
            level_1()
    # this else statement sets up the inital rectangle and writes the text on it
    # it is also meant to be, if nothing is clicked or the mouse does not scroll
    # over it, the button does nothing.
    else:
        pygame.draw.rect(screen, (0, 200, 0), (150, 400, 200, 100))
    start_button_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_objects('Start', start_button_text, (0, 0, 0))
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
            print('quit')
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(screen, (200, 0, 0), (450, 400, 200, 100))
    quit_button_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_objects('Quit', quit_button_text, (0, 0, 0))
    text_rect.center = ((450 + (200 / 2)), (400 + (100 / 2)))
    screen.blit(text_surf, text_rect)


# I am making a function for every individual screen from here on out
# For example a screen for each level and the intro, winning, and death screens
def intro_screen():
    print('intro screen')
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


def level_3():
    print('level 3')
    player_X = 182
    player_Y = 486
    player_X_change = 0
    player_Y_change = 0
    apple_X = 486
    apple_Y = 314
    enemy_X_1 = 25
    enemy_Y_1 = 416
    enemy_X_2 = 312
    enemy_Y_2 = 268
    enemy_X_3 = 668
    enemy_Y_3 = 302
    egg_movement_speed = 1.3
    egg_X_1 = enemy_X_1 + 8
    egg_Y_1 = enemy_Y_1 + 16
    egg_X_2 = enemy_X_2 + 8
    egg_Y_2 = enemy_Y_2 + 16
    egg_X_3 = enemy_X_3 + 8
    egg_Y_3 = enemy_Y_3
    dead = False
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -.8
                if event.key == pygame.K_RIGHT:
                    player_X_change = .8
                if event.key == pygame.K_UP:
                    player_Y_change = -.8
                if event.key == pygame.K_DOWN:
                    player_Y_change = .8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        player_X += player_X_change
        player_Y += player_Y_change
        screen.fill((0,0,0))
        rectangles(150, 150, 96, 400, (202, 0, 254))
        rectangles(25, 400, 150, 64,(202, 0, 254))
        rectangles(150,54,400,96,(202, 0, 254))
        rectangles(296, 150, 64, 150, (202, 0, 254))
        rectangles(454, 150, 96, 200, (202, 0, 254))
        rectangles(550, 286, 150, 64, (202, 0, 254))
        player(player_X,player_Y)
        apple(apple_X, apple_Y)
        enemy(enemy_X_1, enemy_Y_1)
        enemy(enemy_X_2, enemy_Y_2)
        enemy(enemy_X_3, enemy_Y_3)

        level_3_text_line_1 = pygame.font.Font('freesansbold.ttf', 16)
        level_3_text_line_2 = pygame.font.Font('freesansbold.ttf', 16)
        text_surf, text_rect = text_objects("Owls will stop at nothing", level_3_text_line_1, (255,255,255))
        text_rect.center = (550,425)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("to get the apple...", level_3_text_line_2, (255,255,255))
        text_rect.center = (550,450)
        screen.blit(text_surf, text_rect)

        if player_Y >= 150 and player_X <= 247:
            if player_Y >= 518:
                player_X = 182
                player_Y = 486
            if player_X >= 214:
                player_X = 182
                player_Y = 486
            if player_Y >= 464:
                if player_X <= 150:
                    player_X = 182
                    player_Y = 486
            if player_X <= 25:
                player_X = 182
                player_Y = 486
            if player_Y <= 464 or player_Y >= 400:
                if player_X <= 150:
                    if player_Y >= 432:
                        player_X = 182
                        player_Y = 486
                    if player_Y <= 400:
                        player_X = 182
                        player_Y = 486
        if player_Y <= 54:
            player_X = 182
            player_Y = 486
        if player_Y <= 150:
            if player_X <= 150 or player_X >= 518:
                player_X = 182
                player_Y = 486
            if player_X >= 214 and player_X <= 296:
                if player_Y >= 118:
                    player_X = 182
                    player_Y = 486
            if player_X >= 328 and player_X <= 422:
                if player_Y >= 118:
                    player_X = 182
                    player_Y = 486
        if player_X >= 296 and player_X <= 328:
            if player_Y >= 118:
                if player_X <= 296 or player_X >= 328:
                    player_X = 182
                    player_Y = 486
        if player_Y >= 150 and player_X >= 422:
            if player_X <= 454:
                player_X = 182
                player_Y = 486
            if player_Y <= 254:
                if player_X >= 518:
                    player_X = 182
                    player_Y = 486
            if player_Y >= 254 and player_X >= 518:
                if player_Y <= 286:
                    player_X = 182
                    player_Y = 486
            if player_Y >= 318:
                player_X = 182
                player_Y = 486


        egg_X_1 += egg_movement_speed
        egg(egg_X_1, egg_Y_1)
        if egg_X_1 >= 222:
            egg_X_1 = enemy_X_1
        if egg_X_1 >= 150:
            egg(enemy_X_1, enemy_Y_1)

        egg_Y_2 -= egg_movement_speed
        egg(egg_X_2, egg_Y_2)
        if egg_Y_2 <= 62:
            egg_Y_2 = enemy_Y_2
        if egg_Y_2 <= 150:
            egg(enemy_X_2, enemy_Y_2)

        egg_X_3 -= egg_movement_speed
        egg(egg_X_3, egg_Y_3)
        if egg_X_3 <= 470:
            egg_X_3 = enemy_X_3
        if egg_X_3 <= 534:
            egg(enemy_X_3, enemy_Y_3)

        apple_collision = is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y, 16)
        if apple_collision:
            print('collide')
            intro_screen()

        enemy_collision_1 = is_colliding_with_enemy(enemy_X_1, enemy_Y_1, player_X, player_Y, 25)
        enemy_collision_2 = is_colliding_with_enemy(enemy_X_2, enemy_Y_2, player_X, player_Y, 25)
        enemy_collision_3 = is_colliding_with_enemy(enemy_X_3, enemy_Y_3, player_X, player_Y, 25)
        if enemy_collision_1 or enemy_collision_2 or enemy_collision_3:
            print('player died')
            player_X = 182
            player_Y = 486

        egg_collision_1 = is_colliding_with_egg(egg_X_1,egg_Y_1,player_X,player_Y, 20)
        egg_collision_2 = is_colliding_with_egg(egg_X_2,egg_Y_2,player_X,player_Y, 20)
        egg_collision_3 = is_colliding_with_egg(egg_X_3,egg_Y_3,player_X,player_Y, 20)
        if egg_collision_1 or egg_collision_2 or egg_collision_3:
            print('player died')
            player_X = 182
            player_Y = 486

        pygame.display.update()



def level_2():
    print('level 2')
    player_X = 400
    player_Y = 500
    player_X_change = 0
    player_Y_change = 0
    enemy_X = 402
    enemy_Y = 280
    enemy_X_change = -1.2
    enemy_Y_change = 0
    apple_X = 404
    apple_Y = 82
    dead = False
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -1
                if event.key == pygame.K_RIGHT:
                    player_X_change = 1
                if event.key == pygame.K_UP:
                    player_Y_change = -1
                if event.key == pygame.K_DOWN:
                    player_Y_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        if enemy_X >= 536:
            enemy_X_change = -1.2
        if enemy_X <= 268:
            enemy_X_change = 1.2

        player_X += player_X_change
        player_Y += player_Y_change
        enemy_X += enemy_X_change

        screen.fill((0,0,0))
        rectangles(368, 50, 96, 500, (255,0,0))
        rectangles(268, 248, 300, 96, (255,0,0))
        apple(apple_X,apple_Y)
        apple_collision = is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y, 16)
        if apple_collision:
            print('collide')
            level_3()
        enemy_collision = is_colliding_with_enemy(enemy_X, enemy_Y, player_X, player_Y, 25)
        if enemy_collision:
            print('player died')
            player_X = 400
            player_Y = 500
        player(player_X,player_Y)
        enemy(enemy_X,enemy_Y)

        level_2_text_line_1 = pygame.font.Font('freesansbold.ttf', 16)
        level_2_text_line_2 = pygame.font.Font('freesansbold.ttf', 16)
        level_2_text_line_3 = pygame.font.Font('freesansbold.ttf', 16)
        text_surf, text_rect = text_objects("Owls do not want the Snake", level_2_text_line_1, (255,255,255))
        text_rect.center = (175,150)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("to get the apple because they", level_2_text_line_2, (255,255,255))
        text_rect.center = (175,175)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("want it for themselves.", level_2_text_line_3, (255,255,255))
        text_rect.center = (175,200)
        screen.blit(text_surf, text_rect)


        if player_Y >= 518 or player_Y <= 50:
            player_X = 400
            player_Y = 500
        if player_Y >= 312:
            if player_X <= 368 or player_X >= 432:
                player_X = 400
                player_Y = 500
        if player_X >= 536 or player_X <= 268:
            player_X = 400
            player_Y = 500
        if player_X <= 368 or player_X >= 432:
            if player_Y <= 248:
                player_X = 400
                player_Y = 500


        pygame.display.update()


# Sets up the first level
def level_1():
    print('level 1')
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
                    player_X_change = -1
                if event.key == pygame.K_RIGHT:
                    player_X_change = 1
                if event.key == pygame.K_UP:
                    player_Y_change = -1
                if event.key == pygame.K_DOWN:
                    player_Y_change = 1
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

        level_1_text_line_1 = pygame.font.Font('freesansbold.ttf', 16)
        level_1_text_line_2 = pygame.font.Font('freesansbold.ttf', 16)
        level_1_text_line_3 = pygame.font.Font('freesansbold.ttf', 16)
        text_surf, text_rect = text_objects("Snakes like apples", level_1_text_line_1, (255,255,255))
        text_rect.center = (175,150)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("but,", level_1_text_line_2, (255,255,255))
        text_rect.center = (175,175)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("Snakes don't like the darkenss", level_1_text_line_3, (255,255,255))
        text_rect.center = (175,200)
        screen.blit(text_surf, text_rect)
        # this gets the returned value from the collision function. if it is
        # true it runs the if statement. I am going to make it so that if
        # the player hits the apple it goes to the next level. but for right now
        # it only prints out that the player model hit the apple model.
        apple_collision = is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y, 28)
        if apple_collision:
            print('collide')
            level_2()

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
