import pygame
import variables as v
import thinkrs
import mainOpen
import mainRes
import mainSize
import levelPicker
import level1


def stop():
    pygame.quit()
    quit()


mainOpen = mainOpen.main()
if not mainOpen:
    stop()

mainRes = mainRes.main()
if not mainRes:
    stop()

mainSize = mainSize.main()
if not mainSize:
    stop()

v.resX, v.resY = thinkrs.res(mainRes)
v.blockSize = thinkrs.size(mainSize)
v.sa = pygame.image.load("square.png")

if mainSize == 1:
    v.s = pygame.transform.scale(v.sa, (50, 50))
elif mainSize == 2:
    v.s = pygame.transform.scale(v.sa, (100, 100))
elif mainSize == 3:
    v.s = pygame.transform.scale(v.sa, (150, 150))

if mainRes == 1:
    v.floor = pygame.image.load("floor800.png")
elif mainRes == 2:
    v.floor = pygame.image.load("floor1080.png")
elif mainRes == 3:
    v.floor = pygame.image.load("floor1600.png")

v.floorTopY = v.resY - 100

level = levelPicker.main()
if not level:
    stop()

if level == 1:
    level1.main((v.resX, v.resY))
