import pygame


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

name = "KeyColor"

colorsIMG = pygame.image.load("colors.png")

up_down = False
down_down = False
left_down = False
right_down = False

pixels = []
