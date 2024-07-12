import pygame
from pygame import *
import variables as v
import handleDrawing as hD


pygame.init()
v.display = pygame.display.set_mode(v.winDims, pygame.RESIZABLE)
pygame.display.set_caption("Tester Window")
print("Pygame and window initialized")

while v.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit button pressed")
            v.running = False
        if event.type == pygame.VIDEORESIZE:
            print("new res: " + str(event.w) + "x" + str(event.h))
            v.winDims = [event.w, event.h]
    hD.main(v.display)
    v.mainClock.tick(v.mainFPS)

quit()
