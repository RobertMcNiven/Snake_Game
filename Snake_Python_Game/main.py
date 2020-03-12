# Robert McNiven
# Integration Project
# Snake

# References

# https://www.flaticon.com/
# website I used to get the models for the player and apple

# https://en.bloggif.com/text?id=4b61524d1e87cf37615e77df36a1fd49
# Website I used to make the title name

# https://www.w3schools.com/colors/colors_rgb.asp
# Website I used to calculate RGB values

# https://www.pygame.org/docs/
# Where I got the pygame library and read about the offered
# functions that come with it

#https://soundcloud.com/eric-skiff/prologue
#https://creativecommons.org/licenses/by/3.0/
#I used the song Prologue by Eric Skiff. I have provided
#the link to the song and license he used.


# I have to import these libraries so that I can use the functions
# they provide.
import pygame
import math

from pygame import mixer

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

#The music files I have to load in
mixer.music.load('Prologue.mp3')
mixer.music.play(-1)


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

#Function that checks if the player  model is coming in contact with the egg model
def is_colliding_with_egg(egg_X, egg_Y, player_X, player_Y, distance_max):
    distance_egg = math.sqrt(((egg_X - player_X) ** 2) + ((egg_Y - player_Y) ** 2))
    if distance_egg <= distance_max:
        return True
    else:
        return False

#function that checks if the player model is coming in contact with the enemy model
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



# I made this function just as an easier way to draw the rectangles
# I use on the levels. Since in the pygame function you need to specify
# the display name every time, I figured since they will all be on one
# display, this was a good choice.
def rectangles(rect_X, rect_Y, rect_W, rect_H, color):
    # Here is the pygame function for drawing rectangles. I only have to give
    # it 1 less argument but it makes it easier to use
    pygame.draw.rect(screen, color, [rect_X, rect_Y, rect_W, rect_H])

#initializing the death count variable
death_count = 0
#passing the death count variable through the death count display function
#this allows me to place the counter at a specific point on the screen that will
#translate to every level
def death_count_display():
    global death_count
    deaths = pygame.font.Font('freesansbold.ttf', 16)
    text_surf, text_rect = text_objects("Deaths: ", deaths, (255,255,255))
    text_rect.center = (675,500)
    screen.blit(text_surf, text_rect)

    number_of_deaths = pygame.font.Font('freesansbold.ttf', 16)
    text_surf, text_rect = text_objects(str(death_count), number_of_deaths, (255,255,255))
    text_rect.center = (725,500)
    screen.blit(text_surf, text_rect)


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

#Level 3
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
    egg_movement_speed = 2.1
    egg_X_1 = enemy_X_1 + 8
    egg_Y_1 = enemy_Y_1 + 16
    egg_X_2 = enemy_X_2 + 8
    egg_Y_2 = enemy_Y_2 + 16
    egg_X_3 = enemy_X_3 + 8
    egg_Y_3 = enemy_Y_3
    global death_count
    dead = False

#This starts the infinite loop for the level until the player reaches the apple
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -1.25
                if event.key == pygame.K_RIGHT:
                    player_X_change = 1.25
                if event.key == pygame.K_UP:
                    player_Y_change = -1.25
                if event.key == pygame.K_DOWN:
                    player_Y_change = 1.25
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        player_X += player_X_change
        player_Y += player_Y_change
        screen.fill((0,0,0))
#Drawing all the rectangles and models to the screen
        rectangles(150, 150, 96, 400, (202, 0, 254))
        rectangles(25, 400, 150, 64,(202, 0, 254))
        rectangles(150,54,400,96,(202, 0, 254))
        rectangles(296, 150, 64, 150, (202, 0, 254))
        rectangles(454, 150, 96, 200, (202, 0, 254))
        rectangles(550, 286, 150, 64, (202, 0, 254))
        player(player_X,player_Y)
        apple(apple_X, apple_Y)
        death_count_display()
        enemy(enemy_X_1, enemy_Y_1)
        enemy(enemy_X_2, enemy_Y_2)
        enemy(enemy_X_3, enemy_Y_3)

#Writing the text to the screen for level 3
        level_3_text_line_1 = pygame.font.Font('freesansbold.ttf', 16)
        level_3_text_line_2 = pygame.font.Font('freesansbold.ttf', 16)
        text_surf, text_rect = text_objects("Owls will stop at nothing", level_3_text_line_1, (255,255,255))
        text_rect.center = (550,425)
        screen.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects("to get the apple...", level_3_text_line_2, (255,255,255))
        text_rect.center = (550,450)
        screen.blit(text_surf, text_rect)

