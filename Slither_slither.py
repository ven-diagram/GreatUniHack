# import the modules
import pygame
import random

# initialize the module
pygame.init()

# colors
white = (0, 0, 0)
black = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)

# window display
display_width = 800
display_height = 600

# returns a python.game surface object.
gameDisplay = pygame.display.set_mode((display_width, display_height))

# To add a title:
pygame.display.set_caption("Slither")

# Sets the icon for the game. NOTE: Best Icon size is 32X32.
icon = pygame.image.load('Slither_apple.png')
icon = pygame.transform.scale(icon, (48, 48)) 
pygame.display.set_icon(icon)

# To import an image.
img = pygame.image.load('Slither_snakehead.png')
img = pygame.transform.scale(img, (32, 48)) 
img2 = pygame.image.load('Slither_apple.png')
img2 = pygame.transform.scale(img2, (48, 48)) 

# 'flip book' updates entire surface
pygame.display.flip()

# updates surface (blank to update entire surface)

# Returns a pygame Clock object
clock = pygame.time.Clock()

block_size = 20
apple_thickness = 30
FPS = 18

direction = "right"

# Font size
small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)


def score(score):
    text = small_font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def rand_apple_gen():
    rand_apple_x = round(random.randrange(0, display_width - apple_thickness))
    rand_apple_y = round(random.randrange(0, display_height - apple_thickness))
    return rand_apple_x, rand_apple_y


rand_apple_x, rand_apple_y = rand_apple_gen()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither", green, -100, "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black, -30)
        message_to_screen("The more apples you eat, the longer you get", black,
                          10)
        message_to_screen("If you run into yourself or the edges, you die!",
                          black, 50)
        message_to_screen("Press C to play, P to pause, or Q to quit.", black,
                          180)
        pygame.display.update()
        clock.tick(5)


def snake(block_size, snake_list):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))

    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, green,
                         [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = med_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


# prints all events to console


def game_loop():
    global direction
    direction = "right"
    game_exit = False
    game_over = False

    # Will be the leader of the #1 block of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0

    # list is for the length of the snake (Note: the last item in list is
    # the head)
    snake_list = []
    snake_length = 1

    rand_apple_x, rand_apple_y = rand_apple_gen()

    while not game_exit:
        if game_over is True:
            message_to_screen("Game Over", red, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to quit", black,
                              y_displace=50, size="medium")
            pygame.display.update()

        while game_over is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        # Creates the boundaries for the game
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height\
                or lead_y < 0:
            game_over = True

        # Adds or subtracts from lead_x
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Sets background to white
        gameDisplay.fill(white)

        # Draw a rectangle (where, color, [dimensions])
        # pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y,
        # apple_thickness, apple_thickness])
        apple = img2
        gameDisplay.blit(apple, [rand_apple_x, rand_apple_y, apple_thickness,
                                 apple_thickness])

        # creates the snake and will make it longer by appending last known
        # place
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        snake(block_size, snake_list)
        score(snake_length - 1)
        pygame.display.update()

        if lead_x > rand_apple_x and lead_x < rand_apple_x + apple_thickness\
                or \
                                        lead_x + block_size > rand_apple_x \
                        and lead_x + block_size < rand_apple_x + \
                        apple_thickness:

            if lead_y > rand_apple_y and lead_y < rand_apple_y + \
                    apple_thickness:
                rand_apple_x, rand_apple_y = rand_apple_gen()
                snake_length += 1

            elif lead_y + block_size > rand_apple_y and lead_y + block_size \
                    < rand_apple_y + apple_thickness:
                rand_apple_x, rand_apple_y = rand_apple_gen()
                snake_length += 1

        # Specify FPS
        clock.tick(FPS)

    # Hard coding = having the parameters set in other parameters

    # updates the screen with the created text
    # pygame.display.update()

    # un-initialize the module
    pygame.quit()
    quit()


game_intro()
game_loop()

