import pygame


class Display:
    def __init__(self, res=(200, 200), bg=(50, 50, 50), title=None):
        self.res = res
        self.bg = bg
        self.disp = pygame.display.set_mode(self.res)

        if title:
            pygame.display.set_caption(title)

    def draw(self):
        pygame.draw.rect(self.disp, self.bg, (0, 0, self.res[0], self.res[1]))
    
    def dispUpdate(self):
        pygame.display.update()

class GraphGrid:
    def __init__(self, xMin, xMax, yMin, yMax, pointSize, backgroundColor, foregroundColor):
        # 0 is included, and not needed to be considered in the mins and maxes
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.ptSize = pointSize
        self.bgColor = backgroundColor
        self.fgColor = foregroundColor
        self.points = self.createPointList()
        self.axisPoints = self.createPointList()
        self.gridPoints = self.createPointList()
        print(self.xMin, self.xMax, self.yMin, self.yMax)
    
    def createPointList(self, value=0):
        newPoints = []
        for y in range(abs(self.xMin) + abs(self.xMax) + 1):
            row = []
            for x in range(abs(self.yMin) + abs(self.yMax) + 1):
                row.append(value)
            newPoints.append(row)
        
        return newPoints
    
    def setAllPoints(self, points, value):
        newPoints = points
        for y in range(self.xMin + self.xMax + 1):
            for x in range(self.yMin + self.yMax + 1):
                newPoints[x][y] = value

        return newPoints
    
    def printPoints(self):
        for row in self.points:
            print(row)
    
    def setPoint(self, x, y, value, pointsAreGraphCoords=True):
        if ((x > self.xMin) and (x < self.xMax)) and ((y > self.yMin) and (y < self.yMax)):
            if pointsAreGraphCoords:
                x = self.getListX(x)
                y = self.getListY(y)
        
            self.points[y][x] = value
    
    def setRowOfPoints(self, y, value):
        pass  # finish method eventually
    
    def setColumnOfPoints(self, x, value):
        pass  # finish method eventually
    
    def getListX(self, graphX):  # convert a graph x coord to a index for the list
        listX = graphX + abs(self.xMin)
        return listX
    
    def getListY(self, graphY):  # convert a graph y coord to a index for the list
        listY = -(graphY - self.yMax)
        return listY
    
    def getListIndexesFromGraphCoords(self, graphX, graphY):  # a function for handling converting both an x and y coords to a list index
        listX = self.getListX(graphX)
        listY = self.getListY(graphY)
        return [listX, listY]

    def setAxis(self, interval=1, x_axis=True, y_axis=True):
        # x-axis lines
        if x_axis:
            y = self.getListY(0)
            for x in range(len(self.points)):
                self.axisPoints[y][x] = 1
        
        # y-axis lines
        if y_axis:
            x = self.getListX(0)
            for y in range(len(self.points[x])):
                self.axisPoints[y][x] = 1
        
        # x-axis intervals
        if x_axis:
            y = self.getListY(-1)
            # set x to beginning
            x = self.xMin

    def drawAxis(self, displaySurface, color):
        for row in range(len(self.axisPoints)):
            for col in range(len(self.axisPoints[row])):
                if self.axisPoints[col][row] == 1:
                    pygame.draw.rect(displaySurface, color, (self.ptSize*col, self.ptSize*row, self.ptSize, self.ptSize))
            
    def drawPoints(self, displaySurface):
        for row in range(len(self.points)):
            for col in range(len(self.points[row])):
                if self.points[row][col]:
                    pygame.draw.rect(displaySurface, self.fgColor, (self.ptSize*col, self.ptSize*row, self.ptSize, self.ptSize))

class VisualGrid:
    def __init__(self, res, size, color):
        self.res = res
        self.size = size
        self.color = color
        self.chunks = []
    
    def setAllChunks(self, percentage):
        # if there is nothing in the list
        if len(self.chunks) == 0:
            for y in range(int(self.res[0]/self.size)):
                row = []
                for x in range(int(self.res[0]/self.size)):
                    row.append(0)
                self.chunks.append(row)
        # then, set values
        for row in range(len(self.chunks)):
            for col in range(len(self.chunks[row])):
                self.chunks[row][col] = percentage
    
    def drawPoints(self, displaySurface):
        for row in range(int(self.res[0]/self.size)):
            for col in range(int(self.res[1]/self.size)):
                pygame.draw.rect(displaySurface, self.color, (self.size*row, self.size*col, 1, 1))
    
    # for debugging
    def printChunks(self):
        for row in range(len(self.chunks)):
            print(row, self.chunks[row])
    
    def drawChunks(self, displaySurface):
        for row in range(int(self.res[0]/self.size)):
            for col in range(int(self.res[1]/self.size)):
                pygame.draw.rect(displaySurface, [(self.color[0]*self.chunks[row][col])/100, (self.color[1]*self.chunks[row][col])/100, (self.color[2]*self.chunks[row][col])/100], (self.size*col, self.size*row, self.size, self.size))