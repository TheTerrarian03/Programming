import pygame
import variables as v
import thinkrs
import level1

v.resX, v.resY = thinkrs.res(2)
v.blockSize = thinkrs.size(1)
v.sa = pygame.image.load("square.png")

v.s = pygame.transform.scale(v.sa, (50, 50))
v.floor = pygame.image.load("floor1080.png")
v.floorTopY = v.resY - 100

level1.main((v.resX, v.resY))
