import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Display dimensions
display_width = 800
display_height = 600

# Car dimensions
car_width = 73

# Initialize display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PythonRace')
clock = pygame.time.Clock()

# Define functions
def car(x, y):
    pygame.draw.rect(gameDisplay, black, [x, y, car_width, 100])

def obstacles(obstacle_x, obstacle_y):
    pygame.draw.rect(gameDisplay, red, [obstacle_x, obstacle_y, 100, 100])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    score = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        # Obstacle movement
        obstacles(obstacle_startx, obstacle_starty)
        obstacle_starty += obstacle_speed

        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, display_width)
            score += 1

        if y < obstacle_starty + obstacle_height:
            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x+car_width > obstacle_startx and x+car_width < obstacle_startx+obstacle_width:
                crash()

        # Display score and instructions
        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Score: "+str(score), True, black)
        instruction_text = font.render("Press 'Q' to quit", True, black)
        gameDisplay.blit(score_text, (0, 0))
        gameDisplay.blit(instruction_text, (0, 30))

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
