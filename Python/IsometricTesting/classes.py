import pygame


class Tile:
    def __init__(self, imgName, resizeTo, gridPos):
        self.imgName = imgName
        self.resizeTo = resizeTo
        self.gridPos = gridPos

        self.img = pygame.transform.scale(pygame.image.load(imgName), resizeTo)
        self.isoPos = self.calcPos()
    
    def calcPos(self):
        x = (self.gridPos[0] * 0.5 * self.resizeTo[0])  + (self.gridPos[1] * -0.5 * self.resizeTo[1])
        y = (self.gridPos[0] * 0.25 * self.resizeTo[1]) + (self.gridPos[1] * 0.25 * self.resizeTo[1])
        return [x, y]
    
    def setGlobalOffset(self, offX, offY):
        self.offX = offX
        self.offY = offY
    
    def changeGridPos(self, xChange, yChange):
        self.gridPos = [self.gridPos[0]+xChange, self.gridPos[1]+yChange]

    def draw(self, surface):
        self.isoPos = self.calcPos()
        # print(self.gridPos, self.isoPos)
        surface.blit(self.img, [self.isoPos[0]+self.offX, self.isoPos[1]+self.offY])