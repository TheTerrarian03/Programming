import pygame
import Variables as v


def create_screen():
    v.graph_screen = pygame.display.set_mode((abs(v.GraphXMIN) + abs(v.GraphXMAX),
                                              (abs(v.GraphYMIN) + abs(v.GraphYMAX))))
