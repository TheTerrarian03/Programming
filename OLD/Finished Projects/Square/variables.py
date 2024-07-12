import pygame
pygame.init()


colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "greedDark": (0, 150, 0),
    "blueDark": (0, 0, 255),
    "yellow": (255, 255, 0),
    "pink": (255, 192, 203),
    "greenLight": (0, 255, 0),
    "purple": (128, 0, 128),
    "blueLight": (0, 116, 255),
    "None": "None",
}

resX = 0
resY = 0
blockSize = 0
floorTopY = 0
topSpeed = 30
sideSpeed = 0
vertSpeed = 0
acc = 2
gravity = 1.5
X = 50
Y = 0

sa = None
s = None
floor = None

clock = pygame.time.Clock()
fps = 30

up_down = False
down_down = False
a_down = False
d_down = False
