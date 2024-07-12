import pygame, variables as v, presetColors as pC
from pygame import *


def main(window):
    if v.drawTopBar:
        # main bar, line, and background color
        pygame.draw.rect(window, pC.colors["black"], (0, 21, v.winDims[1], 2))
        pygame.draw.rect(window, v.topBarColor, (0, 0, v.winDims[0], 20))
        # "icons"
        pygame.draw.rect(window, pC.colors["fullRed"], (0, 0, 20, 20))
        pygame.draw.rect(window, pC.colors["fullBlue"], (20, 0, 20, 20))
        pygame.draw.rect(window, pC.colors["fullGreen"], (40, 0, 20, 20))
        pygame.draw.rect(window, pC.colors["fullPink"], (v.winDims[0]-60, 0, 60, 20))

    if v.testWindow:
        # top bar, borders
        pygame.draw.rect(window, pC.colors["black"], (v.tWPos[0], v.tWPos[1], v.tWBarDims[0], v.tWBarDims[1]))
        pygame.draw.rect(window, pC.colors["black"], ())

    # "desktop" background
    pygame.draw.rect(window, v.bgColor, (0, 21, v.winDims[0], v.winDims[1]-20))

    # update [IMPORTANT]
    pygame.display.update()
