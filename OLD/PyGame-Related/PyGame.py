import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 220, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))  # there must be two parenthesis and a tuple.
pygame.display.set_caption("Slither")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)  # (I'm-Not-Sure, font size)  MUST DO THIS TO DISPLAY FONT


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)  # message, true for antialiasing, color
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])  # places the screen_text object


def gameLoop():
    def snake(block_size, snakeList):
        for XnY in snakeList:
            pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])  # top-left x, y, width, height

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    block_size = 10

    fps = 30

    randAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    randAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not gameExit:  # game loop

        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()
                # mine
                elif event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                # end of mine

        for event in pygame.event.get():  # event-handling loop
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeList = []
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        snake(block_size, snakeList)
        pygame.display.update()  # updates specific area, no parameters = update all, what most normal people use

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            randAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

        clock.tick(fps)

    pygame.quit()  # un-initialize it
    quit()  # exits out of python

gameLoop()
