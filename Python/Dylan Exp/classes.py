import math
import pygame
from random import choice as rancho


class CollisionPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.coord = (x, y)

class Shape:
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius
        self.topLeft = (self.center[0]-self.radius, self.center[1]-self.radius)
        self.collisionPoints = []
    
    def changeCenterPosition(self, xChange, yChange):
        self.center = [self.center[0]+xChange, self.center[1]+yChange]
        self.topLeft = (self.center[0]-self.radius, self.center[1]-self.radius)

    def makeCollisionBox(self, colors):
        self.collisionPoints = []
        # make box around circle
        for x in range(self.radius*2):
            for y in range(self.radius*2):
                self.collisionPoints.append(CollisionPoint(x, y, rancho(colors)))
    
    def makeCollisionCircleFilled(self, colors):
        self.collisionPoints = []
        # make filled in circle
        for x in range(-self.radius, self.radius):
            for y in range(-self.radius, self.radius):
                if math.floor(x*x) + math.floor(y*y) <= self.radius*self.radius:
                    print(x, y)
                    self.collisionPoints.append(CollisionPoint(x+self.radius, y+self.radius, rancho(colors)))
    
    def makeCollisionCircleBorder(self, colors):
        self.collisionPoints = []
        # make circle edge
        for angle in range(360):
            x = round(self.radius * math.cos(angle * (math.pi / 180)))
            y = round(self.radius * math.sin(angle * (math.pi / 180)))
            self.collisionPoints.append(CollisionPoint(x+self.radius, y+self.radius, rancho(colors)))

    def getCoordList(self):
        coords = []
        for point in self.collisionPoints:
            coords.append(point.coord)
        
        return coords

    def draw(self, display):
        pygame.draw.circle(display, self.color, self.center, self.radius)
    
    def drawCollisionPoints(self, display):
        for point in self.collisionPoints:
            pointLeft = self.topLeft[0] + point.x
            pointTop = self.topLeft[1] + point.y
            pygame.draw.rect(display, point.color, (pointLeft, pointTop, 1, 1))