import pygame
import time

# Variables
resX = 1600
resY = 900
floorY = resY - 200
trashX = 50
trashY = floorY - 100

colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 150, 0),
        "blue": (0, 0, 255),
        "purple": (128, 0, 128),
        "blueLight": (0, 153, 255),
}

# Pygame
pygame.init()
game = pygame.display.set_mode((resX, resY))


def eventHandling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass


def drawing():
    game.fill(colors["blueLight"])

    pygame.display.update()


while True:
    eventHandling()
    drawing()