#Setting the boundaries for this level
        if player_Y >= 150 and player_X <= 247:
            if player_Y >= 518:
                player_X = 182
                player_Y = 486
                death_count += 1
            if player_X >= 214:
                player_X = 182
                player_Y = 486
                death_count += 1
            if player_Y >= 464:
                if player_X <= 150:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
            if player_X <= 25:
                player_X = 182
                player_Y = 486
                death_count += 1
            if player_Y <= 464 or player_Y >= 400:
                if player_X <= 150:
                    if player_Y >= 432:
                        player_X = 182
                        player_Y = 486
                        death_count += 1
                    if player_Y <= 400:
                        player_X = 182
                        player_Y = 486
                        death_count += 1
        if player_Y <= 54:
            player_X = 182
            player_Y = 486
            death_count += 1
        if player_Y <= 150:
            if player_X <= 150 or player_X >= 518:
                player_X = 182
                player_Y = 486
                death_count += 1
            if player_X >= 214 and player_X <= 296:
                if player_Y >= 118:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
            if player_X >= 328 and player_X <= 422:
                if player_Y >= 118:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
        if player_X >= 296 and player_X <= 328:
            if player_Y >= 118:
                if player_X <= 296 or player_X >= 328:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
        if player_Y >= 150 and player_X >= 422:
            if player_X <= 454:
                player_X = 182
                player_Y = 486
                death_count += 1
            if player_Y <= 254:
                if player_X >= 518:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
            if player_Y >= 254 and player_X >= 518:
                if player_Y <= 286:
                    player_X = 182
                    player_Y = 486
                    death_count += 1
            if player_Y >= 318:
                player_X = 182
                player_Y = 486
                death_count += 1
#each reset is also accompanied by adding 1 to the death count

#These next statements set the boundaries for the eggs and also make them move
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

#checking if the player is hitting the apple
        apple_collision = is_colliding_with_apple(apple_X, apple_Y, player_X, player_Y, 16)
        if apple_collision:
            print('collide')
            intro_screen()

#Checking if the player is hitting any of the 3 enemies
        enemy_collision_1 = is_colliding_with_enemy(enemy_X_1, enemy_Y_1, player_X, player_Y, 25)
        enemy_collision_2 = is_colliding_with_enemy(enemy_X_2, enemy_Y_2, player_X, player_Y, 25)
        enemy_collision_3 = is_colliding_with_enemy(enemy_X_3, enemy_Y_3, player_X, player_Y, 25)
        if enemy_collision_1 or enemy_collision_2 or enemy_collision_3:
            print('player died')
            player_X = 182
            player_Y = 486
            death_count += 1

#Checking to see if the player is hitting any of the eggs
        egg_collision_1 = is_colliding_with_egg(egg_X_1,egg_Y_1,player_X,player_Y, 20)
        egg_collision_2 = is_colliding_with_egg(egg_X_2,egg_Y_2,player_X,player_Y, 20)
        egg_collision_3 = is_colliding_with_egg(egg_X_3,egg_Y_3,player_X,player_Y, 20)
        if egg_collision_1 or egg_collision_2 or egg_collision_3:
            print('player died')
            player_X = 182
            player_Y = 486
            death_count += 1

        pygame.display.update()


#level 2
def level_2():
    print('level 2')
    player_X = 400
    player_Y = 500
    player_X_change = 0
    player_Y_change = 0
    enemy_X = 402
    enemy_Y = 280
    enemy_X_change = -1.2
    #enemy_Y_change = 0
    apple_X = 404
    apple_Y = 82
    global death_count
    dead = False
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -1.35
                if event.key == pygame.K_RIGHT:
                    player_X_change = 1.35
                if event.key == pygame.K_UP:
                    player_Y_change = -1.35
                if event.key == pygame.K_DOWN:
                    player_Y_change = 1.35
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        if enemy_X >= 536:
            enemy_X_change = -1.75
        if enemy_X <= 268:
            enemy_X_change = 1.75

        player_X += player_X_change
        player_Y += player_Y_change
        enemy_X += enemy_X_change

#creates the rectangles for level 2
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
            death_count += 1
        player(player_X,player_Y)
        enemy(enemy_X,enemy_Y)

#Writes the text to the second level
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


        death_count_display()

#Sets boundaries for level 2
        if player_Y >= 518 or player_Y <= 50:
            player_X = 400
            player_Y = 500
            death_count += 1
            print(death_count)
        if player_Y >= 312:
            if player_X <= 368 or player_X >= 432:
                player_X = 400
                player_Y = 500
                death_count += 1
                print(death_count)
        if player_X >= 536 or player_X <= 268:
            player_X = 400
            player_Y = 500
            death_count += 1
            print(death_count)
        if player_X <= 368 or player_X >= 432:
            if player_Y <= 248:
                player_X = 400
                player_Y = 500
                death_count += 1
                print(death_count)


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
    global death_count
    death_count = 0
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
                    player_X_change = -1.4
                if event.key == pygame.K_RIGHT:
                    player_X_change = 1.4
                if event.key == pygame.K_UP:
                    player_Y_change = -1.4
                if event.key == pygame.K_DOWN:
                    player_Y_change = 1.4
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
        death_count_display()


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
                death_count += 1
                print(death_count)
            if player_Y >= 468:
                player_X = 400
                player_Y = 450
                death_count += 1
                print(death_count)
        if player_Y <= 200:
            if player_X <= 368 or player_X >= 636:
                player_X = 400
                player_Y = 450
                death_count += 1
                print(death_count)
            if player_Y < 136:
                player_X = 400
                player_Y = 450
                death_count += 1
                print(death_count)
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
