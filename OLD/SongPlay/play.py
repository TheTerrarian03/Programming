import pygame
import calls
import os


# normal pygame stuff
pygame.init()
windowImage = pygame.image.load("window.png")
display = pygame.display.set_mode((windowImage.get_rect().size))
display.blit(windowImage, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
fps = 15
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                outcome = calls.getCommand()
                print(str(outcome[0]), " -- ", outcome[1])
                if outcome[0] == 3:
                    running = False
    
    pygame.display.update()
    clock.tick(fps)

